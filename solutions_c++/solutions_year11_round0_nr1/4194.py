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

char c[105][5];
int x[105];
int OGT[105],BGT[105];

int main()
{
    freopen ("A.in","r",stdin);
    freopen ("A.out","w",stdout);
    
    int i,j,k=0,T,ret=0;
    
    scanf("%d",&T);
    
    int A,B,f1=0,f2=0,last1,last2;
    
    while(T--)
	{
		k++;
		f1=0,f2=0;
		ret=0;
		memset(OGT,-1,sizeof(OGT));
		memset(BGT,-1,sizeof(BGT));
		
		int N;
		scanf("%d",&N);
		fo(i,N)
		{
			scanf("%s %d",c[i],&x[i]);
			if(c[i][0]=='O')
			{
				if(!f1)
				{
					A=i;
					last1=i;
					f1=1;
				}
				else
				{
					OGT[last1]=i;
					last1=i;
				}
			}
			if(c[i][0]=='B')
			{
				if(!f2)
				{
					B=i;
					last2=i;
					f2=1;
				}
				else
				{
					BGT[last2]=i;;
					last2=i;
				}
			}
		}
		
		
		
		int ind1=1,ind2=1;
    
		while(1)
		{
			int AA=A,BB=B;
			bool f=0;
			//printf("\n%d: %d %d %d %d\n",ret,A,B,ind1,ind2);
			if(A==-1 && B==-1)break;
			if(A!=-1)
			{
				if(x[A]<ind1)ind1--,f=1;
				else if(x[A]>ind1)
				{
					ind1++,f=1;
				}
				else if(x[A]==ind1)
				{
					if(A<B || B==-1)
					{//printf("%d %d done1\n",ind1,ind2);
						A=OGT[A],f=1;
					}
				}
			}
			if(B!=-1)
			{
				if(x[B]<ind2)ind2--,f=1;
				else if(x[B]>ind2)
				{
					ind2++;f=1;
				}
				else
				{
					if(B<AA || AA==-1)
					{//printf("%d %d done2\n",ind1,ind2);
						B=BGT[B],f=1;
					}
				}
			}
			if(!f)break;
			ret++;
		}
		printf("Case #%d: %d\n",k,ret);
	}
}


































