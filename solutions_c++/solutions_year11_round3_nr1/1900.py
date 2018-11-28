 #include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <string>
#include <math.h>

using namespace std;

#define fori(i,j,k) for(int i=j;i<k;i++)
#define ford(i,j,k) for(int i=j-1;i>=k;i--)
#define i64 __int64
#define ld long double
#define mp make_pair


int main()
{
    int t;
    int n,m; 
    scanf("%d",&t);
    fori(h,0,t){
    
        printf("Case #%d:\n",h+1);
        
        scanf("%d %d",&n,&m);
        
        char **a=new char*[n+1];
        fori(i,0,n){
            scanf("\n");
            a[i]=new char[m+1];
            fori(j,0,m){
                scanf("%c",&a[i][j]);
                //printf("%c",a[i][j]);
            }
            a[i][m]='.';
        }
        a[n]=new char[m+1];
        fori(i,0,m+1){
            a[n][i]='.';
        }
        
        int t=1;
        fori(i,0,n){
            fori(j,0,m){
                if(a[i][j]=='#'){
                    if((a[i+1][j]=='#')&&(a[i][j+1]=='#')&&(a[i+1][j+1]=='#')){
                        a[i][j]='/';
                        a[i+1][j]='\\';
                        a[i][j+1]='\\';
                        a[i+1][j+1]='/';
                    }
                    else{
                        printf("Impossible\n");
                        t=0;
                        i=n;
                        j=m;
                    }
                }
            }
        }
        if (t==1){
            fori(i,0,n){
                fori(j,0,m)
                    printf("%c",a[i][j]);
                printf("\n");
            }
        }
    }
    
    
    return 0;
}
