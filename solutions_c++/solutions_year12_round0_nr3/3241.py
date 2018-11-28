#include<iostream>
#include<string>
#include<fstream>
#include<cmath>
using namespace std;
inline int digits(int n){
	int d=0;
	while(n){
		n/=10;
		d++;
	}
	return d;
}
inline int power10(const int d){
	int ans = 1;
	for(int i=0; i<d; i++)
		ans *= 10;
	return ans;
}


int findNumCount(const int N, const int b){
	extern ofstream cout;
	int num=N, D = digits(num), ans=0;
	for(int i=1; i<D; i++){
		int dig = num%10;
		num /=10;
		if(dig==0)
			continue;
		num += power10(D-1)*dig;
		if(num<=b && num>N){
			ans++;
//			if(ans==1)	cout<<N<<": ";
//			cout<<num<<" ";
		}
	}
//	if(ans)		cout<<endl;
	return ans;
}

ofstream cout("out.txt");

int main(){
	
	ifstream cin("in.txt");
	extern ofstream cout;
	int te;
	cin>>te;
	
	for(int test=1; test<=te; test++){
		int a,b, ans=0;
		cin>>a>>b; 
		for(int i=a; i<b; i++){
			ans += findNumCount(i, b);
		}
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
	return 0;
}
