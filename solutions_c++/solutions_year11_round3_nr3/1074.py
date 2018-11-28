#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <cmath>

using namespace std;
int gcd(int a,int b);
int lcm(int a,int b);

int main(){
	ifstream in;
	ofstream out;
	
	in.open("C-small-attempt0.in");
	out.open("output.txt");

	int T;
	in>>T;

	for(int u=0;u<T;u++){
		int N,L,H;
		in>>N>>L>>H;

		int fre[100];

		for(int i=0;i<N;i++){
			int temp;
			in>>temp;
			fre[i]=temp;
		}

		/*int gcdV=fre[0];
		int lcmV=fre[0];

		for(int i=1;i<N;i++){
			gcdV=gcd(gcdV,fre[i]);
			lcmV=lcm(lcmV,fre[i]);
		}

		cout<<gcdV<<" gcd"<<endl;
		cout<<lcm<<" gcd"<<endl;*/

		int ans=-1;

		for(int i=L;i<=H;i++){
			int stat=0;
			for(int j=0;j<N;j++){
				if(fre[j]%i==0||i%fre[j]==0){
				}
				else{
					stat=1;
					break;
				}
			}
			if(stat==0){
				ans=i;
				break;
			}
		}

		if(ans==-1){
			out<<"Case #"<<(u+1)<<": NO"<<endl;
		}
		else{
			out<<"Case #"<<(u+1)<<": "<<ans<<endl;
		}

		cout<<u<<endl;

	}


	in.close();
	out.close();

	

	return 0;
}

int lcm(int a,int b)
  {
    int n;
    for(n=1;;n++)
    {
  	if(n%a == 0 && n%b == 0)
  	  return n;
    }
  }

int gcd(int a,int b)
  {
    int c;
    while(1)
    {
  	c = a%b;
  	if(c==0)
  	  return b;
  	a = b;
  	b = c;
    }
  }

