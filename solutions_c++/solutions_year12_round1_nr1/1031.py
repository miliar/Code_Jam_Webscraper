#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

double p[100002];

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	
	int T,k=0;
	
	scanf("%d",&T);
	
	while(T--)
	{
		k++;
		double A,B;
		double P=1,ret;
		scanf("%lf %lf",&A,&B);
		for(int i=0;i<(int)A;i++)
		{
			scanf("%lf",&p[i]);
			P*=p[i];
		}
		ret=min(P*(B-A+1)+(1-P)*(A+1+B+1), (1+B+1));
		for(int i=1;i<=A;i++)
		{
			P/=p[(int)A-i];
			ret=min(ret,i+P*(B-(A-i)+1)+(1-P)*(B-(A-i)+1+B+1));
			//printf("%lf %lf %lf %lf\n",i+P*(B-(A-i)+1)+(1-P)*(1-P)*(B-(A-i)+1+B+1),P,(B-(A-i)+1),(B-(A-i)+1+B+1));
		}
		printf("Case #%d: %lf\n",k,ret);
	}
}



































