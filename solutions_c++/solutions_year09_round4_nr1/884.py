#include <iostream>

using namespace std;


const int N = 100;
char m[N][N];
int a[N];
int n;

void doTest(){
    scanf("%d",&n);
    memset(m,0,sizeof(m));
    for (int i = 0; i < n; i++)
        scanf("%s",m[i]);        
    for (int i = 0; i < n; i++)
        a[i] = -1;
    for (int i = 0; i < n; i++){        
        for (int j = n - 1; j >= 0; j--){                        
            if (m[i][j] == '1'){                
                a[i] = j;
                break;
            }
        }
    }    
    
    int ans = 0;
    for (int i = 0; i < n; i++){
        for (int j = i; j < n; j++){
            if (a[j] <= i){
                ans += (j-i);  
                for (int k = j; k > i; k--)
                    swap(a[k],a[k-1]);
                break;
            }
        }
    }

    printf("%d\n",ans);
}

int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int i = 0; i < T; i++){
        printf("Case #%d: ",i+1);
        doTest();
    }

    return 0;
}