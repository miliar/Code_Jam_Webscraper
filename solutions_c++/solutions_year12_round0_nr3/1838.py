#include <cstdio>
const int INF=2000005;
int t,a,b;
bool f[INF];
int getl(int k){
   int c=1;
   for(;k>0;k=k/10,c*=10);
   return c/10;
}
int shift(int k,int *l){
   int t;
   do{
      t=k%10;
      k=(k/10)+t*(*l);
   }while(t==0);
   return k;
}
int main(){
   scanf("%d",&t);
   for(int cs=1;cs<=t;++cs){
      long long o=0;
      scanf("%d%d",&a,&b);
      int l=getl(a);
      for(int i=a;i<=b;++i) f[i]=true;
      for(int i=a;i<=b;++i)
	 if(f[i]){
	    int k=shift(i,&l);
	    int t=1;
	    for(;k!=i;k=shift(k,&l))
	       if((a<=k)&&(k<=b)){
		  f[k]=false;
		  ++t;
	       }
	    o+=t*(t-1)/2;
	 }
      printf("Case #%d: %lld\n",cs,o);
   }
}
