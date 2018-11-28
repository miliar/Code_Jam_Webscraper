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



int main()
{

    FILE *in=fopen("a.in","r");
    FILE *out=fopen("a.out","w");
    int i,j,y=1,T;
	fscanf(in,"%d",&T);
    while(T--)
    {

        int n;
		long K;
		fscanf(in,"%d",&n);
		fscanf(in,"%d",&K);

		
		long r=pow((double)2,(double)n);
		long a = r-1;
	
		

		if((K%r)==a)
			//printf("Case #%d: ON\n",y);
			fprintf(out,"Case #%d: ON\n",y);
		else
			//printf("Case #%d: OFF\n",y);
			fprintf(out,"Case #%d: OFF\n",y);
			
		
		
		y++;
	}
	
	
     return 0;
}
