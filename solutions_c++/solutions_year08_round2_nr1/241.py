#include<iostream>
#include<deque>
using namespace std;
struct Point{
	long long x, y;
};
Point now;
deque<Point>kk;
int main(){
	freopen("A-small-attempt0.in" ,"r",stdin);
	freopen("ans1.out" ,"w" , stdout);
	int Case = 0;
	int test;
	scanf("%d" , &test);
	long long  N , A , B, C , D , x0 , y0 ,M;
	while(test--){
		Case++;
		kk.clear();
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld" , &N , &A , &B , & C ,&D , &x0 , &y0 ,&M);
		now.x = x0 ;
		now.y = y0 ;
		kk.push_back(now);
		int i ,j , k;
		for(i = 1 ; i < N ;i++){
			now.x = (A * now.x + B)%M;
			now.y = (C * now.y + D)%M;
			kk.push_back(now);
		}
		long long count = 0;
		for(i = 0 ; i < kk.size() ; i++){
			for(j = i+1 ; j < kk.size() ;j++){
				for(k = j+1 ; k<kk.size() ;k++){
					if((kk[i].x+kk[j].x+kk[k].x)%3==0){
						if((kk[i].y+kk[j].y+kk[k].y)%3==0){
							count++;
						}
					}
				}
			}
		}
		printf("Case #%d: %lld\n" , Case , count);

	}
	return 0;
}