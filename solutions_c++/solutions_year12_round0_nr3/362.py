#include <stdio.h>
#include <algorithm>
#include <set>
using namespace std;

int in[10];
int c;
int A,B;

int convert(int x[], int num){
    int res = 0;
    for(int i=num-1;i>=0;i--){
        res += x[i];
        if(i != 0) res *= 10;
    }
    return res;
}

typedef pair<int ,int >PII;
set<PII>S;
PII aa[500];
int mm = 0;
void solve(int x[], int num){
    int res = 0;
    int y[10];
    for(int i=1;i<num;i++){
        for(int j=0;j + i < num;j++)
            y[j] = x[i+j];
        for(int j=0;j<i;j++)
            y[num-i+j] = x[j];
        int xx = convert(x, num);
        int yy = convert(y, num);
        if(xx > yy && yy >= A && yy <= B && y[num-1]){
            S.insert(PII(xx,yy));
        }
    }
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int Test;
    scanf("%d",&Test);
    for(int t=1;t<=Test;t++){
        S.clear();
        scanf("%d %d",&A, &B);
        mm=0;
        for(int i=A+1;i<=B;i++){
            int in[10];
            int c = 0;
            int m = i;
            while(m){
                in[c++] = m % 10;
                m /= 10;
            }
            solve(in, c);      
        }
        printf("Case #%d: %d\n", t, S.size());
    }
return 0;
}
