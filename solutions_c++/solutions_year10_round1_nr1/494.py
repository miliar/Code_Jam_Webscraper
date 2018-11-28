#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;
char aa[100][100];
char bb[100][100];
int main()
{
     freopen("A-large.in","r",stdin);//A-small-attempt0.in
     freopen("1.txt","w",stdout);
     int T,i,j,n,k,h;
     scanf("%d",&T);
     for(int test=0;test<T;test++){
          scanf("%d%d",&n,&k);
          for(i=0;i<n;i++)
          for(j=0;j<n;j++)
          scanf(" %c",&aa[i][j]);
          for(i=0;i<n;i++)
          for(j=0;j<n;j++)
          bb[i][j]=aa[n-1-j][i];
          for(i=n-1;i>=0;i--){
               for(j=0;j<n;j++){
                   if(bb[i][j]!='.'){
                        for(h=i+1;h<n;h++){
                            if(bb[h][j]!='.')break;                   
                        }
                        h--;
                        char temp=bb[i][j];
                        bb[i][j]='.';
                        bb[h][j]=temp;                  
                   }                 
               }                    
          }
          //for(i=0;i<n;i++){
         // for(j=0;j<n;j++) printf("%c",bb[i][j]);puts("");}
          bool blue=0;
          for(i=0;i<n;i++){
          for(j=0;j<n;j++){
              bool flag=1;
              for(h=0;h<k;h++){
                  if(i+h>=n||bb[i+h][j]!='B'){
                      flag=0;
                      break;           
                  }        
              } 
              if(flag){
                 blue=1;
                 break;
              }                
          } 
          if(blue)break;
          }   
          for(i=0;i<n;i++){
          for(j=0;j<n;j++){
              bool flag=1;
              for(h=0;h<k;h++){
                  if(j+h>=n||bb[i][j+h]!='B'){
                      flag=0;
                      break;           
                  }        
              } 
              if(flag){
                 blue=1;
                 break;
              }                
          } 
          if(blue)break;
          }   
          for(i=0;i<n;i++){
          for(j=0;j<n;j++){
              bool flag=1;
              for(h=0;h<k;h++){
                  if(i+h>=n||j+h>=n||bb[i+h][j+h]!='B'){
                      flag=0;
                      break;           
                  }        
              } 
              if(flag){
                 blue=1;
                 break;
              }                
          } 
          if(blue)break;
          }   
          for(i=0;i<n;i++){
          for(j=0;j<n;j++){
              bool flag=1;
              for(h=0;h<k;h++){
                  if(i-h<0||j+h>=n||bb[i-h][j+h]!='B'){
                      flag=0;
                      break;           
                  }        
              } 
              if(flag){
                 blue=1;
                 break;
              }                
          } 
          if(blue)break;
          }
          bool red=0;
          for(i=0;i<n;i++){
          for(j=0;j<n;j++){
              bool flag=1;
              for(h=0;h<k;h++){
                  if(i+h>=n||bb[i+h][j]!='R'){
                      flag=0;
                      break;           
                  }        
              } 
              if(flag){
                 red=1;
                 break;
              }                
          } 
          if(red)break;
          }   
          for(i=0;i<n;i++){
          for(j=0;j<n;j++){
              bool flag=1;
              for(h=0;h<k;h++){
                  if(j+h>=n||bb[i][j+h]!='R'){
                      flag=0;
                      break;           
                  }        
              } 
              if(flag){
                 red=1;
                 break;
              }                
          } 
          if(red)break;
          }   
          for(i=0;i<n;i++){
          for(j=0;j<n;j++){
              bool flag=1;
              for(h=0;h<k;h++){
                  if(i+h>=n||j+h>=n||bb[i+h][j+h]!='R'){
                      flag=0;
                      break;           
                  }        
              } 
              if(flag){
                 red=1;
                 break;
              }                
          } 
          if(red)break;
          }   
          for(i=0;i<n;i++){
          for(j=0;j<n;j++){
              bool flag=1;
              for(h=0;h<k;h++){
                  if(i-h<0||j+h>=n||bb[i-h][j+h]!='R'){
                      flag=0;
                      break;           
                  }        
              } 
              if(flag){
                 red=1;
                 break;
              }                
          } 
          if(red)break;
          }
          printf("Case #%d: ",test+1);
          if(red&&blue)puts("Both");
          else if(red)puts("Red");
          else if(blue)puts("Blue");
          else puts("Neither");
     }
}
