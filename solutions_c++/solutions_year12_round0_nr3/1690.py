#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cassert>
#include<ctime>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>


#define PB push_back
#define M 100
#define N 500010
#define MOD 1000000007
#define MAX 18450000
#define MAX 18450000
//#define NMAX 101
//#define SRT 11
#define SRT 4300
#define LL long long
#define LLMAX 0x7fffffffffffffffLL

using namespace std;
int  main()
{
	int tc,ti,i,j,k,cnt,len,a,b;
	string s1,s2;
	char str[100];
	scanf("%d",&tc);
	for(ti=1;ti<=tc;++ti)
	{
		scanf("%d %d",&a,&b);
		cnt=0;
		set < pair <int,int > > s;
		for(i=a;i<=b;++i)
		{
			len=0;
			k=i;
			while(k>0)
			{
				k/=10;
				++len;
			}
			sprintf(str,"%d%d",i,i);
			for(j=len;j>0;--j)
			{
				if(str[j]=='0')
				continue;
				str[j+len]=0;
				k=atoi(str+j);
				if(k>i && k>=a && k <=b)
				{
				//printf("%d %d\n",i,k);
				s.insert(make_pair(i,k));
				
				}
			}
			
		}
		printf("Case #%d: %d\n",ti,s.size());
		//sort(v.begin(),v.end());
		//for(i=0;i<v.size();++i)
		//printf("%d %d\n",v[i].first,v[i].second);
	}
	return 0;
}