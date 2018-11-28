#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
	int cas;
	scanf("%d",&cas);
	for(int j=1;j<=cas;j++){
		double prob,ans,in;
		int A,B;
		vector<double> v;v.clear();
		scanf("%d %d",&A,&B);
		prob=1;
		for(int i=0;i<A;i++){
			scanf("%lf",&in);
			v.push_back(in);
			prob*=in;
		}
		ans=2+B;
		ans=min(ans,prob*(B-A+1)+(1-prob)*(B-A+2+B));
		for(int i=A-1;i>0;i--){
			prob/=v[i];
			ans=min(ans,prob*(B-i+1)+(1-prob)*(B-i+2+B)+A-i);
//			printf("%lf %lf\n",prob,ans);
		}

		printf("Case #%d: %lf\n",j,ans);
	}
}

