//============================================================================
// Name        : codejam_2012_q.cpp
// Author      : festony
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

const long double PI = 3.141592654;

const long double MAX_RADIUS = PI;
const long double MIN_RADIUS = -PI;

enum SIDE_DIRECTION {
	HORIZONTAL = 0, VERTICAL = 1
};

enum SIDE_POINT_DIRECTION {
	LEFT_UP = 0, RIGHT_DOWN = 1
};

enum BLOCK_SIDE_DIRECTION {
	UP = 0, LEFT = 1, DOWN = 2, RIGHT = 3
};

enum BLOCK_POINT_DIRECTION {
	UPRIGHT = 0, UPLEFT = 1, DOWNLEFT = 2, DOWNRIGHT = 3
};

enum POINT_CONNECTIVITY {
	UNKNOWN = -1, PASS = 0, PASS_OR_DESTROY = 1, REFLECT = 2, FULL_REFLECT = 3, DESTROY = 4
};

const long double side_dir_angle[] = { PI / 2, -PI, -PI / 2, 0 };
const long double point_dir_angle[] = { PI / 4, PI * 3 / 4, -PI * 3 / 4, -PI / 4 };

struct point;
struct side;
struct block;
struct ray;
struct reflection;
struct mirror_room;

void cut_radius_in_range(long double & r);
void swap_pointers(void * * p1, void * * p2);
side * get_common_side(point * p1, point * p2);
side * get_common_side(block * b1, block * b2);

int compare_double(const long double & d1, const long double & d2) {
	int r = 0;
	static const long double threshold = 0.0001;
	if((d1-d2) > threshold) {
		r = 1;
	}
	if((d1-d2) < -threshold) {
		r = -1;
	}

	return r;
}

bool is_double_equal(const long double & d1, const long double & d2) {
	if(compare_double(d1, d2) == 0) {
		return true;
	}
	return false;
}

struct point {
	long double x;
	long double y;
	POINT_CONNECTIVITY connectivity;
	side * sides[4];
	block * blocks[4];

	long double get_r();
	long double get_theta();

	void set_pos(const point & p);
	void set_pos(long double px, long double py);
	void set_origin(const point & o);

	point();
	point(long double px, long double py);

	bool has_mirror();
	int count_mirror();
	int count_null();
	int count_mirror_block();

	void calc_connectivity();
};

bool compare_point_by_r(point p1, point p2) {
	return compare_double(p1.get_r(), p2.get_r()) < 0;
}

struct side {
	bool is_mirror;
	SIDE_DIRECTION dir; // 0: horizontal; 1: vertical.
	point * points[2];
	block * blocks[2];

	void setup(point * p1, point * p2, bool ismirror);
	void set_to_mirror();

	side();
	side(point * p1, point * p2);
	side(point * p1, point * p2, bool ismirror);
};

struct block {
	bool is_mirror_block;
	side * sides[4];
	point * points[4];

	void set_to_mirror();
	void setup(point * p1, point * p2, point * p3, point * p4, bool ismirrorblock);
	point get_center();

	block();
	block(point * p1, point * p2, point * p3, point * p4);
};

struct ray {
	point start_point;
	long double theta;
	long double life;
};

struct reflection {
	long double r;
	long double theta;
	bool operator<(const reflection& other) const {
		bool r = compare_double(this->theta, other.theta) < 0;
		return r;
	}
};

struct mirror_room {
	int W, H, D;
	point * points;
	side * sides;
	block * blocks;
	point player_pos;
	vector<ray> rays;
	set<reflection> reflections;

	int get_point_num() {
		return (W - 1) * (H - 1);
	}

	int get_side_num() {
		return 2 * W * H - 3 * (W + H) + 4;
	}

	int get_block_num() {
		return (W - 2) * (H - 2);
	}

	void set_origin();
	void set_player_pos(block * player_block);
	void calc_point_connectivity();

	void read_line(int line_num, char line[]);
	void read();

	void calc_reflection(int rD) {
		D = rD;
		int matrix_size = 2 * rD + 1;
		point * possible_reflections = new point[matrix_size * matrix_size];

		set<long double> possible_theta;

		int init_y = rD;
		for(int i=0; i<matrix_size; i++) {
			int init_x = -rD;
			for(int j=0; j<matrix_size; j++) {
				int serial = i*matrix_size + j;
				possible_reflections[serial].set_pos(init_x, init_y);
				long double r, theta;
				r = possible_reflections[serial].get_r();
				theta = possible_reflections[serial].get_theta();
				if(r <= rD && possible_theta.find(theta) == possible_theta.end()) {
					possible_theta.insert(possible_reflections[serial].get_theta());
					ray r_m;
					r_m.start_point = player_pos;
					r_m.theta = theta;
					r_m.life = rD;
					rays.push_back(r_m);
				}
				init_x ++;
			}
			init_y --;
		}
	}

	void process_ray(ray & r) {
//		cout << "ray: " << r.start_point.x << " " << r.start_point.y << " " << r.theta  << " " << r.life << endl;

		long double t;

//		// Check if cross original point.
//		bool crossed_original = false;
//		if(!is_double_equal(cos(r.theta), 0)) {
//			t = (-r.start_point.y) / cos(r.theta);
//			if (t > 0) {
//				if (is_double_equal(r.start_point.x + t * sin(r.theta), 0)) {
//					// cross original point.
//					crossed_original = true;
//				}
//			}
//		} else {
//			t = (-r.start_point.y) / sin(r.theta);
//			if (t > 0) {
//				if (is_double_equal(r.start_point.y + t * cos(r.theta), 0)) {
//					// cross original point.
//					crossed_original = true;
//				}
//			}
//		}
//
//		if(crossed_original) {
//			double dis_ori = r.start_point.get_r();
//			if(dis_ori <= r.life) {
//				// truly crossed original point before it dies.
//				reflection rfl;
//				rfl.r = D - r.life + dis_ori;
//				rfl.theta = r.start_point.get_theta();
//			}
//		}



		// Reflect on the first mirror it meets.
		// First find out which mirror it hits.
		vector<point> cross_points;
		cross_points.clear();
		for(int i=0; i<get_side_num(); i++) {
			if(!sides[i].is_mirror) {
				continue;
			}
			if(&sides[i] == r.start_point.sides[0]) {
				continue;
			}
			point cross;
			bool crossed = false;
			if (sides[i].dir == HORIZONTAL) {
				if (!is_double_equal(sin(r.theta), 0)) {
					t = (sides[i].points[0]->y - r.start_point.y)
							/ sin(r.theta);
					if (compare_double(t, 0) <= 0) {
						continue;
					}
					cross.x = r.start_point.x + t * cos(r.theta);
					cross.y = sides[i].points[0]->y;
				} else {
					continue;
				}

				if((compare_double(cross.x, sides[i].points[0]->x) >= 0) && (compare_double(cross.x, sides[i].points[1]->x) <= 0)) {
					crossed = true;
				}
			} else {
				if (!is_double_equal(cos(r.theta), 0)) {
					t = (sides[i].points[0]->x - r.start_point.x)
							/ cos(r.theta);
					if (compare_double(t, 0) <= 0) {
						continue;
					}
					cross.x = sides[i].points[0]->x;
					cross.y = r.start_point.y + t * sin(r.theta);
				} else {
					continue;
				}

				if((compare_double(cross.y, sides[i].points[1]->y) >= 0) && (compare_double(cross.y, sides[i].points[0]->y) <= 0)) {
					crossed = true;
				}
			}
			if(crossed) {
				cross.x -= r.start_point.x;
				cross.y -= r.start_point.y;
				cross.sides[0] = &sides[i];
				cross_points.push_back(cross);
			}
		}
		sort(cross_points.begin(), cross_points.end(), compare_point_by_r);

//		cout << "size: " << cross_points.size() << endl;
		side * cross_side = cross_points[0].sides[0];
		long double dis_cross = cross_points[0].get_r();
//		cout << "size: " << cross_points.size() << " " << dis_cross << " " << r.life << endl;

		cross_points[0].x += r.start_point.x;
		cross_points[0].y += r.start_point.y;
		if((is_double_equal(cross_points[0].x, 0) && is_double_equal(r.start_point.x, 0) && compare_double(cross_points[0].y * r.start_point.y, 0) < 0) || (is_double_equal(cross_points[0].y / cross_points[0].x, r.start_point.y / r.start_point.x) && compare_double(cross_points[0].x * r.start_point.x, 0) < 0)) {
			if(compare_double(r.start_point.get_r(), r.life) <= 0) {
//				cout << "start point: " << r.start_point.x << " " << r.start_point.y << endl;
//				cout << "cross point: " << cross_points[0].x << " " << cross_points[0].y << endl;
				// cross original point.
				reflection rfl;
				rfl.r = D - r.life + r.start_point.get_r();
				rfl.theta = r.start_point.get_theta();
				reflections.insert(rfl);
//				cout << "    " << rfl.r << " " << rfl.theta << endl;
			}
		}

		if(compare_double(dis_cross, r.life) >= 0) {
			// r dies.
			r.life = 0;
		} else {
//			cout << "cross point: " << cross_points[0].x << " " << cross_points[0].y << endl;
			r.life -= dis_cross;
//			r.start_point.x += cross_points[0].x;
//			r.start_point.y += cross_points[0].y;

			r.start_point.x = cross_points[0].x;
			r.start_point.y = cross_points[0].y;

			r.start_point.sides[0] = cross_side;

//			cout << "--ray: " << r.start_point.x << " " << r.start_point.y << " " << r.theta  << " " << r.life << endl;
//			cout << "---side i: " << cross_side->points[0]->x << " " << cross_side->points[0]->y << " " << cross_side->points[1]->x  << " " << cross_side->points[1]->y;
			if(cross_side->dir == HORIZONTAL) {
//				cout << " HORIZONTAL";
			}
			if(cross_side->dir == VERTICAL) {
//				cout << " VERTICAL";
			}
//			cout << endl;

			if(is_double_equal(r.start_point.x, cross_side->points[0]->x) && is_double_equal(r.start_point.y, cross_side->points[0]->y)) {
//				cout << "hit side point 0" << endl;
				int mirror_block_index = -1;
				int ray_destroy_index = -1;
				switch(cross_side->points[0]->connectivity) {
				case UNKNOWN:
					cerr << "ERROR!" << endl;
					break;
				case PASS:
					// Do nothing.
					break;
				case PASS_OR_DESTROY:
					for(int i=0; i<4; i++) {
						if(cross_side->points[0]->blocks[i] != NULL && cross_side->points[0]->blocks[i]->is_mirror_block) {
							mirror_block_index = i;
						}
					}
					if(mirror_block_index < 0) {
						cerr << "ERROR!" << endl;
						break;
					}
					// This shouldn't happen if the ray is straight up/down/left/right.
					if(is_double_equal(r.theta, -PI) || is_double_equal(r.theta, -PI / 2) || is_double_equal(r.theta, 0) || is_double_equal(r.theta, PI / 2)) {
						cerr << "ERROR!" << endl;
						break;
					}
					if(compare_double(r.theta, 0) > 0 && compare_double(r.theta, PI / 2) < 0) {
						ray_destroy_index = 0;
					}
					else if(compare_double(r.theta, PI / 2) > 0 && compare_double(r.theta, PI) < 0) {
						ray_destroy_index = 1;
					}
					else if(compare_double(r.theta, -PI) > 0 && compare_double(r.theta, -PI / 2) < 0) {
						ray_destroy_index = 2;
					}
					else if(compare_double(r.theta, -PI / 2) > 0 && compare_double(r.theta, 0) < 0) {
						ray_destroy_index = 3;
					}
					if(ray_destroy_index < 0) {
						cerr << "ERROR!" << endl;
						break;
					}

					if(mirror_block_index == ray_destroy_index) {
						// DESTROY
						r.life = 0;
					} else {
						// PASS
						// Do nothing, keep r.theta the same.
					}
					break;
				case REFLECT:
					if(cross_side->dir == HORIZONTAL) {
						r.theta = -r.theta;
					} else {
						r.theta = PI - r.theta;
					}
					cut_radius_in_range(r.theta);
					break;
				case FULL_REFLECT:
					r.theta = r.theta - PI;
					cut_radius_in_range(r.theta);
					break;
				case DESTROY:
					r.life = 0;
					break;
				}
			} else if (is_double_equal(r.start_point.x, cross_side->points[1]->x) && is_double_equal(r.start_point.y, cross_side->points[1]->y)) {
//				cout << "hit side point 1" << endl;
				int mirror_block_index = -1;
				int ray_destroy_index = -1;
				switch(cross_side->points[1]->connectivity) {
				case UNKNOWN:
					cerr << "ERROR!" << endl;
					break;
				case PASS:
					// Do nothing.
					break;
				case PASS_OR_DESTROY:
					for(int i=0; i<4; i++) {
						if(cross_side->points[1]->blocks[i] != NULL && cross_side->points[1]->blocks[i]->is_mirror_block) {
							mirror_block_index = i;
						}
					}
					if(mirror_block_index < 0) {
						cerr << "ERROR!" << endl;
						break;
					}
					// This shouldn't happen if the ray is straight up/down/left/right.
					if(is_double_equal(r.theta, -PI) || is_double_equal(r.theta, -PI / 2) || is_double_equal(r.theta, 0) || is_double_equal(r.theta, PI / 2)) {
						cerr << "ERROR!" << endl;
						break;
					}
					if(compare_double(r.theta, 0) > 0 && compare_double(r.theta, PI / 2) < 0) {
						ray_destroy_index = 0;
					}
					else if(compare_double(r.theta, PI / 2) > 0 && compare_double(r.theta, PI) < 0) {
						ray_destroy_index = 1;
					}
					else if(compare_double(r.theta, -PI) > 0 && compare_double(r.theta, -PI / 2) < 0) {
						ray_destroy_index = 2;
					}
					else if(compare_double(r.theta, -PI / 2) > 0 && compare_double(r.theta, 0) < 0) {
						ray_destroy_index = 3;
					}
					if(ray_destroy_index < 0) {
						cerr << "ERROR!" << endl;
						break;
					}

					if(mirror_block_index == ray_destroy_index) {
						// DESTROY
						r.life = 0;
					} else {
						// PASS
						// Do nothing, keep r.theta the same.
					}
					break;
				case REFLECT:
					if(cross_side->dir == HORIZONTAL) {
						r.theta = -r.theta;
					} else {
						r.theta = PI - r.theta;
					}
					cut_radius_in_range(r.theta);
					break;
				case FULL_REFLECT:
					r.theta = r.theta - PI;
					cut_radius_in_range(r.theta);
					break;
				case DESTROY:
					r.life = 0;
					break;
				}
			} else {
//				cout << "hit side" << endl;
				if(cross_side->dir == HORIZONTAL) {
					r.theta = -r.theta;
				} else {
					r.theta = PI - r.theta;
				}
				cut_radius_in_range(r.theta);
			}
		}
//		cout << "-----ray: " << r.start_point.x << " " << r.start_point.y << " " << r.theta  << " " << r.life << endl;
	}

	mirror_room(int rW, int rH);
	~mirror_room();
};

static string process(int caseNum) {
	char buf[10240];
	string temp_str = "";
	string result = "";

	int W,H,D;

	cin >> H >> W >> D;

	mirror_room mr(W, H);
	mr.read();
	mr.calc_reflection(D);
	for(int i=0; i<mr.rays.size(); i++) {
		ray r = mr.rays[i];
		while(compare_double(r.life, 0) > 0) {
			mr.process_ray(r);
		}
	}

//	cout << caseNum + 1 << " " << mr.reflections.size() << endl;
//	for(int i=0; i<mr.reflections.size(); i++)
//		cout << "    " << mr.reflections[i].r << " " << mr.reflections[i].theta << endl;

	sprintf(buf, "Case #%d: %d\n", caseNum + 1, mr.reflections.size());
	result.append(buf);
	return result;
}

int main() {
	int caseNum = 0;
	cin >> caseNum;
	cin.ignore(256, '\n');
	char buf[10240];

	string result = "";

	for (int i = 0; i < caseNum; i++) {
		result.append(process(i));
	}
	cout << result;

//	point p;
//	p.x = -3;
//	p.y = 0;
//	cout << p.get_r() << " " << p.get_theta() / (PI) * 180 << endl;
//
//	int a = 1;
//	int b = 3;
//	int * pa;
//	int * pb;
//	pa = &a;
//	pb = &b;
//	swap_pointers((void**)&pa, (void**)&pb);
//	cout << *pa << " " << *pb << endl;

//	mirror_room mr(6,4);
//
//	cout << mr.blocks[6].points[1]->x << " " << mr.sides[6].points[1]->y << endl;

	return 0;
}

// [MIN_RADIUS, MAX_RADIUS)
void cut_radius_in_range(long double & r) {
	while (compare_double(r, MAX_RADIUS) >= 0) {
		r -= PI * 2;
	}
	while (compare_double(r, MIN_RADIUS) < 0) {
		r += PI * 2;
	}
}

void swap_pointers(void * * p1, void * * p2) {
	void * temp;
	temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}

side * get_common_side(point * p1, point * p2) {
	side * result = NULL;
	if(compare_double(p1->x, p2->x) == 0) {
		if(compare_double(p1->y, p2->y) > 0) {
			if(p1->sides[2] == p2->sides[0]) {
				result = p1->sides[2];
			}
		} else if(compare_double(p1->y, p2->y) < 0) {
			if(p1->sides[0] == p2->sides[2]) {
				result = p1->sides[0];
			}
		}
	} else if(compare_double(p1->y, p2->y) == 0) {
		if(compare_double(p1->x, p2->x) > 0) {
			if(p1->sides[1] == p2->sides[3]) {
				result = p1->sides[1];
			}
		} else if(compare_double(p1->x, p2->x) < 0) {
			if(p1->sides[3] == p2->sides[1]) {
				result = p1->sides[3];
			}
		}
	}
	return result;
}

side * get_common_side(block * b1, block * b2) {
	side * result = NULL;

	if(b1->sides[0] == b2->sides[2]) {
		result = b1->sides[0];
	} else if (b1->sides[2] == b2->sides[0]) {
		result = b1->sides[2];
	} else if (b1->sides[1] == b2->sides[3]) {
		result = b1->sides[1];
	} else if (b1->sides[3] == b2->sides[1]) {
		result = b1->sides[3];
	}

	return result;
}


long double point::get_r() {
	return sqrt(x * x + y * y);
}

long double point::get_theta() {
	long double theta;
	if (compare_double(x, 0) == 0 && compare_double(y, 0) == 0) {
		theta = 0;
		return theta;
	}
	if (compare_double(x, 0) == 0 && compare_double(y, 0) > 0) {
		theta = PI / 2;
		return theta;
	}
	if (compare_double(x, 0) == 0 && compare_double(y, 0) < 0) {
		theta = -PI / 2;
		return theta;
	}
	if (compare_double(x, 0) > 0 && compare_double(y, 0) == 0) {
		theta = 0;
		return theta;
	}
	if (compare_double(x, 0) < 0 && compare_double(y, 0) == 0) {
		theta = -PI;
		return theta;
	}
	theta = acos(x / get_r());
	if (compare_double(theta * y, 0) < 0) {
		theta = -theta;
	}
	cut_radius_in_range(theta);
	return theta;
}

void point::set_origin(const point & o) {
	x -= o.x;
	y -= o.y;
}

point::point() {
	x = 0;
	y = 0;
	connectivity = UNKNOWN;

	sides[0] = NULL;
	sides[1] = NULL;
	sides[2] = NULL;
	sides[3] = NULL;

	blocks[0] = NULL;
	blocks[1] = NULL;
	blocks[2] = NULL;
	blocks[3] = NULL;
}

point::point(long double px, long double py) {
	x = px;
	y = py;
	connectivity = UNKNOWN;

	sides[0] = NULL;
	sides[1] = NULL;
	sides[2] = NULL;
	sides[3] = NULL;

	blocks[0] = NULL;
	blocks[1] = NULL;
	blocks[2] = NULL;
	blocks[3] = NULL;
}

void point::set_pos(const point & p) {
	x = p.x;
	y = p.y;
}

void point::set_pos(long double px, long double py) {
	x = px;
	y = py;
}

bool point::has_mirror() {
	for (int i = 0; i < 4; i++) {
		if (sides[i] != NULL && sides[i]->is_mirror) {
			return true;
		}
	}

	return false;
}

int point::count_mirror() {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (sides[i] != NULL && sides[i]->is_mirror) {
			count ++;
		}
	}

	return count;
}

int point::count_null() {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (sides[i] == NULL) {
			count ++;
		}
	}

	return count;
}

int point::count_mirror_block() {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (blocks[i] == NULL || blocks[i]->is_mirror_block) {
			count ++;
		}
	}

	return count;
}

void point::calc_connectivity() {
	int mirror_block_count = count_mirror_block();
	if(mirror_block_count == 0) {
		connectivity = PASS;
	}
	else if(mirror_block_count == 1) {
		connectivity = PASS_OR_DESTROY;
		return;
	}
	else if(mirror_block_count == 2) {
		int b1 = -1;
		int b2 = -1;
		for(int i=0; i<4; i++) {
			if(blocks[i] == NULL || blocks[i]->is_mirror_block) {
				if(b1 == -1) {
					b1 = i;
					continue;
				}
				b2 = i;
			}
		}
		if(b2-b1 == 1 || b2-b1 == 3) {
			connectivity = REFLECT;
		} else {
			connectivity = PASS;
		}
	}
	else if(mirror_block_count == 3) {
		connectivity = FULL_REFLECT;
	}
	else if(mirror_block_count == 4) {
		connectivity = DESTROY;
		return;
	}
}

void side::setup(point * p1, point * p2, bool ismirror) {
	points[0] = p1;
	points[1] = p2;
	is_mirror = ismirror;
	point * temp;
	// always 0 left 1 right, 0 up 1 down.
	if (compare_double(points[0]->x, points[1]->x) == 0) {
		if (compare_double(points[0]->y, points[1]->y) < 0) {
			swap_pointers((void**) &points[0], (void**) &points[1]);
			//			temp = points[0];
			//			points[0] = points[1];
			//			points[1] = temp;
		}
		points[0]->sides[DOWN] = this;
		points[1]->sides[UP] = this;
		dir = VERTICAL;
	}
	if (compare_double(points[0]->y, points[1]->y) == 0) {
		if (compare_double(points[0]->x, points[1]->x) > 0) {
			swap_pointers((void **) &points[0], (void **) &points[1]);
			//			temp = points[0];
			//			points[0] = points[1];
			//			points[1] = temp;
		}
		points[0]->sides[RIGHT] = this;
		points[1]->sides[LEFT] = this;
		dir = HORIZONTAL;
	}
}

void side::set_to_mirror() {
	is_mirror = true;
}

side::side() {
	is_mirror = false;

	points[0] = NULL;
	points[1] = NULL;

	blocks[0] = NULL;
	blocks[1] = NULL;
}

side::side(point * p1, point * p2) {
	blocks[0] = NULL;
	blocks[1] = NULL;

	setup(p1, p2, false);
}

side::side(point * p1, point * p2, bool ismirror) {
	blocks[0] = NULL;
	blocks[1] = NULL;

	setup(p1, p2, ismirror);
}

void block::set_to_mirror() {
	is_mirror_block = true;
	sides[0]->set_to_mirror();
	sides[1]->set_to_mirror();
	sides[2]->set_to_mirror();
	sides[3]->set_to_mirror();
}

void block::setup(point * p1, point * p2, point * p3, point * p4, bool ismirrorblock) {
	is_mirror_block = false;
	points[0] = p1;
	points[1] = p2;
	points[2] = p3;
	points[3] = p4;

	// should be upright, upleft, downleft, downright.
	if (compare_double(points[0]->y, points[3]->y) < 0) {
		swap_pointers((void**) &points[0], (void**) &points[3]);
	}
	if (compare_double(points[1]->y, points[2]->y) < 0) {
		swap_pointers((void**) &points[1], (void**) &points[2]);
	}
	if (compare_double(points[0]->x, points[1]->x) < 0) {
		swap_pointers((void**) &points[0], (void**) &points[1]);
	}
	if (compare_double(points[3]->x, points[2]->x) < 0) {
		swap_pointers((void**) &points[3], (void**) &points[2]);
	}

	points[0]->blocks[2] = this;
	points[1]->blocks[3] = this;
	points[2]->blocks[0] = this;
	points[3]->blocks[1] = this;

	sides[0] = get_common_side(points[0], points[1]);
	sides[0]->blocks[1] = this;
	sides[1] = get_common_side(points[1], points[2]);
	sides[1]->blocks[1] = this;
	sides[2] = get_common_side(points[2], points[3]);
	sides[2]->blocks[0] = this;
	sides[3] = get_common_side(points[3], points[0]);
	sides[3]->blocks[0] = this;

	if(is_mirror_block) {
		set_to_mirror();
	}
}

point block::get_center() {
	point p;
	for(int i=0; i<4; i++) {
		p.x += points[i]->x;
		p.y += points[i]->y;
	}
	p.x /= 4;
	p.y /= 4;

	return p;
}

//void block::setup(side * s1, side * s2, side * s3, side * s4);
//
block::block() {
	is_mirror_block = false;
	for(int i=0; i<4; i++) {
		sides[i] = NULL;
		points[i] = NULL;
	}
}

block::block(point * p1, point * p2, point * p3, point * p4) {
	setup(p1, p2, p3, p4, false);
}

//block::block(side * s1, side * s2, side * s3, side * s4);

void mirror_room::set_origin() {
	if (compare_double(player_pos.x, 0) == 0 && compare_double(player_pos.y, 0) == 0) {
		return;
	}
	for (int i = 0; i < get_point_num(); i++) {
		points[i].set_origin(player_pos);
	}
	player_pos.x = 0;
	player_pos.y = 0;
}

void mirror_room::set_player_pos(block * player_block) {
	player_pos = player_block->get_center();
	set_origin();
}

void mirror_room::calc_point_connectivity() {
	for(int i=0; i<get_point_num(); i++) {
		points[i].calc_connectivity();
	}
}

void mirror_room::read_line(int line_num, char line[]) {
	if(line_num == 0 || line_num == H-1) {
		return;
	}
//	cout << line << endl;
	int y = line_num - 1;
	for(int x=0;x<W-2;x++) {
		if(line[x + 1] == 'x' || line[x + 1] == 'X') {
			set_player_pos(&blocks[y*(W-2) + x]);
		} else if(line[x + 1] == '#') {
			blocks[y*(W-2) + x].set_to_mirror();
		}
	}
}

void mirror_room::read() {
	char buf[256];
	cin.ignore(256, '\n');
	for(int i=0;i<H;i++) {
		cin.getline(buf, 256);
		read_line(i, buf);
	}

	for(int i=0; i< W-2; i++) {
		sides[i].set_to_mirror();
		sides[(H-2) * (W-2) + i].set_to_mirror();
	}
	for(int i=0; i< H-2; i++) {
		sides[(H-1)*(W-2) + i * (W-1)].set_to_mirror();
		sides[(H-1)*(W-2) + i * (W-1) + W - 2].set_to_mirror();
	}
	calc_point_connectivity();

//	for(int i=0; i<H-1; i++) {
//		for(int j=0; j<W-2; j++) {
//			if(sides[i*(W-2)+j].is_mirror)
//				cout << "M";
//			else
//				cout << "O";
//		}
//		cout << endl;
//	}
//	for(int i=0; i<H-2; i++) {
//		for(int j=0; j<W-1; j++) {
//			if(sides[(H-1)*(W-2) + i*(W-1)+j].is_mirror)
//				cout << "M";
//			else
//				cout << "O";
//		}
//		cout << endl;
//	}
}

mirror_room::mirror_room(int rW, int rH) {
	W = rW;
	H = rH;

	points = new point[get_point_num()];
	for(int i=0; i<H-1; i++) {
		for(int j=0; j<W-1; j++) {
			points[i*(W-1)+j].set_pos(j, -i);
		}
	}

	sides = new side[get_side_num()];
	// HORIZONTAL sides.
	for(int i=0; i<H-1; i++) {
		for(int j=0; j<W-2; j++) {
			sides[i*(W-2)+j].setup(&points[i*(W-1) + j], &points[i*(W-1) + j + 1], false);
		}
	}
	// VERTICAL sides.
	for(int i=0; i<H-2; i++) {
		for(int j=0; j<W-1; j++) {
			sides[(W-2)*(H-1) + i*(W-1)+j].setup(&points[i*(W-1) + j], &points[(i+1)*(W-1) + j], false);
		}
	}

	blocks = new block[get_block_num()];
	for(int i=0; i<H-2; i++) {
		for(int j=0; j<W-2; j++) {
			blocks[i*(W-2)+j].setup(&points[i*(W-1) + j], &points[i*(W-1) + j + 1], &points[(i+1)*(W-1) + j], &points[(i+1)*(W-1) + j + 1], false);
		}
	}

	rays.clear();
}

mirror_room::~mirror_room() {
	delete [] blocks;
	delete [] sides;
	delete [] points;
}
