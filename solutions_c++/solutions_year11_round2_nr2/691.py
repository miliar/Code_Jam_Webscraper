#include <iostream>
#include <cmath>
#define TASK "B"
#define Small "-small-attempt"
#define NUM "1"
#include <string>
#include <map>
#include <set>

using namespace std;

#define N 300

int test;
int x[N];
int cnt[N];
int d,n;
double ans;

void readinput(){
    scanf("%i %i",&n,&d);
    for (int i=0;i<n;i++){
        scanf("%i %i",&x[i],&cnt[i]);
    }   
}

bool good(double tim){
    double leftinf = -2e12;
//    printf("%.5lf\n",tim);
    for (int i=0;i<n;i++){        
        double newleft = x[i]-tim;

        if (newleft>leftinf){
            leftinf = newleft;    
        }        
        //printf("! %.6lf\n",newleft);
        if (x[i]-leftinf>tim+1e-7) return false;
        if (leftinf+d*(cnt[i]-1)-x[i]>tim+1e-7) return false;
        leftinf+=d*(cnt[i]);
        
    }   
    return true; 
}

void solve(){
    ans = 0;
    double l=0;
    double r=1e12+1;
    while (r-l>1e-7){
        double m = (l+r)*0.5;
        if (good(m)){
            r = m;    
        }else{
            l = m;    
        }
    }

    ans = l;
}

void writeoutput(int t){
    printf("Case #%i: ",t+1);        
    printf("%.6lf",ans);
    printf("\n");
}

int main(void){
    //freopen("input.txt","r",stdin);    
    freopen(TASK""Small""NUM".in","r",stdin);
    //freopen(TASK"-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%i\n",&test);
    for (int i=0;i<test;i++){
        readinput();
        solve();
        writeoutput(i);
    }
    
    return 0;    
}
