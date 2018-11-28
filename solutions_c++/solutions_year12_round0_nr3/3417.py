#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
//#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
//const double PI = 2 * acos(0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int I, J;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

int N;
int n;

std::string toString(int i) {
 std::ostringstream buffer;
 buffer << i;
 return buffer.str();
}

int main() {

	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	
	cin >> N;
	string s1;
	getline(cin,s1);
	rep2(nn,1,N+1) {
		int counter = 0;
		int a, b;
		cin >> a >> b;

		string history;
		string already;

		int check = 0;

		for(int j = a ; j <= b ; j++)
		{
			// slice to back
			string now;
			now.append(toString(j));
			
			for(int k = 0 ; k < now.length() ; k++)
			{
				string changed = now.substr(k,string::npos)+now.substr(0,k);
			
				if(changed[0] == '0') continue;
				// 바꿨을때 원래 수랑 같으면 pass - 필요없음.

				//cout << "now : " << now << " changed : " << changed << endl;
				
				if(history.find(changed)!=string::npos) {
					//cout << " I found same!!! " << endl;

					counter++;

					//already.append(changed);
					//already.append("|");
				}
				//cout << endl ;
			}
			history.append(toString(j));
			history.append("|");
		/*
			string now;
			int k = j;
			int at[10] = {0,};
			while(1)
			{
				at[k%10]++;
				if(k < 10) break;
				k /= 10;
			}
			for(int k = 0 ; k < 10 ; k++)
				now.append(toString(at[k])); // now

			if(history.find(now)!=string::npos) { // in history - pair
				if(already.find(now)==string::npos) { // not counted
					counter++;
					cout << j << "c ";
					already.append(now);
					already.append("|");
				}
				else { check++; // pair but aleady counted
				cout << j << "a ";
				}
			}
			else{ // first - not pair
				cout << j << "n ";
				history.append(now);
				history.append("|");
			}
		*/
		}
		printf("Case #%d: ", nn);
		cout << counter << endl;//" " << check << endl;
	}
	return 0;
}
