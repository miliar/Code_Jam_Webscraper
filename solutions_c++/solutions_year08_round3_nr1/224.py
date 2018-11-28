#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    int cs=0;
    int p,k,l;
    int num;
    while(t--){
        cs++;
        scanf("%d%d%d",&p,&k,&l);
        vector <int> f;
        for(int i=0;i<l;i++){
            scanf("%d",&num);
            f.push_back(num);
        }

        sort(f.begin(),f.end());
        vector<int>revf;
        for(int i=0;i<l;i++)
            revf.push_back(f[l-i-1]);

        long long ans=0;
        long long ct=1;
        for(int i=0;i<l;i++){
            ans+=(ct*revf[i]);
            if((i%k)==(k-1))ct++;
        }
        printf("Case #%d: %lld\n",cs,ans);
    }
    return 0;
}
