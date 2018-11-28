#include<iostream>
using namespace std;

typedef __int64 LL;

int main() {
  //  freopen("B-large.in","r",stdin);
  //  freopen("B-bigout.txt","w",stdout);
    
    int a , b, c;
    int test;
    scanf("%d",&test);
    for( int tc = 1; tc <= test;tc++ ) {
        scanf("%d%d%d",&a,&b,&c);
        int tot = 0;
        for(LL i = a; i < b; ) {
            tot++;
            i *= c;    
            //cout<<i<<endl;
        }
        //cout<<tot<<endl;
        int ans = 0;
        c = 2;
        while( tot != 1) {
            ans++;
            if( tot%c == 0) tot /= c;
            else   tot = tot/c+1;
        }
        printf("Case #%d: %d\n",tc,ans);
    }
    return 0;
}

/*
5
50 700 2
19 57 3
1 1000 2
1 1000000000 10

*/
