#include <iostream>

using namespace std;

struct line{
	int a,b;
};

line a[1001];
int n;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("Rope Intranet.out","w",stdout);
	int test,i,j,k,ans;
	cin>>test;
	for (i=1;i<=test;i++) {
		cin>>n;
		for (j=1;j<=n;j++) cin>>a[j].a>>a[j].b;
		ans=0;
		for (j=1;j<=n;j++) {
			for (k=1;k<=n;k++) { 
				if (j!=k) {
					if (a[j].a<a[k].a && a[j].b>a[k].b) ans++;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}