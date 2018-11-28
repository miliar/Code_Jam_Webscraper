/*
Author : Prem Kumar
language : C++
*/
#include<iostream>
using namespace std;

int main()
{
    int T,R,K,N;

    cin>>T;
    int ind = 0;
    while(ind<T){	
	    cin>>R>>K>>N;
	    
	    int g[N];
	    
	    
	    for(int i=0;i<N;i++){
		    cin>>g[i];
		    }
	    
	    int i,j;
	    i=0;
	    j=0;
	    int sum = 0;
	    int cost = 0;
	    while(R!=0){
		    j=i;
		    sum = 0;
		    sum+= g[i];
		    while((sum+g[(j+1)%N]<=K) && i!=(j+1)%N){
		         sum = sum + g[(j+1)%N];
		         j=j+1;                                   
		    }
		    cost= cost + sum;
		    i = (j+1)%N;
		    R--;
	    }
	    
	    cout<<"Case #"<< ++ind<<": "<<cost<<endl;
	
          }
    
    return 0;
    }
