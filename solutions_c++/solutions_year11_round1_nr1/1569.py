#include <cstdio>
int out(short turn, bool a){
   if(a)printf("Case #%d: Possible\n", turn+1);
   else printf("Case #%d: Broken\n", turn+1);
}
int hcf(int a, int b){
	 if(b==0)return a+b;
    return hcf(b,a%b);
}
int main(){
	 int T,pd,pg,d;
	 int N;
	 scanf("%d", &T);
	 for(int i=0;i<T;i++){
		 scanf("%d %d %d", &N, &pd, &pg);
		 if(pg==100&&pd!=100){out(i,0);continue;}
		 if(pg==0&&pd!=0){out(i,0);continue;}
		 if(pd==0)d=1;else d=100/hcf(100,pd);
		 //printf("%d,%d\n",d,N);
		 if(d>N){out(i,0);continue;}
		 out(i,1);
	 }
}
