#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

bool fuck = 0;
void Pr(int a,int b,int c,int d,int e,int f){
	if(!fuck)
		printf(" %d %d %d %d %d %d\n",a,b,c,d,e,f);
	else
		printf(" %d %d %d %d %d %d\n",b,a,d,c,f,e);
}

int main(){
	int z, m, n;
	scanf("%d", &z);
	int A;
	for(int zz=1; zz<=z; zz++){
		printf("Case #%d:", zz);
		scanf("%d%d%d",&m,&n,&A);
	//	fuck = 0;
//		if (m<n)
	//		swap(m,n), fuck=1;
		int x, y;
		bool found = 0;
		if ( m*n >= A )
		for(int x=1; x<=m && !found; x++)
			for(int y=1; y<=n && !found; y++){
				int a, b;
				int c = x*y - A;
				if (c < 0)
					continue;
				int bdd = (int)sqrt(c)+1;
				for(int a=c/y; a<=bdd; a++){
					if (a==0 || c%a)
						continue;
					int b = c/a;
					if( b<=y ){
						found = 1;
						printf(" %d %d %d %d %d %d\n",x-a,0,x,y,0,y-b);
		//				Pr(
			//				x-a, 0, x, y, 0, y-b);
						break;
					}
				}
			}
			if(!found)
				puts(" IMPOSSIBLE");
	//			puts(" -1 -1 -1 -1 -1 -1");
	}
	return 0;
}
