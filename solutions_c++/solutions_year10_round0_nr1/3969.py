#include<cstdio>
#include<algorithm>

using namespace std;

int tcc,n,m,ans;
int main(){
	int i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tcc);
	for (int tc=0;tc<tcc;tc++){
		scanf("%d %d",&n,&m);
		ans=(m!=0)? 1:0;
		for(i=1;i<=n;i++){
			if (m%2==0){
				ans=0;
				break;
			}
			m/=2;
		}
		printf("Case #%d: %s\n",tc+1,ans? "ON":"OFF");
	}
	return 0;
}