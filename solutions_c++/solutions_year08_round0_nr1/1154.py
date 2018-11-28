#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <numeric>

using namespace std;

#define v vector <int>
#define vs vector <string>
#define vv vector< v >
#define forz(i,n) for(int i=0;i<n;i++)
#define fl(i,s,n) for(int i=s;i<n;i++)
#define lh(i) int(i.length())
#define sz(i) (int)(i.size())
#define pb(a) push_back(a)
#define all(a) a.begin(),a.end()

int fin(v alp)
{
	forz(i,sz(alp))if(alp[i]==999999999)return 1;
return 0;
}
int main()
{
	int n,ai=0;
	cin>>n;
	while(n--)
	{
		int s;
		cin>>s;
		char c;
		vs eng,que;
		char str[101];
		map<string,int>mm;
		forz(i,s){c=getchar();scanf("%[^\n]",str);string pp(str);eng.pb(pp);mm[pp]=i;}
		int q;
		cin>>q;
		forz(i,q){c=getchar();scanf("%[^\n]",str);string pp(str);que.pb(pp);}
		int cnt=0;
		v alp(s,999999999);
		v hi=alp;
		forz(i,sz(que))
		{
			if(alp[mm[que[i]]]==999999999)alp[mm[que[i]]]=i;		
			if(fin(alp))continue;
			else
			{
				cnt++;
				alp=hi;
				i--;
			}
		}
		cout<<"Case #"<<++ai<<": "<<cnt<<endl;
		
	}
return 0;
}

