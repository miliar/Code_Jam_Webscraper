#include <iostream>
#include <string>

using namespace std;

const int MAXN=1000002;

int T,k,n;
int a[MAXN];

int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>T;
	for(int casetime=0;casetime<T;++casetime){
		cin>>k>>n;
		memset(a,0,sizeof(a));
		int now=0;
		for(int i=1;i<=k;++i){
			int count=0;
			while(count<i){
				++now;
				if(now>k) now=1;
				while(a[now]!=0){
					++now;
					if(now>k) now=1;
				}
				++count;
			}
			a[now]=i;
		}
		cout<<"Case #"<<casetime+1<<":";
		for(int i=0;i<n;++i){
			int tmp;
			cin>>tmp;
			cout<<" "<<a[tmp];
		}
		cout<<endl;
	}
	return 0;
}


		