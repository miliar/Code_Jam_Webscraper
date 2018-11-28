#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define FR(i,n) for(int i=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int i=c;(i)<(n);(i)++)
#define CLR(a,c) memset(a,c,sizeof(a));
typedef pair<int,int> PII;
typedef long long ll;
int num[2000010]={0};
bool visited[2000010]={false};
int ten[10]={1};
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int a,b;
	int t;cin>>t;
	FOR(i,1,10) num[i]=1;
	FOR(i,10,100) num[i]=2;
	FOR(i,100,1000) num[i]=3;
	FOR(i,1000,10000) num[i]=4;
	FOR(i,10000,100000) num[i]=5;
	FOR(i,100000,1000000) num[i]=6;
	FOR(i,1000000,2000010) num[i]=7;
	ten[1]=1;FOR(i,2,10) ten[i]=ten[i-1]*10;
	FR(cas,t)
	{
		printf("Case #%d: ",cas+1);
		cin>>a>>b;
		ll sum=0;
		CLR(visited,false);
		FOR(i,a,b+1)
		{
			int n=i;
			int val=ten[num[i]];
			vector<int> v;v.clear();
			v.push_back(i);
			visited[i]=true;
			FR(j,num[i]-1)
			{
				int t=n%10;n/=10;n+=(t*ten[num[i]]);
				if(n<i && n>=a && n<=b && num[n]==num[i] && !visited[n]) 
				{
					sum++;
					visited[n]=true;
					v.push_back(n);
				}
			}
			FR(i,v.size()) visited[v[i]]=false;
		}
		cout<<sum<<endl;
	}
}