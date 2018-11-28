#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <string>
#include <sstream>

using namespace std;

typedef multimap< int, int > mmapint;
typedef pair< int, int > pairint;
typedef vector< int > vecint;

pairint parse_time(string str)
{
	pairint t;
	istringstream iss(str);
	int hour, min;

	iss>>setw(2)>>hour;
	iss.ignore();
	iss>>setw(2)>>min;
	t.first = hour * 60 + min;

	iss.ignore();

	iss>>setw(2)>>hour;
	iss.ignore();
	iss>>setw(2)>>min;
	t.second = hour * 60 + min;

	return t;
}

pairint calculate(mmapint a, mmapint b, int turnaround)
{
	vecint av, bv;
	pairint trains, ready;
	for(int i = 0; i < 3600; i++) {
		mmapint::iterator mp;
		vecint::iterator vp;

		while((vp = find(av.begin(), av.end(), i)) != av.end()) {
			// cout<<"["<<i<<"->A] "<<endl;
			ready.first++;
			av.erase(vp);
		}

		while((mp = a.find(i)) != a.end()) {
			// cout<<"[A->"<<i<<"] "<<endl;
			if(!ready.first) {
				trains.first++;
			} else {
				ready.first--;
			}
			bv.push_back(mp->second + turnaround);
			a.erase(mp);
		}

		while((vp = find(bv.begin(), bv.end(), i)) != bv.end()) {
			// cout<<"["<<i<<"->B] "<<endl;
			ready.second++;
			bv.erase(vp);
		}

		while((mp = b.find(i)) != b.end()) {
			// cout<<"[B->"<<i<<"] "<<endl;
			if(!ready.second) {
				trains.second++;
			} else {
				ready.second--;
			}
			av.push_back(mp->second + turnaround);
			b.erase(mp);
		}
	}

	return trains;
}

int main(int argc, char *argv[])
{
	string dummy;
	int ncases;
	cin>>ncases;
	getline(cin, dummy);

	for(int i = 0; i < ncases; i++) {
		string str;
		int turnaround;
		cin>>turnaround;

		int na, nb;
		cin>>na>>nb;
		getline(cin, str);

		mmapint a, b;

		for(int j = 0; j < na; j++) {
			getline(cin, str);
			a.insert(parse_time(str));
		}

		for(int j = 0; j < nb; j++) {
			getline(cin, str);
			b.insert(parse_time(str));
		}

		pairint r = calculate(a, b, turnaround);
		cout<<"Case #"<<i + 1<<": "<<r.first<<" "<<r.second<<endl;
	}

	return 0;
}

