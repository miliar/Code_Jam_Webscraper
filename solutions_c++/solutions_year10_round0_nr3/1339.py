#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;


int main()
	{
	 	  int T,R,K,N,p,f,sum,pro=0,x=1;
	 	  for(cin>>T;T>0;T--)
	 	  {
				  cin>>R>>K>>N;
				  vector<int> v(N);
				  for(int i=0;i<N;i++) cin>>v[i];
				  pro=p=f=0;
				  for(int i=0;i<R;i++)
				  {
				   		  
				   		  sum=0;
				   		  for(int j=0;j<N;j++)
				   		  {
						   		  if(sum+v[(p+j)%N]>K){ p=(p+j+N)%N;break;}
			   					  sum+=v[(p+j)%N];
    				      } 
    				      //if(sum<=K) { cout<<sum*R<<endl;break;}
   				          pro+=sum;
				  }
				  cout<<"Case #"<<x++<<": "<<pro<<endl;
          }
 }
