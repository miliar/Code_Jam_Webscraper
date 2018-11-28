#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

const double pi = 3.14159265358979323846264;

bool outside(double x, double y, double radius) {
	return (x*x + y*y > radius*radius);
}

bool rect_inside(double bottom, double left, double width, double height, double radius) {
	return ((bottom+height)*(bottom+height) + (left+width)*(left+width)) < radius*radius;
}

void print_6(double val) {
	fprintf(stderr, "%.6f\n", val);
}

int main(int argc, char** argv) {
	ifstream infile(argv[1]);

	int num_cases;
	infile >> num_cases;
	
	for(int i = 0; i < num_cases; i++) {
		cout << "Case #" << i+1 << ": ";
		double f, R, t, r, g;
		infile >> f >> R >> t >> r >> g;
		cerr << "f: ";
		print_6(f);
		cerr << "R: ";
		print_6(R);
		cerr << "t: ";
		print_6(t);
		cerr << "r: ";
		print_6(r);
		cerr << "g: ";
		print_6(g);

		if(f >= g/2)  {
			cout << 1 << endl;
			continue;
		}

		// the radius of the circle inside of which the fly must be
		// to have non-zero chance of avoiding the ring
		double real_inner = R - t - f;
		double real_inner_sq = real_inner*real_inner;
		cerr << "real_inner: ";
		print_6(real_inner);

		double bottom_left_x = r + f;
		double bottom_left_y = r + f;
		cerr << "bottom_left_x,y: ";
		print_6(bottom_left_x);

		double bottom_left_dist = 2*r + g;
		cerr << "bottom_left_dist: ";
		print_6(bottom_left_dist);

		//double height = g - 2*r - 2*f;
		double height = g - 2*f;
		double width = height;
		cerr << "height,width: ";
		print_6(height);

		double bottom = bottom_left_y;
		double left = bottom_left_x;

		double area = 0;

		while(!outside(left, bottom_left_y, real_inner)) {
			//cerr << "left: " << left << endl;
			bottom = bottom_left_y;
			while(!outside(left, bottom, real_inner)) {
				//cerr << "bottom: " << bottom << endl;
				// square is completely inside
				if(rect_inside(bottom,left,width,height,real_inner)) {
					//cerr << "inside" << endl;
					area += width*height;
				} else if(outside(bottom, left, real_inner)) {
				} else {
					// find the two intersection points
					double top = bottom + height;
					double right = left + width;

					double int1_x, int1_y, int2_x, int2_y;

					// find left/top point
					if(!outside(left, top, real_inner)) {
						// it intersects in the top
						int1_y = top;
						int1_x = sqrt(real_inner_sq - top*top);
					} else {
						// it intersects in the left
						int1_x = left;
						int1_y = sqrt(real_inner_sq - left*left);
					}

					// find right/bottom point
					if(!outside(right, bottom, real_inner)) {
						// it intersects in the right
						int2_x = right;
						int2_y = sqrt(real_inner_sq - right*right);
					} else {
						// it intersects in the bottom
						int2_y = bottom;
						int2_x = sqrt(real_inner_sq - bottom*bottom);
					}

					// add area from non circle segment
					area += (int1_x - left)*(int2_y - bottom);
					area += (int1_x - left)*(top - int2_y);
					area += (right - int1_x)*(int2_y - bottom);
					area += (int2_x - int1_x)*(int1_y - int2_y)/2;

					// add are from circle segment
					double mag1 = sqrt(int1_x*int1_x + int1_y*int1_y);
					int1_x /= mag1;
					int1_y /= mag1;

					double mag2 = sqrt(int2_x*int2_x + int2_y*int2_y);
					int2_x /= mag2;
					int2_y /= mag2;

					double theta = acos(int1_x*int2_x + int1_y*int2_y);

					area += real_inner_sq*(theta - sin(theta))/2;
				}

				bottom += bottom_left_dist;
			}

			left += bottom_left_dist;
		}

		double total_area = pi * R*R;
		printf("%.6f\n", 1-4*area/total_area);
		cerr << 1 - 4 * area / total_area << endl;
	}

	return 0;
}
