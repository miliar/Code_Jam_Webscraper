#include <iostream>
#include <map>

using namespace std;

bool exists_and_remove(multimap<int,int> &timetable, int time);
void read_timetable(int nof, multimap<int,int> &timetable);
int delay_time(int time, int delay);

int main() {
	string noinp;
	cin >> noinp;

	// Az inputok szamaszor megcsinalja amit kell...
	for (int i=0; i < atoi(noinp.c_str()); ++i) {
		int delay;
		string str;
		cin >> str;
		delay = atoi(str.c_str());
		int na, nb;
		cin >> str;
		na = atoi(str.c_str());
		cin >> str;
		nb = atoi(str.c_str());
		multimap<int,int> trains_from_a;
		multimap<int,int> trains_from_b;
		read_timetable(na,trains_from_a);
		read_timetable(nb,trains_from_b);

		//Jon a lenyeg:
		int notfa = trains_from_a.size();
		int notfb = trains_from_b.size();

		multimap<int,int> b_changeable = trains_from_b;
		for (multimap<int,int>::iterator it = trains_from_a.begin(); it != trains_from_a.end(); ++it) {
			if (b_changeable.size() == 0) {
				break;
			}
			if (exists_and_remove( b_changeable, delay_time( (*it).second, delay ) )) {
				--notfb;
			}
		}

		multimap<int,int> a_changeable = trains_from_a;
		for (multimap<int,int>::iterator it = trains_from_b.begin(); it != trains_from_b.end(); ++it) {
			if (a_changeable.size() == 0) {
				break;
			}
			if (exists_and_remove( a_changeable, delay_time( (*it).second, delay ) )) {
				--notfa;
			}
		}

		//Kiiratjuk az eredmenyt:
		cout << "Case #" << i+1 << ": " << notfa << " " << notfb << endl;

		/*
		//Kiiratja, hogy jo-e a beolvasas
		cout << delay << endl;
		for (map<int,int>::iterator it = trains_from_a.begin(); it != trains_from_a.end(); ++it) {
			cout << (*it).first << "__--__" << (*it).second << endl;
		}
		for (map<int,int>::iterator it = trains_from_b.begin(); it != trains_from_b.end(); ++it) {
			cout << (*it).first << "__--__" << (*it).second << endl;
		}
		*/
	}
	return 0;
}

bool exists_and_remove(multimap<int,int> &timetable, int time) {
	for (multimap<int,int>::iterator it = timetable.begin(); it != timetable.end(); ++it) {
		if ( (*it).first >= time ) {
			timetable.erase(it);
			return true;
		}
	}
	return false;
}

int delay_time(int time, int delay) {
	int h = time / 100;
	int m = time % 100;
	m += delay;
	h += m / 60;
	m  = m % 60;
	return (h*100)+m;
}

void read_timetable(int nof, multimap<int,int> &timetable) {
	for (int i = 0; i < nof; ++i) {
		string str;
		cin >> str;
		int dep_h = atoi((str.substr(0,2)).c_str());
		int dep_m = atoi((str.substr(3,2)).c_str());
		int dep = (dep_h*100) + dep_m;
		cin >> str;
		int arr_h = atoi((str.substr(0,2)).c_str());
		int arr_m = atoi((str.substr(3,2)).c_str());
		int arr = (arr_h*100) + arr_m;
		timetable.insert(pair<int,int>(dep,arr));
	}
}

