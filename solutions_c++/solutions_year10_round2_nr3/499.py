#include <iostream>

#define TASK "C"
#define SMALL "small-attempt" 
#define NUM "1"
#define LARGE "large"

using namespace std;

int test;
int numtest;
int n;

#define N 505
#define MOD 100003

bool mark[N][N];
long long d[N][N];
long long c[N][N];


void readinput(){
    scanf("%i",&n);	   
}

void writeoutput(){
	printf("Case #%i: ",numtest);
    long long ans = 0;
    for (int i=1;i<n;i++) ans=(ans+d[n][i])%MOD;
	cout<<(ans+1)%MOD<<endl;
}

long long calc(int num,int pos){
    
    //if(num<1) return 0;
    if (pos==1) return 1;
    if (mark[num][pos]) return d[num][pos];
    mark[num][pos]=true;
    long long res=0;
    for (int i=1;i<=pos-1;i++){
        if (pos-i-1>num-pos-1) continue;
        long long cur = (calc(pos,i)*c[num-pos-1][pos-i-1])%MOD;        
        res=(res+cur)%MOD;
    }            
    //printf("%i %i = %i\n",num,pos,(int)res);
    d[num][pos]=res;
    return res;    
}

void solve(){

}

int main(void){
	//freopen(TASK"-"SMALL""NUM".in","r",stdin);
	//freopen(TASK"-"SMALL""NUM".out","w",stdout);
	freopen(TASK"-"LARGE".in","r",stdin);
	freopen(TASK"-"LARGE".out","w",stdout);
	scanf("%i\n",&test);
    memset(mark,0,sizeof(mark));
    c[0][0]=1;
    c[1][1]=c[1][0]=1;
    for (int i=2;i<=500;i++){
        for (int j=0;j<=i;j++){
            if (i==j || j==0) c[i][j]=1;
            else
            c[i][j]=(c[i-1][j]+c[i-1][j-1])%MOD;    
        }    
    }
      

	for (int i=1;i<=500;i++){
        for (int j=1;j<i;j++)
            calc(i,j);    
    }
	
	for (int q=0;q<test;q++){
        numtest=q+1;
		readinput();
		solve();
		writeoutput();
	}

	return 0;
}
