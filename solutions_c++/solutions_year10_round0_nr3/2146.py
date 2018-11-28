#include <iostream>

#define TASK "C"
#define SMALL "small-attempt" 
#define NUM "0"
#define LARGE "large"

using namespace std;

int test;
int numtest;
int r,k,n;
long long ans;
#define N 1001
int g[N];
int next[N];
int cnt[N];
int items[10000];



void readinput(){
	scanf("%i %i %i",&r,&k,&n);
    for (int i=0;i<n;i++) scanf("%i",&g[i]);    
}

void writeoutput(){
	printf("Case #%i: ",numtest);
    cout<<ans<<endl;
	
}

void solve(){
	ans=0;
	for (int i=0;i<n;i++){
        int cur = 0;
        int all=0;        
        int j=i;  
        while (all<n && cur+g[j]<=k){
            cur+=g[j];
            all++;
            j++;
            if (j>=n) j=0;       
        }
        cnt[i]=cur;
        next[i]=j;  
    }
    int pos = 0;
    for (int i=0;i<10000;i++){
        items[i]=pos;
        pos=next[pos];
    }    
    if (r<10000){
        for (int i=0;i<r;i++){
            ans+=cnt[items[i]];        
        }
    }else{
        for (int i=0;i<10000;i++){
            ans+=cnt[items[i]];        
        }
        int loopsize = 1000000;
        for (int i=1;i<1000;i++){
            int flag = true;
            for (int j=1;j<=i;j++){
                if (items[10000-j]!=items[10000-i-j] || items[10000-j]!=items[10000-2*i-j]){
                    flag = false;
                    break;   
                }                
            }
            if (flag){
                loopsize = i;
                break;       
            }
        }
        r-=10000;
        long long cntloops = r/loopsize;
        long long loopcost=0;
        for (int i=0;i<loopsize;i++){
            loopcost += cnt[items[10000-1-i]];    
        }
        ans+=(cntloops*loopcost);
        r%=loopsize;
        for (int i=0;i<r;i++){
            ans+=cnt[items[10000-loopsize+i]];    
        }

    }
}

int main(void){
	freopen(TASK"-"SMALL""NUM".in","r",stdin);
	freopen(TASK"-"SMALL""NUM".out","w",stdout);
	//freopen(TASK"-"LARGE".in","r",stdin);
	//freopen(TASK"-"LARGE".out","w",stdout);
	scanf("%i\n",&test);
	for (int q=0;q<test;q++){
        numtest=q+1;
		readinput();
		solve();
		writeoutput();
	}

	return 0;
}
