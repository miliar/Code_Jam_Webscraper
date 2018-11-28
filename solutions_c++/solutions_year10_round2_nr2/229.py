#include<cstdio>
#include<cstring>
int tc;
int nducks,nmin,barn,ntime;
int x[500],v[500];
bool used[500];
int main(){
 
 scanf("%d",&tc);
 for (int ti = 1; ti <= tc; ti++){
     memset(used,false,sizeof(used));
     scanf("%d %d %d %d",&nducks, &nmin,&barn, &ntime);    
     for (int i = 1; i <= nducks; i++){
         scanf("%d",&x[i]);
     }
     for (int i = 1; i <= nducks; i++){
         scanf("%d",&v[i]);    
     }
     int r = 0;
     int res =  0;
     for (int i = nducks; i >= 1; i--){
         double temp = (barn-x[i]) / (double) v[i];
         if (temp <= (double)ntime){
            r++;         
            for (int j = i+1; j <= nducks; j++){
                if (used[j]) continue;
                if (v[j] < v[i]) {
                         double temp= (x[i]-x[j])/(double)(v[j]-v[i]);
                         temp = temp * v[i]+x[i];
                         if (temp < (double)barn) res++;
                }
            }
            used[i] = true;
         }    
         
         if (r >= nmin) break;
     }
     if (r >= nmin)printf("Case #%d: %d\n",ti,res);
     else printf("Case #%d: IMPOSSIBLE\n",ti);
 }   
}
