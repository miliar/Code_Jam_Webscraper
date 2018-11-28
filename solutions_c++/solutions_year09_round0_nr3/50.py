#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cmath>

using namespace std;

#define RP(i,j,k) for(int i=j; i<k; ++i)
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define pB push_back
#define P(a) cout << #a << " : " << a << endl;
#define M make_pair

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<","; return o;}

typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;

const string W="welcome to code jam";
const int mod=10000;

int main()
{
	int C;
	cin >> C;
	string p;
	getline(cin,p);
	
	for(int cs=1; cs<=C; ++cs)
	{
		string ln;
		getline(cin,ln);
		
		int ct[20];
		memset(ct,0,sizeof(ct));
		ct[0]=1;
		R(i,ln)
		{
			RP(j,0,19)
			{
				if(ln[i]==W[j])
				{
					ct[j+1]+=ct[j];
					ct[j+1]%=mod;
				}
			}
		}
		
		cout << "Case #" << cs << ": ";
		int r=ct[19];
		if(r<10) cout << "000"; else if (r<100) cout << "00"; else if(r<1000) cout << "0";
		cout << r;
		cout << endl;
	}
	
	return 0;
}