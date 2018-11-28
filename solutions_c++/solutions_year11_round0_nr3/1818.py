#include <cstdio>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main(){
    int nn;
    scanf("%d",&nn);
    for(int ix=1;ix<=nn;ix++){
        int n;
        scanf("%d",&n);
        vector<int> bitnum(32,0);
        vector<long long int> inss(n);
        for(int i=0;i<n;i++){
            int ins;
            scanf("%d",&ins);
            inss[i]=(long long int)ins;
            for(int j=0;j<32;j++){
                if((ins&(1<<j))!=0) bitnum[j]++;
            }
        }
        bool is=true;
        for(int i=0;i<32;i++){
            if(bitnum[i]%2!=0) is=false;
        }
        if(is) printf("Case #%d: %lld\n",ix,accumulate(inss.begin(),inss.end(),0)-*min_element(inss.begin(),inss.end()));
        else printf("Case #%d: NO\n",ix);
    }
}
