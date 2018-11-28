#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

int t, c,d, n,xx[1005],jum[1005],ar[1005],maks;
bool nagis;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	
	for (int tc=0;tc<t;tc++){
		scanf("%d",&n);
		ar[0]=0;
		xx[0]=0;
		jum[0]=0;
		for (int i=1;i<=n;i++){
			scanf("%d",&ar[i]);
			xx[i]=xx[i-1]^ar[i];
			jum[i]=jum[i-1]+ar[i];
//			printf("%d\n",jum[i]);
		}
		maks = 0;
		nagis = true;
		for (int dep=1;dep<=n;dep++){
			for (int bel=1;bel<=n;bel++){
				if (((xx[dep-1]^xx[bel])==((xx[0]^xx[dep-1])^(xx[bel]^xx[n]))) && (jum[bel]-jum[dep-1]!=0&&jum[bel]-jum[dep-1]!=jum[n])){
//					printf("%d %d\n",(xx[dep-1]^xx[bel]),(xx[0]^xx[dep-1])^(xx[bel]^xx[n]));
//					printf("%d %d %d %d\n",jum[bel],jum[dep-1],jum[bel]-jum[dep-1],jum[n]-jum[bel]+jum[dep-1]);
					if ((jum[bel]-jum[dep-1]>(jum[n]-jum[bel]+jum[dep-1])) && (maks < jum[bel]-jum[dep-1]) && jum[bel]-jum[dep-1]<=jum[n]){
						maks = jum[bel]-jum[dep-1];
					}else if ((jum[bel]-jum[dep-1]<=(jum[n]-jum[bel]+jum[dep-1]))&&(maks <(jum[n]-jum[bel]+jum[dep-1])) && (jum[n]-jum[bel]+jum[dep-1])<=jum[n]){
						maks = jum[n]-jum[bel]+jum[dep-1];
					}//salah super tolol jing lupa kasus klo sama dengan hahahahah cacat
					// ini juga karna gw lupa klo bisa saling overlap yg ternyata ga masalah bzzz liat tc untung heheheh
//					printf("%d\n",maks);
					nagis = false;
				}
			}
		}
		if (nagis)printf("Case #%d: NO\n",tc+1);				
		else printf("Case #%d: %d\n",tc+1,maks);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
