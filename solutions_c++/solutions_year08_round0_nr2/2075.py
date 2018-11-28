#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

using namespace std;

struct train_store {
	int r, d;
	train_store() : r(0), d(0) {}
};

typedef map<int, train_store> map_t;
typedef pair<map_t, map_t> pair_t;
typedef vector<pair_t> vec_t;

bool read_data(const char *filename, vec_t &v)
{
	ifstream in(filename);

	//read problem specific data into structure
	int N;
	in >> N;

	while (N-- > 0) {
		int T, NA, NB;
		in >> T >> NA >> NB;

		int h, m;
		char colon;
		pair_t tp;

		//do A
		while (NA-- > 0) {
			//get the depart time
			in >> h >> colon >> m;
			m = (60 * h) + m;
			tp.first[m].d += 1;
			
			//get the arrival time
			in >> h >> colon >> m;
			m = (60 * h) + m + T;
			tp.second[m].r += 1;
		}
		//do B
		while (NB-- > 0) {
			//get the depart time
			in >> h >> colon >> m;
			m = (60 * h) + m;
			tp.second[m].d += 1;
			
			//get the arrival time
			in >> h >> colon >> m;
			m = (60 * h) + m + T;
			tp.first[m].r += 1;
		}

		v.push_back(tp);
	}

	in.close();
}

//reduce he he
int reduce(const map_t &m) {
	train_store ts;
	for (map_t::const_iterator i(m.begin()), e(m.end()); i != e; ++i) {
		ts.r += i->second.r;
		int d = i->second.d;
		while (d-- > 0) {
			if (ts.r > 0) --ts.r;
			else ++ts.d;
		}
		//cout << i->first << " => r-" << i->second.r << " d-" << i->second.d << endl;
	}
	return ts.d;
}


int main(int argc, char* argv[])
{
	//make sure we have an argument
	if (argc == 1) {
		cout << "Usage: " << argv[0] << " <filename>" << endl;
		return 1;
	}

	vec_t v;
	//read the data
	read_data(argv[1], v);	


	//solve problem
	int count = 0;
	for (vec_t::const_iterator i(v.begin()), e(v.end()); i != e; ++i) {
		cout << "Case #" << ++count << ": " << reduce(i->first) << " " << reduce(i->second) << endl;
	}


	return 0;
}

