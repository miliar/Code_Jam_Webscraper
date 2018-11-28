#include <cstring>
#include <cstdio>
#include <set>

int T;
int A,B;
int p10[] = { 1, 10,100,1000,10000,100000,1000000,10000000 };
using namespace std;
inline int move(int x,int i,int length) {
    x += (x % p10[i]) * p10[length];
    x /= p10[i];
    return x;
}

inline long long count(int x) {
    set<int> resultset;
    long long result=0;
    char buff[20];
    sprintf(buff,"%d",x);
    int length = strlen(buff);
    for(int i=1;i<length;i++) {
        int r = move(x,i,length);
        if(r>x && r <= B && r>=A && buff[length - i]!='0' && resultset.find(r)==resultset.end()){
        //    printf("%d %d\n",x,r);
            result++;
            resultset.insert(r);
        }
    }
    return result;
}

int main() {
    long long sum=0;
    scanf("%d",&T);
    for(int k=0;k<T;k++) {
        sum = 0;
        scanf("%d %d",&A,&B);
        for(int i=A;i<=B;i++) {
            sum+=count(i);
        }
        printf("Case #%d: %lld\n",k+1,sum);
    }
}