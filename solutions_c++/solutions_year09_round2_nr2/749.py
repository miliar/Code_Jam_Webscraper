#include <iostream>
#include <algorithm>
using namespace std;
int a[100];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int N;
    char c;
    scanf("%d",&N);
    scanf("%c",&c);
    for(int I = 1;I <= N;++I){
        int n(0);
        while(scanf("%c",&c) != EOF && c != '\n')
            a[n++] = c - '0';
        bool flag(0);
        for(int i = 0;i < n-1 && !flag;++i)
            if(a[i] != a[i+1]) flag = 1;
        if(!flag){
            a[n] = 0;
            if(n > 1) swap(a[n],a[1]);
            ++n;
        }
        else
        if(!next_permutation(a,a+n)){
            sort(a,a+n);
            int i;
            for(i = 0;i < n && a[i] == 0;++i);
            swap(a[0],a[i]);
            for(i = n;i > 1;--i) a[i] = a[i-1];
            a[1] = 0;
            ++n;
        }
        printf("Case #%d: ",I);
        for(int i = 0;i < n;++i) printf("%d",a[i]);
        puts("");
    }
}
