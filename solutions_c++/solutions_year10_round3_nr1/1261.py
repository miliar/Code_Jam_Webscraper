#include<cstdio>
#include<algorithm>
using namespace std;
#define max(x,y) (x)>(y)?(x):(y)
#define min(x,y) (x)<(y)?(x):(y)

typedef struct wire{
    int left;
    int right;
}wire;

int testCase, num;
wire line[10001];

int main(){
  freopen("A-large.in", "r", stdin);
  freopen("out.out", "w", stdout);
    
    scanf("%d", &testCase);
    for(int i=1; i<=testCase; ++i){
        for(int j=0; j<10001; ++j){
            line[j].left = line[j].right = 0;
        }
        
        scanf("%d", &num);
        for(int j=0; j<num; ++j){
            scanf("%d%d", &line[j].left, &line[j].right);
            int height = max(line[j].left - line[j].right, line[j].right - line[j].left);
        }
        
        int cnt = 0;
        for(int j=0; j<num; ++j){
            for(int k=j+1; k<num; ++k){
                if(line[j].left>line[k].left){
                    if(line[j].right<line[k].right)
                        cnt++;
                }else if(line[j].left<line[k].left){
                    if(line[j].right>line[k].right)
                        cnt++;
                }
            }
        }
        
        printf("Case #%d: %d\n", i, cnt);
    }

    return 0;
}
