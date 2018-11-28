#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <algorithm>

using namespace std;
//#define ONLINE_JUDGE
#define PB push_back
#define MP make_pair
#define CLR(x,y) memset((x),y,sizeof(x))
#define rep(i,n) for(int i=0; i<(n); i++)
#define forr(i,a,b) for(int i=(a);i<=(b);i++)

int gcd(int x,int y) {
    if(y==0) return x;
    return gcd(y,x%y);
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    #endif

    int tt, cas = 1;
    scanf("%d", &tt);
    for(cas=1; cas<=tt; cas++) {
        //To-Do
        int Pd,Pg,N;
        char str1[1000],str2[1000];
        scanf("%s%s",str1,str2);
        Pd=0;
        for(int i=0; i<strlen(str2); i++) {
            Pd=Pd*10+str2[i]-'0';   
        }
        N=0;
        for(int i=0; i<strlen(str1)&&i<4; i++) {
            N=N*10+str1[i]-'0';      
        }
        if(strlen(str1)>4) N=N*10+1;
        scanf("%d",&Pg);
        printf("Case #%d: ",cas);    
        int co=gcd(Pd,100);
        int A=Pd/co, B=100/co;
        
        if(N<B) {
            printf("Broken\n");
            continue;   
        }
        if(Pd==Pg) {
            printf("Possible\n");
            continue;
        }
        if(Pd==0||Pg==0) {
            printf("Broken\n");
            continue;   
        }
        if(Pg==100&&Pd!=100) {
            printf("Broken\n");            
        }
        else {
            printf("Possible\n");
        }
    }
    //system("pause");
    return 0;
}
