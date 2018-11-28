#include <stdio.h>
#include <algorithm>

int t,T;
int tot[105];

bool pointwhensurprised(int number,int p){
	int mid = number / 3;
	for (int lower = std::max(0,mid-2) ;lower <= mid+2; ++lower){
		int upper = lower + 2;
		int center = number - lower - upper;
		if (lower <= center && center <= upper){
			if (upper >= p)
				return true;
		}
	}
	return false;
}

bool pointwhennotsurprised(int number,int p){
	int mid = number / 3;
	for (int lower = std::max(0,mid-2) ;lower <= mid+2; ++lower){
		for (int k=0;k<=1;++k){
			int upper = lower + k;
			int center = number - lower - upper;
			if (lower <= center && center <= upper){
				if (upper >= p)
					return true;
			}
		}
	}
	return false;
}

int main(){
	freopen("b.in","rt",stdin);
	freopen("b.out","wt",stdout);
	scanf("%d",&T);
	for (t=1;t<=T;++t){
		int n,s,p;
		scanf("%d %d %d",&n,&s,&p);
		for (int i=0;i<n;++i)
			scanf("%d",&tot[i]);
		bool surprised[105] = {0,};

		int remaineds = s;
		int point = 0;

		for (int level=0;level<=1;++level){
			for (int i=0;i<n;++i){
				if (level==0){
					if (remaineds==0)
						break;
					if (pointwhensurprised(tot[i],p) && !pointwhennotsurprised(tot[i],p)){
						++point;
						--remaineds;
						surprised[i] = true;
					}
				}
				else{
					if (!surprised[i]){
						if (pointwhennotsurprised(tot[i],p)){
							++point;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",t,point);
	}
	return 0;
}