#include<vector>
#include<iostream>
#include<algorithm>
#include<numeric>
#include<limits>
using namespace std;
void process();
int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		cout<<"Case #"<<i<<": ";
		process();
	}
}
long long gcd(long long a,long long b)
  {
   long long c;
    while(1)
    {
  	c = a%b;
  	if(c==0)
  	  return b;
  	a = b;
  	b = c;
    }
  }

void process() {
	long long n,l,h;
	cin>>n>>l>>h;
	vector<long long> f;
	for(int i=0;i<n;i++) {
		long long temp;
		cin>>temp;
		f.push_back(temp);
	}

	for(long long i=l;i<=h;i++) {
		for(int j=0;j<n;j++) {
			if(!(f[j]%i==0 || i%f[j]==0)) {
				break;
			} 
//			cout<<"i"<<i<<"j"<<j<<endl;
			if(j==n-1) {
				cout<<i<<endl;
				return;
			
			}
		}
		
	}
	cout<<"NO"<<endl;
}
