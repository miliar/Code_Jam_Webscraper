#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <queue>
#include <stdio.h>
using namespace std;

#define rep(i,m) for( i=0;i<m;i++)
#define rep2(i,x,m) for(i=x;i<m;i++)
#define T_Max  50
void toggle(int&x);

int main ()
{
int i,j,k;//counters
//int oo,x;
int h;//temp
int R[T_Max],K[T_Max],N[T_Max];
queue <int> G[50];
int a;      
                 freopen("C-small-attempt1.in","rt",stdin);    
                 freopen("C-small-attempt1.out","wt",stdout);    
      
                 int T;//test cases number    
                 cin>>T;    
    
                     rep(i,T)    
                     {  cin>>R[i]>>K[i]>>N[i];  
					    rep(j,N[i])
						{   cin>>a;
					        G[i].push(a);
						}
					 }
    
			/*
			Testing
			        rep(i,T)    
                     {  cout<<R[i]<<" "<<K[i]<<" "<<N[i]<<endl;  
					     rep(j,N[i])
						{   cout<<G[i].front()<<" ";
					        G[i].pop();
						}
						 cout<<endl;
					 }
					   
			*/

int Sub;
int earn;

rep(i,T)  

{   earn=0;
	rep(k,R[i])
	{ earn+=K[i];
	  Sub=K[i];
	  rep(j,N[i])
	  {
		
		h=G[i].front();
		Sub-=h;
		if(Sub>=0)
			{G[i].pop();
			 G[i].push(h);
			 
			 //Num_Gps++;
			}
		
			
	     else 
		 Sub+=h;;
		}
	 
earn-=Sub;

	/*
	Test
	  rep(oo,N[i]) {x=G[i].front();cout<<x<<" "; G[i].pop(); G[i].push(x);}
	  cout<<endl;
      
	  cout<<earn<<endl;
	*/

	}

cout<<"Case #"<<i+1<<": "<<earn<<endl;
}












 


  return 0;    
}    
    

