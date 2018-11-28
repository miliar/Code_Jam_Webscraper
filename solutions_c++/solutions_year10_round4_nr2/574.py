#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int a[10][1024];
int m[1024];
int p;
int getac(int depth, int n, int miss){
	if(depth == p){
		if(miss<=m[n])
			return 0;
		else
			return -1;
	}else{
		int ret,ret2;
		int t1=getac(depth+1, n*2,miss+1);
		int t2=getac(depth+1, n*2+1,miss+1);
		if(t1==-1 || t2==-1)
			ret=-1;
		else
			ret=t1+t2;

		t1=getac(depth+1, n*2,miss);
		t2=getac(depth+1, n*2+1,miss);
		if(t1==-1 || t2==-1)
			ret2=-1;
		else
			ret2=t1+t2+a[depth][n];

		if(ret==-1)
			return ret2;
		if(ret2==-1)
			return ret;
		return min(ret,ret2);
	}
}

int main(){
	int T;
	scanf("%d", &T);
	for(int TT=1;TT<=T;TT++){
		//int p;
		scanf("%d", &p);
		for(int i=0;i<(1<<p);i++){
			scanf("%d",&m[i]);
			//m[i] = p-m[i];
		}
		for(int i=p-1;i>=0;i--){
			for(int j=0;j<(1<<i);j++){
				//int a[i][j];
				scanf("%d",&a[i][j]);
			}
		}

		

		//for()

		/*memset(a,0,sizeof(a));
		for(int k=0;k<(1<<p);k++){
			int t = k;
			for(int i=p-1;i>=0;i--){
				t/=2;
				if(m[k]>0){
					m[k]--;
				}else{
					a[i][t]=1;
				}
			}
		}
		int ret=0;
		for(int i=0;i<p;i++){
			for(int j=0;j<1024;j++){
				if(a[i][j]){
					ret++;
				}
			}
		}*/

		printf("Case #%d: %d\n", TT, getac(0,0,0));
	}
}