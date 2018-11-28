//
// /home/xenosoz/work/gcj/2009/B_Watersheds
//
#include <iostream>
#include <vector>
#include <tr1/unordered_map>
#include <tr1/functional>
#include <map>
#include <cassert>

using namespace std;
using namespace std::tr1;

struct point
{
	int row, col;
	point()
		: row(0), col(0) {
	}
	point(const int &_row, const int &_col)
		: row(_row), col(_col) {
	}
	bool operator < (const point& rhs) const {
		const point& lhs = *this;
		if(lhs.row != rhs.row) { return lhs.row < rhs.row; }
		if(lhs.col != rhs.col) { return lhs.col < rhs.col; }
		return false;
	}
	bool operator == (const point& rhs) const {
		const point& lhs = *this;
		return (lhs.row == rhs.row && lhs.col == rhs.col);
	}
	bool operator != (const point& rhs) const {
		const point& lhs = *this;
		return (!(lhs == rhs));
	}
	point north() const {
		return point(row - 1, col);
	}
	point west() const {
		return point(row, col - 1);
	}
	point east() const {
		return point(row, col + 1);
	}
	point south() const {
		return point(row + 1, col);
	}
};

template<int ROW, int COL>
struct point_hash : public unary_function<point, size_t>
{
	size_t operator()(const point& v) const {
		return v.row * ROW + v.col * COL;
	}
};


namespace std {
	namespace tr1 {
		template<> struct hash<point> : point_hash<1000, 1> {};
	}
}

struct cell_type;
typedef unordered_map<point, cell_type> world_type;


struct cell_type
{
	point id;
	int altitude;

	mutable point parent_id;

	cell_type(const point& _id, const point& _parent_id, const int& _altitude)
		: id(_id), parent_id(_parent_id), altitude(_altitude) {
	}
	bool operator==(const cell_type& rhs) const {
		const cell_type &lhs = *this;
		if(lhs.id != rhs.id) { return false; }
		return true;
	}
	void normalize(const world_type &world) const {
		typedef	vector<const cell_type *> trace_type;
		trace_type trace;

		const cell_type* p = this;
		while((*p).id != (*p).parent_id) {
			world_type::const_iterator f = world.find((*p).parent_id);
			assert(f != world.end());
			trace.push_back(p);
			p = &(*f).second;
		}
		for(trace_type::iterator i = trace.begin(); i != trace.end(); ++i) {
			trace_type::value_type &c = *i;
			(*c).parent_id = (*p).id;
		}
	}
	void make_flow_to(const point &target_id, const world_type &world) {
		parent_id = target_id;
		normalize(world);
	}
};

typedef vector<cell_type> cell_vector;


struct cell_lexical_ordering
{
	bool operator()(const cell_type &lhs, const cell_type &rhs) {
		//if(lhs.altitude != rhs.altitude) { return lhs.altitude < rhs.altitude; }
		if(lhs.id != rhs.id) { return lhs.id < rhs.id; }
		return false;
	}
};

struct cell_lower_ordering
{
	bool operator()(const cell_type &lhs, const cell_type &rhs) {
		if(lhs.altitude != rhs.altitude) { return lhs.altitude < rhs.altitude; }
		//if(lhs.id != rhs.id) { return lhs.id < rhs.id; }
		return false;
	}
};



void cell_link_flow(cell_type& cell, const world_type& world, cell_vector& sinks)
{
	vector<cell_type> where_to;
	{
		where_to.push_back(cell);
		world_type::const_iterator f;
		if(world.end() != (f = world.find(cell.id.north()))) { where_to.push_back((*f).second); }
		if(world.end() != (f = world.find(cell.id.west()))) { where_to.push_back((*f).second); }
		if(world.end() != (f = world.find(cell.id.east()))) { where_to.push_back((*f).second); }
		if(world.end() != (f = world.find(cell.id.south()))) { where_to.push_back((*f).second); }
		stable_sort(where_to.begin(), where_to.end(), cell_lower_ordering());
	}
	assert(!where_to.empty() && "unexpected end of cell");
	cell_type& here = cell;
	cell_type& there = where_to[0];

	if(there.id == here.id) {
		sinks.push_back(cell);
		return;
	}

	here.make_flow_to(there.id, world);
}

int main(void)
{
	int N = 0;
	if(!(cin >> N)) {
		assert(false && "unexpected end of file");
		return -1;
	}
	for(int i = 0; i < N; ++i) {
		int H = 0;
		int W = 0;
		if(!(cin >> H >> W)) {
			assert(false && "unexpected end of file");
			return -1;
		}

		world_type world;
		cell_vector sinks;

		// input
		for(int row = 0; row < H; ++row) {
			for(int col = 0; col < W; ++col) {
				int alt;
				if(!(cin >> alt)) {
					assert(false && "unexpected end of file");
					return -1;
				}
				point id(row, col);
				cell_type t(id, id, alt);
				world.insert(make_pair<point, cell_type>(id, t));
			}
		}

		// update link flow
		for(world_type::iterator j = world.begin(); j != world.end(); ++j) {
			world_type::value_type &c = *j;
			const point &id = c.first;
			cell_type &cell = c.second;
			cell_link_flow(cell, world, sinks);
		}

		// namebind decl
		typedef map<point, char> namebind_type;
		namebind_type namebind;
		char name_acc = 'a';

		// output
		cout << "Case #" << (i+1) << ":\n";
		for(int row = 0; row < H; ++row) {
			for(int col = 0; col < W; ++col) {
				world_type::iterator f = world.find(point(row, col));
				assert(f != world.end());
				const point &id = (*f).first;
				cell_type &cell = (*f).second;

				//
				cell.normalize(world);

				namebind_type::iterator b = namebind.find(cell.parent_id);
				if(b == namebind.end()) {
					pair<namebind_type::iterator, bool> r = namebind.insert(make_pair<point, char>(cell.parent_id, ' '));
					assert(r.second);
					b = r.first;
				}
				char& name = (*b).second;
				if(' ' == name) {
					name = name_acc;
					++name_acc;
				}

				if(col) { cout << ' '; }
				cout << name;
			}
			cout << '\n';
		}
	}

	world_type world;
	return 0;
}
