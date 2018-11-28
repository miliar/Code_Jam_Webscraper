/*
Author : Prem Kumar
language : C++
*/
#include<iostream>
using namespace std;

int main()
{
    unsigned int T,R,K,N;

    cin>>T;
    unsigned int ind = 0;
    while(ind<T){	
	    cin>>R>>K>>N;
	    
	    unsigned int g[N];
	    int next[N];
	    unsigned int val[N];
	    
	    
	    for(int i=0;i<N;i++){
		    cin>>g[i];
		    val[i]=-1;
		    next[i]=-1;	
		    }
	    
	    int i,j;
	    i=0;
	    j=0;
	    unsigned int sum = 0;
	    unsigned int cost = 0;
	    while(R!=0){
		    
		    if(next[i]!=-1){
			cost = cost + val[i];
			i=next[i];
		    }
		    
		    else{
			    j=i;
			    sum = 0;
			    sum+= g[i];
			    while((sum+g[(j+1)%N]<=K) && i!=(j+1)%N){
				 sum = sum + g[(j+1)%N];
				 j=j+1;                                   
			    }
			    cost= cost + sum;
			    val[i]=sum;
			    next[i] = (j+1)%N;
			    i=next[i];	
			    

		    }
		    R--;
	    }
	    cout<<"Case #"<< ++ind<<": "<<cost<<endl;
	
          }
    
    return 0;
    }
