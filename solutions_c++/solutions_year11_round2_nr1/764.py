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

char arr[105][105];
int M[105];
int W[105];
double OWP[105],OOWP[105],RPI[105];

int main()
{
    freopen ("A.in","r",stdin);
    freopen ("A.out","w",stdout);
    
    int i,j,k=0,T;
    
    scanf("%d",&T);
    
    while(T--)
    {
		k++;
		
		clr(M,0);
		clr(W,0);
		fo(i,102)OWP[i]=0,OOWP[i]=0,RPI[i]=0;
		
		int N;
		scanf("%d",&N);
		fo(i,N)
			scanf("%s",arr[i]);
		
		fo(i,N)
		{
			fo(j,N)
			{
				if(arr[i][j]!='.')
				{
					M[i]++;
					if(arr[i][j]=='1')W[i]++;
				}
			}
		}
		
		fo(i,N)
		{
			int X=0;
			fo(j,N)
			{
				if(j==i)continue;
				if(arr[j][i]!='.')
				{
					X++;
					int g=0,h=0;
					g=W[j];
					if(arr[j][i]=='1')g--;
					h=M[j];
					if(arr[j][i]!='.')h--;
					OWP[i]+=double(g)/double(h);
				}
			}
			OWP[i]/=X;
		}
		fo(i,N)
		{
			int X=0;
			fo(j,N)
			{
				if(j==i)continue;
				if(arr[j][i]!='.')
				{
					X++;
					OOWP[i]+=OWP[j];
				}
			}
			OOWP[i]/=X;
			RPI[i]=0.25*(double)W[i]/(double)M[i] + 0.5*OWP[i] + 0.25*OOWP[i];
			//printf("%lf %lf %lf\n",(double)W[i]/(double)M[i], OWP[i], OOWP[i]);
		}
		printf("Case #%d:\n",k);
		fo(i,N)printf("%lf\n",RPI[i]);
	}
    
}


































