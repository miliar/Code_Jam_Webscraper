#include <iostream>
#include <cstdio>
#define M 1010
using namespace std;
int main()
{
	int t,cas = 0;
	//freopen("./bb.in","r",stdin);
	//freopen("./bb.out","w",stdout);
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		int min = 10000000,sum = 0,x = 0,f;
		while(n--){
			cin>>f;
			x ^= f;
			if(min > f){
				min = f;			
			}
			sum += f;
		}
		cout<<"Case #"<<++cas<<": ";
		if(x){
			cout<<"NO"<<endl;
		}
		else{
			cout<<sum - min<<endl;
		}
	}
	return 0;
}

