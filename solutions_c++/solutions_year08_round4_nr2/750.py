#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<string>
#include<vector>
#include<queue>

using namespace std;

#define SZ 100
#define min(a , b) (a < b ? a : b)
#define max(a , b) (a > b ? a : b)

typedef __int64 II;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<II> vii;

typedef struct{
	int x , y;
}point;

int triangle_area(point a,point b,point c)
{
	return abs(a.x*b.y-a.y*b.x+a.y*c.x-a.x*c.y+b.x*c.y-c.x*b.y);
}

int main(){
	freopen("b.in" , "r" , stdin);
	freopen("b.out" , "w" , stdout);
	int test , kase = 1 , n , m , a;
	scanf("%d" , &test);
	while(test--){
		scanf("%d%d%d" , &n  , &m , &a);
		point aa , bb , cc;
		cc.x = 0;cc.y = 0;
		for(aa.x = 0;aa.x<=n;aa.x++)
			for(aa.y = 0;aa.y<=m;aa.y++)
				for(bb.x = 0;bb.x<=n;bb.x++)
					for(bb.y = 0;bb.y<=m;bb.y++){
						if(triangle_area(aa , bb , cc) == a){
							printf("Case #%d: %d %d %d %d %d %d\n" , kase++ , aa.x , aa.y , bb.x , bb.y , cc.x , cc.y);
							goto done;
						}
					}
	printf("Case #%d: IMPOSSIBLE\n" , kase++);
	done:;
	}
	return 0;
}
