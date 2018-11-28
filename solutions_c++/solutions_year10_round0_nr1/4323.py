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

 	int T,N,K;
 	int P[11];
#define SMALL
//#define LARGE
int main(int argc, char *argv[])
{
//	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt2.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
 	cin>>T;
 	int n=1;
 	while(n<=T)
 	{
	 		  cin>>N;
	 		  cin>>K;
	 		  for(int i=0;i<N;i++)
	 		    P[i]=0;
	 		  while(K>0)
			   {
			   	for(int i=0;i<N;i++)
				   {if(P[i]==0){P[i]=1;goto OUT;}
				   else P[i]=0;
				   }	
				   OUT:	
			   	  K--;		
			   			} 
				int flag=1;		    
			  for(int i=0;i<N;i++)
			    if(P[i]!=1)	flag=0;
				if(flag==1)cout<<"Case #"<<n<<": ON"<<endl;
				else cout<<"Case #"<<n<<": OFF"<<endl;
			n++;	
		  }
    return EXIT_SUCCESS;
}
