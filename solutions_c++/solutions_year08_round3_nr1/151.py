#include <iostream>
#define task "file"

using namespace std;
int test;
int p,k,l;
int d[2000];

int main(void){
	freopen(task".in","r",stdin);
	freopen(task".out","w",stdout);
	cin>>test;
	for (int z=1;z<=test;z++){
		printf("Case #%i: ",z);
		scanf("%i %i %i",&p,&k,&l);
		for (int i=0;i<l;i++) scanf("%i",&d[i]);
		sort(d,d+l,greater<int>());
		int i=0;
		long long ans=0;
		for (int q=0;q<p;q++){
			int cnt=min(l-i,k);
			long long cur=0;
			for (int j=i;j<i+cnt;j++) cur+=d[j];
			i+=cnt;
			ans+=cur*(q+1);		
		}
		cout<<ans<<endl;
	}	

	return 0;
}
