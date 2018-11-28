#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// typedefs
typedef vector<int> VI;
typedef vector<string> VS;

// defines
#define SWAP(x,y) (x)^=(y)^=(x)^=(y)
#define MAX(a,b)   (a)>(b)?(a):(b)
#define MIN(a,b)   (a)<(b)?(a):(b)
#define ABS(a) ((a)>0?(a):-(a))
#define STOI(s,d) istringstream(s)>>d
#define ITOS(d,s) {ostringstream t;t<<d;s=t.str();}
#define REP(i,n) for(int i=0;i<n;i++)
#define REPS(i,s) REP(i,s.length())
#define REPV(i,v) REP(i,v.size())
#define SZ(x) x.size()


// common
int GCD(int a,int b){for(int c;b;c=a,a=b,b=c%b);return a;}
int LCM(int a,int b){return a/GCD(a,b)*b;}

// parsing
template <class T>
vector<basic_string<T> > parse(const basic_string<T> &s,const basic_string<T> &delim){
  vector<basic_string<T> > ret(0);
  for (int b,e=0;;ret.push_back(s.substr(b,e-b)))
    if ((b=s.find_first_not_of(delim,e))==(e=s.find_first_of(delim,b)))
      return ret;
}
VI intparse(const string &s,const string &delim=" \t\n"){
  VS tmp=parse(s,delim);
  VI ret(0);
  for (VS::iterator i=tmp.begin();i!=tmp.end();i++)
    {int t;STOI(*i,t);ret.push_back(t);}
  return ret;
}

//=========================== TTime
class TTime {
public:
	TTime() {hh=mm=0;}
	TTime(string t);
	int TimeDiff(TTime end);
	int hh, mm;
	void addMin(int m);
	string toString() const;
	int getValue() const;
};

int TTime::getValue() const {
    return hh*60+mm;
}

void TTime::addMin(int m) {
	mm += m;
	hh += (mm / 60);
	mm %= 60;
}

string TTime::toString() const {
	ostringstream ss;
	ss << hh << ":" << mm;
	return ss.str();
}

TTime::TTime(string t) {
	//t.replace(2, 1, " ");
	t[2] = ' ';
	istringstream ss(t);
	ss >> hh >> mm;
}

//============================ TTrip
class TTrip {
public:
	TTrip(string trip, char from, char to);
	TTime dep, arr;
	string toString() const;
	int getDuration();
	char from, to;
	bool used;
};

bool operator<(const TTrip &a, const TTrip &b) {
     int v1 = a.dep.getValue();
     int v2 = b.dep.getValue();
     if (v1 == v2) {
         v1 = a.arr.getValue();
         v2 = b.arr.getValue();
     }
     return (v1 < v2);
}

int TTrip::getDuration() {
	if (arr.mm < dep.mm) {
		arr.hh--;
		arr.mm += 60;
	}
	int m = arr.mm - dep.mm;
	int c = arr.hh - dep.hh;
	return 60*c+m;
}

string TTrip::toString() const {
	ostringstream ss;
	ss << dep.toString() << " - " << arr.toString();
	return ss.str();
}

TTrip::TTrip(string trip, char a, char b) {
	from = a;
	to = b;
	string t1, t2;
	istringstream ss(trip);
	ss >> t1 >> t2;
	dep = TTime(t1);
	arr = TTime(t2);
	used = false;
}

//============================
vector <TTrip> tt;

void dfs1(int i) {
	return;
}

//============================ my code
int main() {
	cout << "CJC 2008 Qualification Round: Train Timetable" << endl;
	ifstream in("B-large.in", ios::in);  // declare and open
	ofstream out("b-large.out", ios::out);
	int N, NA, NB, T;
	if (in.is_open())
  	{
		//test cases
		string line;
  		getline (in, line);
  		STOI(line, N);
  		//printf("Number of cases: %d\n", N);
  		
		for(int i=0; i<N; ++i) {
			//turnaround time (in minutes)
	  		getline (in, line);
	  		STOI(line, T);
	  		
			//trips NA and NB on a line
	  		getline (in, line);
  			istringstream ss(line);
			ss >> NA >> NB;
			
			int att[NA][NB];

			memset(att, 0, sizeof(att));
	  		int na=0, nb=0;
	  		
			//A to B
			for(int j=0; j<NA; ++j) {
		  		getline (in, line);
		  		tt.push_back(TTrip(line, 'A', 'B'));
			}

			//B to A
			for(int j=NA; j<NA+NB; ++j) {
		  		getline (in, line);
		  		tt.push_back(TTrip(line, 'B', 'A'));
			}
	  		sort(tt.begin(), tt.end());
			
			/*
			REP(j, NA+NB) {
				printf("Trip from %c to %c %s takes %d minutes.\n", 
                             tt[j].from, tt[j].to,  tt[j].toString().c_str(), tt[j].getDuration());
			}
			*/

			//printf("Case: %d, there are %d search engines\n", i+1, SZ(engines));
			//work
			while (true) {
                  bool loop = false;
                  REPV(i, tt) {
						TTrip *t1 = &tt[i], *t2 = &tt[i];
						TTrip *start = t1;
						if (!t1->used) {
							//cout << "Starting trip:" << t1->toString() << endl;
							loop = true;
							start = t1;
							REPV(j, tt) {
								t2 = &tt[j];
								if (t2->used || t1->to != t2->from) continue;
								if (t1->arr.getValue() + T > t2->dep.getValue()) continue;
								//ok
								//cout << "via trip:" << t2->toString() << endl;
								t2->used = true;
								cout << t1->used << t2->used << endl;
								t1 = t2;
							}
							if (start->from == 'A') na++;
							if (start->from == 'B') nb++;
							start->used = true;
						}
                  }
                  if (!loop) break;
            }
		
			//output
     		out << "Case #" << (i+1) << ": " << na << " " << nb << endl;
     		cout << "Case #" << (i+1) << ": " << na << " " << nb << endl;
		}
		
    	in.close();
	}
	
	out.close();
	cin.get();
	return 0;
}
