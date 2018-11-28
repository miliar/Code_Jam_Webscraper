#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <utility>
#include <sstream>
#include <cstring>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

#define RP(i,s,e) for(int i=s;i<e;i++) 
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin();i!=(x).end();++i)
#define M make_pair
#define pB push_back
#define _1 first
#define _2 second
#define foreach(t,i) RI(i,t)
#define CLEAR(x,v) memset((x),(v),sizeof((x))
#define PRINT(o,b) RI(i,b) o << *i << (--b.end()==i ? "" : " ");
#define PE(s,e) cout << #s << " : "; for(typeof(s) i=s; i!=e; ++i) cout << (*i) << " "; cout << endl;

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<" "; return o;}

//Cake please.

int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};

int w, h;
char lal;

int gog(int x, int y, int *al, char *la)
{
	if (la[y*w+x] != 0) return la[y*w+x];
	
	int min = al[y*w+x] - 1;
	int mind = -1;
	RP(i, 0, 4)
	{
		if (x + dx[i] >= 0 && x + dx[i] < w && y + dy[i] >= 0 && y + dy[i] < h)
		{
			if (al[(y + dy[i]) * w + x + dx[i]] <= min)
			{
				mind = i;
				min = al[(y + dy[i]) * w + x + dx[i]];
			}
		}
	}
	
	if (mind == -1)
	{
		//A sink
		la[y * w + x] = lal;
		++lal;
		return la[y * w + x];
	}
	
	int t = gog(x + dx[mind], y + dy[mind], al, la);
	la[y * w + x] = t;
	return t;
}

int main()
{
	int t;
	cin >> t;
	
	RP(cs, 1, t+1)
	{
		cin >> h >> w;
		
		int al[h * w];
		RP(i, 0, h * w)
			cin >> al[i];

		char la[h * w];
		memset(la, 0, h * w * sizeof(char));
		lal = 'a';
		
		
//		RP(i, 0, h)
//		{
//			RP(j, 0, w)
//			{
//				cout << la[i * w + j] << " ";
//			}
//			cout << endl;
//		}
//		
//		cout << "---" << endl;		
		
		RP(y, 0, h)
		{
			RP(x, 0, w)
			{
				gog(x, y, (int*)al, (char*)la);
			}
		}
				
//		RP(i, 0, h)
//		{
//			RP(j, 0, w)
//			{
//				cout << al[i * h + j] << " ";
//			}
//			cout << endl;
//		}
//		
//		cout << "---" << endl;		
		
		cout << "Case #" << cs << ":" << endl;
		RP(i, 0, h)
		{
			RP(j, 0, w)
			{
				cout << la[i * w + j] << " ";
			}
			cout << endl;
		}
	}
	
	return 0;
}