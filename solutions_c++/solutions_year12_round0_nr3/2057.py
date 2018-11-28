#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<sstream>
#include<set>
using namespace std;
int ndigit(int n){
	int r=0;
	do{
		n/=10;
		r++;
	}while(n>0);
	return r;
}
vector<int> perm(int n,int digit){
	int m;//n<=m<=B
	vector<int> result;
	int big=0;
	for(int i=1;i<digit;++i){
		if(big==0){
			big=10;
			continue;
		}
		big*=10;
	}
	for(int i=1;i<digit;++i){
		m=n/10+n%10*big;
		n=m;
		result.push_back(m);
	}
	for(int i=0;i<result.size();++i){
	}
	return result;
}
int solve(int A,int B){
	int digit=ndigit(A);
	int result=0;
	for(int n=A;n<B;++n){
		vector<int> allm=perm(n,digit);
		set<int> s;
		for(int i=0;i<allm.size();++i){
			int m=allm[i];
			if(n<m && m<=B ){
			//cout<<n<<" "<<m<<endl;
				s.insert(m);
			//	result++;
			}
		}
		result+=s.size();
	}
	return result;
}
int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;++i){
		int A,B;
		cin>>A>>B;
		int r=solve(A,B);
		cout<<"Case #"<<i+1<<": "<<r<<endl; 
	}
}
