/*
ID: harrymw1
LANG: C++
TASK: 
*/
 
#include <iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include <cstdio>
#include<map>
#include<stack>
#include<set>
#include<queue>
#include<cctype>
#include<assert.h>
#include<numeric>
#include<ctime>
#include<iterator>
//#include<sstream>
using namespace std;

#define PI acos(-1.0)
#define fore(i,a) for(int i=0; i<(a); i++)
#define forv(i,a) for(typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define all(x) x.begin(),x.end()
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
/*template<class T> string toString(T n){
	ostringstream ost;ost<<n;ost.flush();
	return ost.str();
}*/

//__builtin_popcount(int x);
int main()
{
	freopen("A.in.txt", "r", stdin);
	freopen("A.out.txt", "w", stdout);
	//clock_t start, finish;
   	//double duration;
   	//start = clock();
	int t,ca=1;
	cin>>t;
	while(t--){
		int n,m;scanf("%d%d",&n,&m);
		set<string> ss,v;string s;
		for(int i=0; i<n;i++){cin>>s;ss.insert(s);}
		int ret=0;
		for(int j=0;j <m;j++){cin>>s;
			if(ss.count(s))continue;
			ss.insert(s);++ret;
			for(int i=s.size()-1;i>=0;i--){
				if(i&&s[i]=='/'){
					string ts=s.substr(0,i);
					if(ss.count(ts)){break;}
					ss.insert(ts);
					++ret;
				}
			}
			/*for(int i=s.size()-1;i>=0;i--){
				if(i&&s[i]=='/'){
					string ts=s.substr(0,i);
					ss.insert(ts);
				}
			}*/
		}
		printf("Case #%d: %d\n",ca++,ret);

	}


	//finish = clock();
   	//duration = (double)(finish - start) / CLOCKS_PER_SEC;
	//printf( "%f seconds\n", duration );
	return 0;
}
