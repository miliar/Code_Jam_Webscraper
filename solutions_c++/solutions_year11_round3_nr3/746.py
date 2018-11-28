#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<cmath>
#include<map>
#include<cstdlib>
#include<cstdio>
#include<climits>
#include<algorithm>
#include<cstring>

using namespace std;

#define PB(x) push_back(x)
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define VVI (vector<vector<int> >) 
#define FOR(I,A,B) for(int I=A;I<B;I++)
#define FORA(I,A,B) for(int I=A;I>B;I--)
#define SORT(x) sort(x.begin(),x.end())

long long gcd (long long a, long long b){
	if(b==0){
		return a;
	}else{
		return gcd(b,a%b);
	}
}

int main(){
	long long a,b,c,x,y,z,l,h,ans;
	int t,n,f,fm;
	vector<long long> v;
	cin>>t;
	for(int k=1;k<=t;k++){
		v.clear();
		cin>>n>>l>>h;
		for(int i=0;i<n;i++){
			cin>>x;
			v.PB(x);
		}
		fm=0;
		for(int i=l;i<=h;i++){
			f=1;
			for(int j=0;j<n;j++){
				if(v[j]%i==0 || i%v[j]==0){
				}else{
					f=0;
					break;
				}
			}
			if(f==1){
				ans=i;
				fm=1;
				break;
			}
		}

		if(fm==1){
			cout<<"Case #"<<k<<": "<<ans<<endl;
		}else{
			cout<<"Case #"<<k<<": "<<"NO"<<endl;
		}
	}
	return 0;
}
