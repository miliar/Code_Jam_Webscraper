#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <stack>
#include <cstdlib>

using namespace std;
class walk{
	public:
	double s,e,speed;
	walk(double a,double b,double c){s=a;e=b;speed=c;}
};
bool cmp(walk a , walk b){
	if(a.speed < b.speed)return true;
	return false;
}
int main(){
	int i,j,k,n,N,T,l,m,M;
	double X,S,R,t;
	double temp1,temp2,temp3;
	double left = 0;
	scanf("%d",&n);
	vector<walk> way;
	double ans=0;
	for(T=0;T<n;T++){
	way.clear();
	ans=0;
	double total_walk=0;
		scanf("%lf %lf %lf %lf %d ",&X,&S,&R,&t,&N);
		for(i=0;i<N;i++){
		cin >> temp1>>temp2>>temp3;
		way.push_back(walk(temp1,temp2,temp3));
			total_walk+=temp2-temp1;
			
		}
		left = X-total_walk;
		sort(way.begin(),way.end(),cmp);
		double temp;
		double dis;
		double temp_t;
//		printf("left is %lf left/R is %lf t is %lf \n",left,left/R,t);
		if(left/R >=t){
			ans+=t;
			left-=R*t;
			t=0;
		}else{
			temp_t = t;
			t-=left/R;
			left -=(temp_t - t)*R;
			ans+=temp_t-t;
		}
//		printf("left is %lf left/R is %lf t is %lf \n",left,left/R,t);
		for(i=0;i<N;i++){
			if(t>0){
			temp=(way[i].e-way[i].s)/(R+way[i].speed);
					if(temp <=t){
					t-=temp;
					ans+=temp;
					}else{
					ans+=t;
					dis = (R+way[i].speed)*t;
					dis = way[i].e-way[i].s -dis;
					ans+= dis/(S+way[i].speed);
					t=0;
					}
			}else{
			ans+=(way[i].e-way[i].s)/(S+way[i].speed);

			}
//			printf("cur ans is %lf cur t is %lf\n",ans,t);
		}
		if(left >0){
			ans+=left/S;
		}
		printf("Case #%d: %lf\n",T+1,ans);
	}
	return 0;
}

