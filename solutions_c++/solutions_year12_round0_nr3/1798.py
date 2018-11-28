#include <cstdio>
#include <sstream>
#include <set>
#define MP make_pair
using namespace std;
int main(){
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++){
        printf("Case #%d: ",i+1);
        int A,B;
        scanf("%d%d",&A,&B);
        int ret=0;
        set<pair<int,int> > hoge;
        for(int j=A;j<=B;j++){
            stringstream ns;
            ns<<j;
            string n=ns.str();
            for(int k=1;k<n.size();k++){
                if(j>=1000000 && n[k]!='1' && n[k]!='2') continue;
                if(n[k]=='0') continue;
                int ndnum=0,sz=n.size(),l;
                for(l=k;l<sz;l++){
                    ndnum*=10;
                    ndnum+=n[l]-'0';
                }
                for(l=0;l<k;l++){
                    ndnum*=10;
                    ndnum+=n[l]-'0';
                }
                if(j!=ndnum && A<=ndnum && ndnum<=B){
                    int a=j,b=ndnum;
                    if(a>b) swap(a,b);
                    hoge.insert(MP(a,b));
                }
            }
        }
        printf("%d\n",hoge.size());
    }
}
