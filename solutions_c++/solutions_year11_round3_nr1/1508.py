#include<stdio.h>

int main(){
    int T,n,i,j,k,l,cant;
    char arr[100][100];
    scanf("%d",&T);
    for(i=0;i<T;i++){
                     scanf("%d %d\n",&n,&l);
                     cant=0;
                     for(j=0;j<n;j++){
                                      gets(arr[j]);
                     }
                     for(j=0;j<n;j++){
                                      for(k=0;k<l;k++){
                                                       if(arr[j][k]=='#'){
                                                                          if(j+1<n && k+1<l){
                                                                                   if(arr[j][k+1] =='#' && arr[j+1][k]=='#' && arr[j+1][k+1]=='#'){
                                                                                          arr[j][k]='/';
                                                                                          arr[j][k+1]='\\';
                                                                                                       arr[j+1][k]='\\';
                                                                                                       arr[j+1][k+1]='/';
                                                                                   }
                                                                                   else{
                                                                                        cant=1;
                                                                                        break;
                                                                                   }
                                                                          }
                                                                          else{
                                                                               cant=1;
                                                                               break;
                                                                          }
                                                       }
                                      }
                                      if(cant==1)break;
                     }
                     printf("Case #%d: \n",i+1);
                     if(cant==1)printf("Impossible\n");
                     else{
                          for(j=0;j<n;j++){
                                           printf("%s\n",arr[j]);
                          }
                     }
    }                
    
}
