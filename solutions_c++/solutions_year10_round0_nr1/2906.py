 #include "stdio.h"
int N,K,a[101];
void solve(){
	int i;
	a[1]=1;
     for(i=2;i<=100;i++)
       a[i]=2*a[i-1]+1;
}

int main(){
#ifdef _DEBUG
	freopen("A-large.in", "r", stdin);
	freopen("out3.txt", "w", stdout);
#endif

    int T,j=1,i,t;

scanf("%d",&T);
   for(i=1;i<=T;i++)
     { scanf("%d%d",&N,&K);
      solve();

	  while(a[N]+1<K)
               { t=1;
                 while((a[N]+1)*t<K)
                    t=t*10;
                 t=t/10;
                 K=K-(a[N]+1)*t;  }

     if(K==a[N])
        printf("Case #%d: ON\n",i);
      else printf("Case #%d: OFF\n",i);
   }
return 0;
}
