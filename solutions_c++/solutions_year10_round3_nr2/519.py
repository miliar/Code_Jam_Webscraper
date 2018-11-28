#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<list>
#define f(i,n) for(int i=0;i<n;i++)
#define vi vector<int>
#define vs vector<string>
#define p_b push_back
using namespace std;
//stringstream ss (stringstream::in | stringstream::out);
bool ispower(int n){
	while(n!=1){
		if(n%2)
			return false;
		n/=2;
	}
	return true;
}
int main(){
	fstream fin,fout;
	fin.open ("input.txt", fstream::in | fstream::out);
	fout.open ("output.txt", fstream::in | fstream::out);
	int t;
	fin>>t;
	f(k,t){
		long l,p,c;
		fin>>l>>p>>c;
		int x=c*l;
		int k1=0;
		while(x<p){
			k1++;
			x*=c;
		}
		//cout<<"k1="<<k1<<endl;
		int k2=1,ans=0;
		while(k2<=k1){
			ans++;
			k2*=2;
		}

		//cout<<ans<<endl;
		
		fout<<"Case #"<<k+1<<": "<<ans<<endl;

		

	}

}

