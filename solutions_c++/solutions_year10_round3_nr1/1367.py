#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

     int a[1000],b[1000];
     int ac[10],bc[1000][1000];


int sol(int i){
     int j,k,n,count;
     
     scanf("%d",&n);
     
     for(j=0;j<n;j++){
         scanf("%d %d",&a[j],&b[j]);                                  
 
     }
 
     for(k=0;k<n;k++){
        for(j=0;j<n;j++){
            bc[j][k]=-1;
        }                 
     }
     
     count=0;
     
     for(j=0;j<n;j++){
          
           if(a[j]<b[j]){
          
              for(k=0;k<n;k++){
                               
                 if(a[j]<a[k] && b[j]>b[k] && j!=k && bc[k][j]==-1){

                    count++;             
                    bc[k][j]=1;
                 }               
                                
              }
           }
           else if(a[j]>b[j]){
          
              for(k=0;k<n;k++){
                 if(a[j]>a[k] && b[j]<b[k] && j!=k && bc[j][k]==-1){
                   count++;             
                   bc[j][k]=1;
                 }                                
              }
           }
                         
     }
     
     printf("Case #%d: %d\n",(i+1),count);
     
}

int main(void){

	int t,i;
	scanf("%d",&t);
    for(i=0;i<t;i++){
      sol(i);
    }
	return 0;

}
