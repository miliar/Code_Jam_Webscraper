#include <cstdio>
int t,n,s,p,o;
int main(){
   scanf("%d",&t);
   for(int cs=1;cs<=t;++cs){
      scanf("%d%d%d",&n,&s,&p);
      o=0;
      for(int i=1;i<=n;++i){
	 int tt;
	 scanf("%d",&tt);
	 int k=tt/3;
	 if(tt%3==0){
	    if(k>=p) ++o;
	    else if((k+1>=p)&&(s>0)&&(k>0)) {++o;--s;}
	 }
	 if(tt%3==1){if(k+1>=p) ++o;}
	 if(tt%3==2){
	    if((k+1)>=p) ++o;
	    else if(((k+2)>=p)&&(s>0)){++o;--s;};
	 }
      }
      printf("Case #%d: %d\n",cs,o);
   }
   return 0;
}
