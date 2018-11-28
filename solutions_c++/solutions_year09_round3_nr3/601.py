#include<iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
const int MAXIMUM = 105; 
int arr[MAXIMUM];

vector<int> v;

int T,P,Q,D;


int COST(int p)
{
 	int valu = 0;
 	arr[p] = -1;
	 for(int i=p-1;i>0 ;--i)
  	{
		   if(arr[i]==-1)
		   break;
		   valu++;
  	} 
 for(int i=p+1;i<=P;++i)
  {
  	 if(arr[i]==-1)
  	  break;
 	  valu++;
  } 
 
 return (valu);  
}


int main()
 {
  scanf("%d",&T);
  int i;
  for(int cases=1;cases<=T;cases++)
   {
   
   	 scanf("%d%d",&P,&Q);
  	  v.clear();
    
	for(i=1;i<=Q;i++)
     	{
      		scanf("%d",&D);
      		v.push_back(D); 
     	} 
   	 sort(v.begin(),v.end());
  	  int cost = 123456789,temp=0;
    	do
    	{
     	arr[0]=-1;  
     	for(i=1;i<=P;i++)
      	arr[i]=0;
     	arr[P+1]=-1; 
     	temp = 0;
     	
     	for(int j=0;j<Q;j++)
      	temp += COST(v[j]);
     	if(temp < cost)
       	{
       	cost = temp;
     	}
    	}
    while(next_permutation(v.begin(),v.end())); 
     
    printf("Case #%d: %d\n",cases,cost);
   }
 }
