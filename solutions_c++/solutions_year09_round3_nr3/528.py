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
#include <queue>
#include <fstream>

using namespace std;
int main()
{
  int p,q,nn,cas=0;
  cin>>nn;
  while(nn--)
  {cas++;
  cin>>p>>q;
  bool pr[p+1];
  memset(pr,true,sizeof(pr));
  
  int ans=0,j=0,i,k,c,tmp;
  int a[q];
  for(i=0;i<q;i++)cin>>a[i];
  bool fg=true;
  do
  {
      memset(pr,true,sizeof(pr));
      tmp=0;
      for(j=0;j<q;j++)
	  {
         k=a[j];
		 pr[k]=false;
		 c=k-1;
		 while(c>=1&&pr[c]){tmp++;c--;}c=k+1;
		 while(c<=p&&pr[c]){tmp++;c++;}
	  }
	  if(fg){ans=tmp;fg=false;}
	  else	  
	  ans=min(tmp,ans);
  }while(next_permutation(a,a+q));
  cout<<"Case #"<<cas<<": ";
  cout<<ans<<endl;
  }
}