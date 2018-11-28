#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
  int i,j,k,l,m,n,o,T;
  int C,A,N,M,x,y;
  cin>>C;
  for(i=1;i<=C;i++)
  {
	cin>>N;cin>>M;cin>>A;
	o=0;
	for(j=0;j<=N;j++){
		for(k=0;k<=M;k++){
			for(m=0;m<=N;m++){
				for(n=0;n<=M;n++)
					if(abs((m-j)*(0-k)-(0-j)*(n-k))==A){
						o=1;
						break;
					}
				if(o)break;
			}
				if(o)break;
		}
				if(o)break;
	}
	if(o) cout<<"Case #"<<i<<": 0 0 "<<j<<" "<<k<<" "<<m<<" "<<n<<endl;
	else  cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
  }

  return 0;
}
