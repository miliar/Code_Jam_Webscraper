#include <iostream>
using namespace std;

const int N=200;

int t;
int sum, now,mm, tmp;
int main(){
	freopen("c.in", "r",stdin);	
	freopen("c.txt", "w",stdout);
	cin>>t;
	int n, sum;
	for(int L=1; L<=t; ++L){
		cin>>n;
		sum=0;
		now=0;
		mm=1000000000;
		for(int i=0; i<n; ++i)
		{
			cin>>tmp;
			sum+=tmp;
			now^=tmp;
			if (tmp<mm) mm=tmp;
			
		}
	
	
		cout<<"Case #"<<L<<": ";
		if (now==0) cout<<sum-mm<<endl;
		else cout<<"NO"<<endl;
	}	
}
