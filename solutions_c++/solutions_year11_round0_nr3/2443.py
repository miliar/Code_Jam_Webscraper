//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, to) for(int i = 0; i<to; ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)

int sum, x, men, N, a,t;

int main(){
	scanf("%d", &t);
	For(T,t){
		scanf("%d", &N);
		men = 1000000047;
		x = 0;
		sum = 0;
		For(i, N) {
			scanf("%d", &a);
			men = min(a,men);
			x = x^a;
			sum+=a;
		}
		if (x!=0) printf("Case #%d: NO\n",T+1);
		else printf("Case #%d: %d\n",T+1, sum-men);
	}
	
}