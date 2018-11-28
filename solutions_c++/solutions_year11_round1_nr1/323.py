#include<iostream>
#include<string>
#include<cstring>

#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
typedef long long LL;
using namespace std;

int main(){
	int cas;
	cin>>cas;
	
	for(int ca = 1; ca<=cas; ++ca){
		LL n, pd, pg;
		cin>>n>>pd>>pg;
		LL deno = 100;
		if (pd %2 == 0){
			deno /= 2;
			
			if((pd/2) %2 == 0)
				deno /=2;
		}
		if (pd %5 == 0){
			deno /= 5;
			if((pd/5) %5 == 0)
				deno /=5;
		}
		
		if (deno > n ){
			cout<<"Case #"<<ca<<": Broken"<<endl;
			continue;
		}
		
		if (pg == 100){
			if (pd != 100){
				cout<<"Case #"<<ca<<": Broken"<<endl;
				continue;
			}
		}
		if(pg == 0){
			if (pd != 0){
				cout<<"Case #"<<ca<<": Broken"<<endl;
				continue;
			}
		}
		cout<<"Case #"<<ca<<": Possible"<<endl;
	}
}
