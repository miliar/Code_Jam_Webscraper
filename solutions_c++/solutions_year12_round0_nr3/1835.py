#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<cmath>
using namespace std;

int a,b;
set<int> s;

int adv(int in){
	int nd = (int)floor(log10(in))+1;
	int ans=0;
	s.clear();
	int orig=in;
	s.insert(in);
	int last,t=nd;
	while(t--){
		last=in%10;
		in/=10;
		in+=last*pow(10,nd-1);
		if(!s.count(in)&&in<=b&&in>=a&&in>orig){
			ans++;
			s.insert(in);
		}
	}
	return ans;
}

int main(){
	int cas,ans;
	scanf("%d",&cas);
	for(int i=1;i<=cas;i++){
		ans=0;
		scanf("%d %d",&a,&b);
		for(int j=a;j<b;j++){
			ans+=adv(j);
		}
		printf("Case #%d: %d\n",i,ans);
	}
}
