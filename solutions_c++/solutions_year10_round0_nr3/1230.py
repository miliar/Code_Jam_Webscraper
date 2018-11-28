#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <time.h>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <stack>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()a
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define FOR(n,a,b) for(n=a;n<b;n++)
#define RFOR(n,b,a) for(n=b;n>=a;n--)
#define fo(i,j) for(int i=0;i<j;i++)


long GoRound(long K,long N );

int head,tail;
double  total;
long q[1000];

int main()
{

    FILE *in=fopen("a.in","r");
    FILE *out=fopen("a.out","w");
    int i,j,y=1,T;
	
	

	fscanf(in,"%d",&T);
    while(T--)
    {

 		long R;
		long K;
		int N;

		fscanf(in,"%d",&R);
		fscanf(in,"%d",&K);
		fscanf(in,"%d",&N);
		
		fo(i,N)
			fscanf(in,"%d",&q[i]);
		head=0;
		tail=N-1;

		total=0;
		while(R--)
		{
			total+=GoRound(K,N);
		}
	
		fprintf(out,"Case #%d: %.0f\n",y,total);
		printf("Case #%d: %.0f\n",y,total);
		y++;
	}
	
	//getchar();
     return 0;
}

long GoRound(long K,long N )
{
	long c=0;
	long gc=0;
	int i=0;
	while(true)
	{
		if(N==c)
			return gc;

		gc+= q[(head +i)%N];
		if(gc==K)
		{
			head= (head +i+1)%N;
			tail= (tail +i+1)%N;
			return gc;
		}
		else if(gc>K)
		{
			gc-= q[(head +i)%N];
			head= (head +i)%N;
			tail= (tail +i)%N;
			return gc;
			
		}
		i=(i++)%N;
		c++;

	}
	//printf("error");
	return gc;
	
}
