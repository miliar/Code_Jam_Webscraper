#include<stdio.h>
int main(){
    FILE *fi= fopen("C-small-attempt0.in", "r");
    FILE *fo= fopen("C-small-attempt0.out", "w");

    int R,T,MAX,N,k;
    fscanf(fi,"%d",&T);
    for(k=1;k<=T;k++){
          fscanf(fi,"%d %d %d",&R,&MAX,&N);
          int g[N],s,count=0,i,a;
          for(i=0;i<N;i++)     fscanf(fi,"%d",&g[i]);   
          while(R--){
                i=0;s=0;
                while(s<=MAX&&i!=N)     s+=g[i++];
                if(i==N && s<=MAX) {  count=s*(R+1); break;}
                count+=s-g[--i];
                while(i--){
                     a=g[0];
                     for(int j=0;j<N;j++)  g[j]=g[j+1];
                     g[N-1]=a;
                }               
          }
          fprintf(fo,"Case #%d: %d\n",k,count);
    }
    return 0;
}
