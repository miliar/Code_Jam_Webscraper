#include <iostream>
#include <stdio.h>
#include <queue>
#include <vector>
#include <set>
#include <memory.h>

using namespace std;

#define FOR(i,b) for (int i = 0; i < (b); i++)
#define MP(A,B) make_pair(A,B)

char ch[200][200];
int N;

long long games[200];
long long win[200];
long long loose[200];

double wp[200];
double op[200];
double opw[200];
double rpi[200];


int main()
{
	int T;
	
	scanf("%d",&T);
	
	FOR(t,T)
	{
		scanf("%d",&N);
		
		FOR(n,N)
		{
			scanf("%s",ch[n]);
		}
		
		for(int y=0;y<N;y++)
		{
			games[y]=win[y]=loose[y]=0;
			
			for(int x=0;x<N;x++)
			{
				if(ch[y][x]=='1')
				{
					win[y]++;
					games[y]++;
				}
				else if(ch[y][x]=='0')
				{
					games[y]++;
					loose[y]++;
				}
			}
			
			wp[y]=win[y]/(1.0*games[y]);
		}
		
		
		for(int y=0;y<N;y++)
		{
			op[y]=0;
			int counter= 0;
			
			for(int x=0;x<N;x++)
			{
				if(ch[y][x]=='1')
				{
					op[y]+=(win[x])/(1.0*(games[x]-1));
					counter++;
				}
				else if(ch[y][x]=='0')
				{
					op[y]+=(win[x]-1)/(1.0*(games[x]-1));
					counter++;
				}
			}
			
			op[y]=op[y]/counter;
		}
		
		for(int y=0;y<N;y++)
		{
			opw[y]=0;
			
			int counter=0;
			
			for(int x=0;x<N;x++)
			{
				if(ch[y][x]=='1')
				{
					opw[y]+=op[x];
					counter++;
				}
				else if(ch[y][x]=='0')
				{
					opw[y]+=op[x];
					counter++;
				}
			}
			
			opw[y]=opw[y]/counter;;
		}
		
		printf("Case #%d:\n",t+1);
		
		for(int n=0;n<N;n++)
		{
			rpi[n] =  0.25 * wp[n] + 0.50 * op[n] + 0.25 * opw[n];
			printf("%.8lf\n",rpi[n]);
		}
	}
}