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

int main()
{
	int C;
	cin >> C;
	for(int cs=1; cs<=C; ++cs)
	{
		int c,d,n;
		string f;
		map<string,char> m;
		set<string> r;
		
		cin >> c;
		RP(i,0,c){
			cin >> f;
			string a;
			a+=f[0];
			a+=f[1];
			char b=f[2];
			m[a]=b;
			swap(a[0],a[1]);
			m[a]=b;
		}
		
		cin >> d;
		RP(i,0,d){
			cin >> f;
			r.insert( ""+f);
			swap(f[0],f[1]);
			r.insert( ""+f);
		}
		
		string res;
		
		cin >> n;
		
		for(int i=0; i<n; ++i){
			char t;
			cin >> t;
			
			string e="  ";
			
			if(res.length()>0){
				e[0]=res[res.size()-1];
				e[1]=t;
				if(m.count(e)){
					res[res.size()-1]=m[e];
					t=m[e];
				}
				else res=res+t;
			}
			else res=res+t;
			
			
			e[0]=t;
			for(int i=0; i<res.size(); ++i)
				if(e[1]=res[i], r.count(e))
					res="";
			
		}
		
		cout << "Case #" << cs << ": [";
		
		for(int i=0; i<res.size(); ++i)
			cout << res[i] << (i<res.size()-1?", ":"");
		
		cout << "]" << endl;
	}
	
	return 0;
}