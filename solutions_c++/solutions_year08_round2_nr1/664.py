#include <iostream>

using namespace std;
int test;
int x[200],y[200];
long long a,b,c,d;
int n,m;

int main(void){
	freopen("file.in","r",stdin);
	freopen("file.out","w",stdout);
	cin>>test;
	for (int t=1;t<=test;t++){
		printf("Case #%i: ",t);
		cin>>n>>a>>b>>c>>d>>x[0]>>y[0]>>m;
		for (int i=1;i<n;i++){
			long long X=(a*x[i-1]+b);
			x[i]=X%m;
			long long Y=(c*y[i-1]+d);
			y[i]=Y%m;
		}
		int ans=0;
		for (int i=0;i<n;i++)
			for (int j=i+1;j<n;j++)
				for (int k=j+1;k<n;k++){
					long long X=x[i]+x[j];
					X+=x[k];
					long long Y=y[i]+y[j];
					Y+=y[k];
					if (X%3==0 && Y%3==0) ans++;
				}
		printf("%i\n",ans);
	}

	
	return 0;
}
