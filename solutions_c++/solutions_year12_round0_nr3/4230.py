#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <ctime>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000
#define maxn 1000000

//typedef long long  LL;
//typedef __int64 LL;
typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;


short f[9999999];

int main()
{
	int i,j,k,tests,cs=0,n,cnt=0;

	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		int a,b;
		scanf("%d%d",&a,&b);

		int ans=0;
		for(i=a;i<=b;i++)
		{
			char num[10];
			sprintf(num,"%d",i);
			int l=strlen(num);
			cnt++;
			for(j=0;j<l;j++)
			{
				int v=0;
			
				for(k=0;k<l;k++)
					v=v*10+(num[(j+k)%l]-'0');
				
				if(v>i && v<=b && f[v]!=cnt) ans++;
				f[v]=cnt;
			}
		}
		printf("Case #%d: %d\n",++cs,ans);
	}




	return 0;
} 


