#include<stdio.h>

FILE *inf,*ouf;

int main(){
    
    long z=0,l,i,ii,r,t,k,n,g[1001];
    long long dan ,ans;
    inf = fopen("c.in","r");  
    ouf = fopen("c.txt","w");
    fscanf(inf,"%d",&t);
    while(t--){
    
      fscanf(inf,"%d%d%d",&r,&k,&n);
      ans = 0;
      for(i=0;i<n;i++)
        fscanf(inf,"%d",&(g[i]));
      for(ii=0,i = 0;i<r;i++){
       dan=0;ii--;
       l=0;
       while(ii=(ii+1)%n,(dan += g[ii])<=k && (l<n))l++;
             ans+=dan-g[ii];

         
           



}fprintf(ouf,"Case #%d: %d\n",++z,ans); 
    }
    
    
}
