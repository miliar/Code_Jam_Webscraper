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

 	int T,R,k,N;
 	int P;
 	
#define SMALL
//#define LARGE
int main(int argc, char *argv[])
{
//	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
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
              queue<int> que;
	 		  cin>>R; 
	 		  cin>>k;
	 		  cin>>N;
	 		  for(int i=0;i<N;i++)
	 		    {cin>>P;que.push(P);}
	 		  int c=0;  
	 		  int ret=0;
		      while(R>0)
		      {
			   			for(int i=0;i<N;i++)
			   			 if(c+que.front()<=k){c+=que.front();que.push(que.front());que.pop();}
			   			 else break;
			   			 ret+=c;
			   			 c=0;
			   			R--;}
   			cout<<"Case #"<<n<<": "<<ret<<endl;
			n++;	
		  }
    return EXIT_SUCCESS;
}
