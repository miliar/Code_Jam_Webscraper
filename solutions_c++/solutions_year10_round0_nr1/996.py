#include<iostream>
#include<ios>
#include<fstream>
#include<string>
#include<sstream>
#include<algorithm>
using namespace std;
#define CLR(x,y) memset((x) ,y ,sizeof(x))

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    //FILE* fs=fopen("A-small-attempt0.out","w+");
    int cas=1;
    int n,k,ans,t;
    while(scanf("%d",&t)!=EOF) {
        cas=1;
        while(t--) {
            scanf("%d%d",&n,&k);
            k=k%(1<<n);
            if(k==(1<<n)-1) printf("Case #%d: ON\n",cas++);
            else printf("Case #%d: OFF\n",cas++);
        }
    }
    //system("pause");
    return 0;
}
