#include <cstdio>

int c,n,m,AC;

//int x,t,p[35],C[35];

int main(){
	/*

	for (int i=1;i<=30;i++){
		p[0]=1;
		for (int j=1;j<=i;j++) p[j]=0;
		t=0;
		while (t<i){
			x=0;
			while (p[x]) x++;
			C[i]++;
			for (int j=1;j<=x;j++){
				p[j]^=1;
				if (p[j]==0) t--;
				if (p[j]==1) t++;
			}
		}
		printf("%d %d\n",i,C[i]);
	}
	
	*/
	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
		scanf("%d%d",&n,&m);
		if (!m) AC=0;
		else AC=(m+1)%(1<<n)?0:1;
		printf("Case #%d: %s\n",tc,AC?"ON":"OFF");
	}


	return 0;
}
