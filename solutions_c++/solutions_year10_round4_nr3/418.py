#include <iostream>

#define TASK "C"
#define SMALL "small-attempt" 
#define NUM "1"
#define LARGE "large"

using namespace std;

#define N 1100

int test;
int numtest;
int n;

int x_1[N];
int y_1[N];
int x_2[N];
int y_2[N];

long long ans;

bool g[N][N];
bool g2[N][N];
bool used[N];
int s[N];


void readinput(){
    ans=0;
    for (int i=0;i<101;i++)
    for (int j=0;j<101;j++) g[i][j]=0;
    scanf("%i",&n);	  
    for (int i=0;i<n;i++){
        scanf("%i %i %i %i",&x_1[i],&y_1[i],&x_2[i],&y_2[i]);  
        for (int a = x_1[i];a<=x_2[i];a++)
            for (int b = y_1[i];b<=y_2[i];b++){
                g[a][b]=1;    
            }          
    }       
    
}

void writeoutput(){
	printf("Case #%i: ",numtest);
    cout<<ans-1<<endl;
}



void solve(){
    int minx = 101;
    int maxx = 0;
    int miny = 101;
    int maxy = 0;
    for (int i=0;i<n;i++){
        if (x_1[i]<minx) minx = x_1[i];    
        if (x_2[i]>maxx) maxx = x_2[i];    
        if (y_1[i]<miny) miny = y_1[i];    
        if (y_2[i]>maxy) maxy = y_2[i];                            
        
        if (x_2[i]<minx) minx = x_2[i];    
        if (x_1[i]>maxx) maxx = x_1[i];    
        if (y_2[i]<miny) miny = y_2[i];    
        if (y_1[i]>maxy) maxy = y_1[i];
    }
    //cout<<minx<<" "<<maxx<<" "<<miny<<" "<<maxy<<endl;
    while (true){
        
        /*for (int i=minx;i<=maxx;i++){
            for (int j=miny;j<=maxy;j++){
                if (g[i][j]) printf("1"); else printf("0");    
            }
            printf("\n");
        }
        printf("\n");*/
        
        ans++;
        int cnt=0;
        for (int i=minx;i<=maxx;i++){
            for (int j=miny;j<=maxy;j++){
                if (g[i][j]){
                    cnt++;
                    if (!g[i-1][j] && !g[i][j-1]) g2[i][j]=0;else g2[i][j]=1;     
                }else{
                    if (g[i-1][j] && g[i][j-1]){
                        g2[i][j]=1;
                        cnt++;    
                    }else{
                        g2[i][j]=0;    
                    }    
                }    
            }    
        }
        if (cnt==0) break;
        for (int i=minx;i<=maxx;i++)
            for (int j=miny;j<=maxy;j++){
                g[i][j]=g2[i][j];
                g2[i][j]=0;    
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
