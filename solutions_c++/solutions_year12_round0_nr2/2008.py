#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

bool xx[33]; //may be good
bool yy[33]; //may be surprised
int zz[33];
int ww[33];

int max(int a,int b){
    return (a>b)?a:b;    
}

int max3(int a,int b,int c){
    return max(a,max(b,c));
}

int min(int a,int b){
    return (a<b)?a:b;    
}

int min3(int a,int b,int c){
    return min(a,min(b,c));
}

int a[102];

int main(void){
    //freopen("B-small-attempt0.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    
    for (int x = 0;x<=10;x++){
        for (int y =0;y<=10;y++){
            for (int z = 0;z<=10;z++){
                int t=max3(x,y,z)-min3(x,y,z);
                
                if (t<3){
                    int qq = max3(x,y,z);
                    
                    if (t==2){
                        if (ww[x+y+z]<qq) ww[x+y+z]=qq;
                        yy[x+y+z]=1;
                    }else{    
                        if (zz[x+y+z]<qq) zz[x+y+z]=qq;                    
                        xx[x+y+z]=1;    
                    }    
                }
            }    
        }    
    }
    
    int test;
    scanf("%i",&test);
    for (int z=0;z<test;z++){
        int n,s,p;
        scanf("%i %i %i",&n,&s,&p);
        for (int i=0;i<n;i++) scanf("%i",a+i);
        //sort(a,a+n);
        /*for (int i=0;i<n;i++){
            printf("%i - %i ^ %i = %i\n",a[i],xx[a[i]],yy[a[i]],zz[a[i]]);    
        }*/
        
        int ans = 0; 
        for (int i=0;i<n;i++){
            if (xx[a[i]] && zz[a[i]]>=p){
                    ans++;    
            }else{
                if (yy[a[i]] && s && ww[a[i]]>=p){
                    
                        ans++;
                        s--;    
                        
                }    
            }                    
        }   
        printf("Case #%i: ",z+1);
        printf("%i\n",ans);
    }
    
    
    return 0;    
}
