#include <iostream>

#define TASK "B"
#define SMALL "small-attempt" 
#define NUM "1"
#define LARGE "large"

using namespace std;

int test;
int numtest;
int n;

long long d[3100][12];
bool mark[3100][12];

long long a[3100];
long long price[3100]; 
int m[3100];
int l[3100];
int r[3100];
long long ans;
int list;
long long INF=1000000000000000LL;


long long calc(int ver,int cnt){
    if (cnt>a[ver]) return INF;
    if (ver<list){
        return 0;        
    }
    if (mark[ver][cnt]) return d[ver][cnt];
    mark[ver][cnt]=1;
    long long res=INF;
    long long cur = price[ver]+calc(l[ver],cnt)+calc(r[ver],cnt);        
    if (cur<res) res = cur;
    //cur = price[ver]+calc(l[ver],cnt+1)+calc(r[ver],cnt);        
    //if (cur<res) res = cur;
    cur = calc(l[ver],cnt+1)+calc(r[ver],cnt+1);
    if (cur<res) res= cur;
    d[ver][cnt]=res;
    return res;        
}

void readinput(){
    scanf("%i",&n);	 
    for (int i=0;i<(1<<(n+1));i++)
        for (int j=0;j<=n;j++) mark[i][j]=0;
    for (int i=0;i<=(1<<(n+1));i++){
        a[i]=0;
        price[i]=0;    
    }
    
    for (int i=0;i<(1<<n);i++){
        int num;
        scanf("%i",&num);
        a[i]=num;    
    }
    int cur=(1<<n);
    int big = (1<<(n+1))-2;
    for (int i=cur;i<=big;i++){
        int num;
        scanf("%i",&num);
        price[i]=num;    
    }   
    
    
    list = cur;
    //cout<<big<<" "<<cur<<endl;
    for (int i=0;i<big;i++){
        if (i&1){
            r[cur]=i;
            cur++;
        }else{
            l[cur]=i;    
        }        
    }
    cur=(1<<n);
    for (int i=cur;i<=big;i++){
        //printf("%i -> %i and %i\n",i,l[i],r[i]);    
        a[i]=min(a[l[i]],a[r[i]]);   
        //cout<<price[i]<<" "<<a[i]<<endl;
             
    }
    ans = calc(big,0);     
      
}

void writeoutput(){
	printf("Case #%i: ",numtest);
    cout<<ans<<endl;
}


void solve(){
               
}

int main(void){
	//freopen(TASK"-"SMALL""NUM".in","r",stdin);
	//freopen(TASK"-"SMALL""NUM".out","w",stdout);
	freopen(TASK"-"LARGE".in","r",stdin);
	freopen(TASK"-"LARGE".out","w",stdout);
	scanf("%i\n",&test);
    	
	for (int q=0;q<test;q++){
        numtest=q+1;
		readinput();
		solve();
		writeoutput();
	}

	return 0;
}
