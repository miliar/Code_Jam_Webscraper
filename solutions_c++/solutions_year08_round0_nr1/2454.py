#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int main()
{
   int N,S,Q,max,swich,count,i,j,k,l,m;
   int zero;
   
   string prev;
   char a[1022];
   string engine[1000];
   string queries[10000];
   max=swich=0;
   cin>>N;
   	for(i=0;i<N;i++)
   	{
   		map<string,int> dic;
   	        max=0;swich=0;
   		scanf("%d",&S);
   		getchar();
   		for(j=0;j<S;j++)
   		{
   			getline(cin,engine[j]);
//			cin>>engine[j];
   			//cout<<engine[j]<<endl;
   			dic[engine[j]]=1;
   			//cout<<dic[engine[j]]<<endl;
   			
   		}
   		cin>>Q;
   		zero=0;
   		getchar();
   		for(j=0;j<Q;j++)
   		{
   			getline(cin,queries[j]);
   			
   			if(dic[queries[j]]!=0&&zero!=S-1)
   			{
   			  dic[queries[j]]=0;
   			  zero++;
   			 // cout<<zero<<"\t"<<j<<"\n";
   			}
   			/*if(zero==N-1)
   			{
   				for(k=0;k<S;k++)
   				    if(dic[engine[k]]!=0)
   				        prev=engine[k];
			Yeehaw 1
			Yeehaw1
			Googol2
			B93
			Googol3
			NSM4
			B94
			NSM4
			Dont Ask1
			Googol2
			}*/
			if(zero==S-1&&dic[queries[j]]!=0)
			{
				swich++;
				dic[queries[j]]=0;
				for(k=0;k<S;k++)
				  if(engine[k]!=queries[j])
				    dic[engine[k]]=1;
 		               zero=1;
 		               prev="\0";
			}
   		//	cout<<swich<<"\n";
   		}
   		cout<<"Case #"<<i+1<<": "<<swich<<"\n";
//   		if(i!=N-1)
 //  		cout<<"\n";
   	}
   
}
