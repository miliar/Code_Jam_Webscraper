#include <iostream>
#define task "file"

using namespace std;
long long Mod=1000000007;
int test;
int n,m,N;
int d[2000];
int a[2000];
long long t[2000];
long long x,y,z;

int main(void){
	freopen(task".in","r",stdin);
	freopen(task".out","w",stdout);
	cin>>test;
	for (int q=1;q<=test;q++){
		printf("Case #%i: ",q);
		cin>>n>>m>>x>>y>>z;
		//cout<<n<<" "<<m<<" "<<x<<" "<<y<<" "<<z<<endl;
		for (int i=0;i<m;i++) scanf("%i",&d[i]);
		N=0;
		for (int i=0;i<n;i++){
			a[N++]=d[i%m];
			//cout<<(d[i%m])<<endl;
			d[i%m]=(x*d[i%m]+y*(i+1))%z;	
		}
		for (int i=0;i<N;i++) t[i]=1;
		
		for (int i=1;i<N;i++){
			for (int j=0;j<i;j++)
				if (a[i]>a[j]){
					t[i]+=(t[j]);
					t[i]%=Mod;
				}
		}
		//for (int i=0;i<N;i++) printf("%i ",(int)a[i]);
		//printf("\n");
		long long ans=0;
		for (int i=0;i<N;i++){
			ans+=t[i];
			ans%=Mod;
		}
		cout<<ans<<endl;
	}	

	return 0;
}
