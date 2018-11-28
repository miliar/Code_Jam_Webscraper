#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
long long data[1100];
int main()
{
 	FILE *fin=fopen("A.in","r");
 	FILE *fout=fopen("A.out","w");
	
	int R,K,N,T;
	fscanf(fin,"%d",&T);
	for(int ll=1;ll<=T;ll++)
	{
	 	fprintf(fout,"Case #%d: ",ll);	
		fscanf(fin,"%d%d%d",&R,&K,&N);
		for(int i=0;i<N;i++)
		{
		   fscanf(fin,"%d",&data[i]); 		
	    }	 
	    int ans=0;
	    int i=1;
	    int j=-1;
	    while(i<=R)
	    {
		      int temp=0;
		      int start=-10;
			  while(temp+data[(j+1)%N]<=K)
			  {
			       j=(j+1)%N;
				   if(temp==0)
				   {
				      start=j;			  
				   }
				   if((j==start)&&temp)
				   {
				   	  break;		   				  
			       } 
				   temp+=data[j];
		      }  		   
			  i++;
			  ans+=temp;		
		}
		fprintf(fout,"%d\n",ans);
    }
    return 0;
}


