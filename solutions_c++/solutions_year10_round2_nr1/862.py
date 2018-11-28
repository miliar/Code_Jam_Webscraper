#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<sstream>
#include<map>
#include<utility>

#define S(n) scanf("%d",&n)


#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)
#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>

#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000

#define CLR(var,val) memset(var,val,sizeof((var)))
#define S(n) scanf("%d",&n)
#define LL unsigned long long
#define LD long double
#define triple pair<int, pair<int,int> >
#define OFF 0
#define MAX(a,b) (a>b?a:b)

using namespace std;


int main()
{
	//freopen("inp.in", "r", stdin);
	int T;
	S(T);
	int c = 0;
	while(T--)
	{
		c++;
		int N, M; cin >> N >> M;
		map<string, bool> mp;
		int i;
		REP(i,N)
		{
			string s;
			cin >> s;
			mp[s] = true;
		}
		mp["/"] = true;
		
		int create = 0;
		REP(i,M)
		{
			string s;
			cin >> s;
			//cout << s << " tbd " << endl;
			
			vector<int> slash_pos;
			int j;
			REP(j, s.SZ) if(s[j] == '/') slash_pos.PB(j);
			slash_pos.PB(s.SZ-1);
			
			j = slash_pos.SZ - 1; 
			while(mp.find(s) == mp.end())
			{
				create++;
				mp[s] = true;
				//cout << s << " ";
				j--;
				s = s.substr(0, slash_pos[j]);
				//cout << s << " " << create << endl;
				if(s == "") break;
			}
			
		}
		cout << "Case #" << c << ": " << create << endl;
	}
	return 0;
}
