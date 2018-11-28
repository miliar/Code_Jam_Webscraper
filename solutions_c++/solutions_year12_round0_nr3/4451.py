#include <cstdio>

int flag[2000000][6];

int r(int n, int &mon){
	int ret = 0;
	while(n){
		mon *= 10;
		n /= 10;
		ret ++;
	}
	return ret;
}
int main(){
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("C-small-attempt0.out","w",stdout);
	int T,a,b, j=0;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		scanf("%d%d",&a,&b);
		int count=0,tmp,len,mon,y;
		for(int x=a;x<=b;x++){
			flag[x][10]=0;
			len=0, mon=1, tmp=x;
			len = r(tmp, mon);
			mon/=10;
			tmp=x;
			for(int i=1;i<len;i++){
				tmp = y=tmp/mon+10*(tmp%mon);
				if(y<a||y>b||x>=y) continue;
				j = 0;
				while(j < flag[x][10] && flag[x][j] != y ) j++;
				if(j>=flag[x][10]){
					count++;
					flag[x][j]=y;
					flag[x][10]++;
				}
			}
		}
		printf("Case #%d: %d\n", t,count);
	}
	return 0;
}

