#include <iostream>
#define TASK "C"
#define Small "-small-attempt"
#define NUM "0"
#include <string>
#include <map>
#include <set>

using namespace std;

int test;
int n;
int a[2000];
int ans;

void readinput(){
    scanf("%i",&n);
    for (int i=0;i<n;i++){
        scanf("%i",&a[i]);    
    }    
}

void solve(){
    sort(a,a+n);
    int val = 0;
    int sum = 0;
    for (int i=0;i<n;i++){
        val^=a[i];    
        sum+=a[i];
    }
    if (val){
        ans = -1; 
    }else{
        ans = sum-a[0];    
    }
}

void writeoutput(int t){
    printf("Case #%i: ",t+1);        
    if (ans>0){
        cout<<ans;    
    }else{
        cout<<"NO";
    }
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
