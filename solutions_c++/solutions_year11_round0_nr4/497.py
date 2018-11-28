#include <iostream>
#define TASK "D"
#define Small "-small-attempt"
#define NUM "1"
#include <string>
#include <map>
#include <set>

using namespace std;

int test;
int n;
int ans;
int a[2000];
bool used[12];



void readinput(){
    scanf("%i",&n);
    for (int i=0;i<n;i++){
        scanf("%i",&a[i]);   
    }   
}

void solve(){
    ans=0;
    for (int k=0;k<n;k++){
                used[k]=0;    
            }     
            for (int k=0;k<n;k++){
                if (!used[k]){
                    int len = 0;
                    int t = k;
                    while (!used[t]){
                        used[t]=1;
                        len++;
                        t=a[t]-1;     
                    }
                    if (len>=2) ans+=len;          
                }                    
            }      
}

void writeoutput(int t){
    printf("Case #%i: ",t+1);        
    printf("%.6lf",ans+0.0);
    printf("\n");
}

int main(void){
    //freopen("input.txt","r",stdin);    
    //freopen(TASK""Small""NUM".in","r",stdin);
    freopen(TASK"-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%i\n",&test);
    for (int i=0;i<test;i++){
        readinput();
        solve();
        writeoutput(i);
    }
    
    return 0;    
}
