#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<climits>

using namespace std;

#define FOR(i,N) for(int i=0; i<(N); ++i)


bool P[200];

int coins(int,int);

int main()
  {
    int T,p,Q,max;
    
    cin>>T;
    
    int C[200];
    
    FOR(i,T)
      {
	cin>>p>>Q;
	
	FOR(j,Q) cin>>C[j];

	
	
	sort(C,C+Q);
	
	max=INT_MAX;
	
	do
	  {
	    
	    FOR(j,p) P[j]=true;
	    
	    int m=0;
	    FOR(j,Q)
	      {
		m+=coins(C[j],p);
		P[C[j]-1]=false;
	      }
	    if(m<max) max=m;
	    
	  }
	while(next_permutation(C,C+Q));
	
	
	
	cout<<"Case #"<<i+1<<": "<<max<<'\n';

      }
    
    
    return(0);
  }

int coins(int p, int N)
  {
    int a=p-1;
    int c=0;
    while(a>=0 && P[a]==true) c++,a--;
    a=p-1;
    while(a<N && P[a]==true) c++, a++;
    return(c-2);   
  }
