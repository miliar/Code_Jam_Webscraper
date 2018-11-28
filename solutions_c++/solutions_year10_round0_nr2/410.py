#include<iostream>
#include<ios>
#include<fstream>
#include<string>
#include<sstream>
#include<algorithm>
using namespace std;
#define CLR(x,y) memset((x) ,y ,sizeof(x))
typedef long long LL;
const int N = 103; 
int data[N],cha[N];

int gcd(int a,int b) {
    if(b==0) return a;
    else return gcd(b, a%b);
}

int main() {
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small-attempt3.out","w",stdout);
    int t,n,cas;
    while(scanf("%d",&t)!=EOF) {
        cas=1;
        while(t--) {
            scanf("%d",&n);
            for(int i=0; i<n; i++) scanf("%d",&data[i]);
            /*if(n==2) { 
                printf("Case #%d: %d\n",cas++, gcd(data[0],data[1])==1?0:);
                continue;   
            }*/
            sort(data, data+n);
            for(int i=0; i<n-1; i++)
                cha[i]=data[i+1]-data[i];
            int tmp=cha[0];
            for(int i=1; i<n-1; i++) {
                tmp=gcd(tmp, cha[i]);
            }
            printf("Case #%d: %d\n",cas++, (data[0]%tmp)==0?0:tmp-data[0]%tmp);
        }
    }
    
    //system("pause");
    return 0;
}
