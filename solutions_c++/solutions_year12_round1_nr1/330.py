#include <iostream>
#include <cstdio>

#include <vector>
#include <cstring>
#include <queue>
#include <cmath>

#define EPS 0.000001
#define INF 2000000000

#define y1 jhsdfdasdg
#define y2 sjgfkagaef

#define ABS(a) ((a)<0?(-(a)):(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))

using namespace std;

void sol(){
    int A, B;
    double p[100500];
    int i,j;
    cin>>A>>B;
    for(i=0;i<A;++i) cin>>p[i];
    double res=B+2,tr, P=1.0;
    for(int k=A;k>=0;--k){
        tr=(k+B-A+1+k)*P+(k+B-A+1+k+B+1)*(1-P);
        if(tr<res) res=tr;
        P*=p[A-k];
    }
    printf("%lf",res);
}

int main(){

    freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

    int T;
    cin>>T;
    char str[100];
//    cin.getline(str,99);
    for(int ii=1;ii<=T;++ii){
//        cout<<"Case #"<<ii<<": ";
        printf("Case #%d: ",ii);
        sol();
        printf("\n");
    }

    return 0;
}
