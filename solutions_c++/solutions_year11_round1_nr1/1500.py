#include<vector>
#include<iostream>
#include<algorithm>
#include<numeric>
#include<limits>
#include<map>
#include<set>
#include<string>
#include<queue>
using namespace std;
void process();
long long gcd(long long a,long long b);
int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		cout<<"Case #"<<i<<": ";
		process();
	}
}

long long gcd(long long a,long long b) {
	if(a==0 || b==0) {
		return 0;
	}
	 while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}
	
void process() {
	long long n, pd,pg,p,g;
	cin>>n>>pd>>pg;
	if(pg==100&&pd!=100) {
		cout<<"Broken"<<endl;
		return;
	}
	if(pg==0&&pd!=0) {
		cout<<"Broken"<<endl;
		return;
	} if(pg==0&& pd==0) {
		cout<<"Possible"<<endl;
		return;
	}
	p = gcd(100,pd);
	long long d=100/p;
	if(d>n) {
		cout<<"Broken"<<endl;
		return;
	}
	d=pd/p;
	p=gcd(100,pg);
	g= pg/p;
	
//	cout<<"d"<<d<<"g"<<g<<endl;
	while(g<d) {
		g+=p;
	}
	if(g>=100) {
		cout<<"Broken"<<endl;
		return;
	}
	cout<<"Possible"<<endl;
}
