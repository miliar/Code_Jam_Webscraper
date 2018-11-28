#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

#define INF 1000000000

using namespace std;

int main(){
    int n;
    cin>>n;
    for (int cn=0;cn<n;++cn){
        int ns;
        cin>>ns;
        map<string,int> m;
        int cnt=0;
        string s;
        getline(cin,s);
        for (int i=0;i<ns;++i){
            getline(cin,s);
            if (!m.count(s)) m[s]=cnt++;
        }
        int nq;
        cin>>nq;
        vector<int> v(nq);
        getline(cin,s);
        for (int i=0;i<nq;++i){
            getline(cin,s);
            v[i]=m[s];
        }
        vector<vector<int> > dp(nq,vector<int>(ns,INF));
        if (nq>0) for (int i=0;i<ns;++i) if (i!=v[0]) dp[0][i]=0;
        for (int i=1;i<nq;++i){
            for (int j=0;j<ns;++j) if (j!=v[i]){
                for (int k=0;k<ns;++k){
                    dp[i][j]<?=dp[i-1][k]+(k!=j);
                }
            }
        }
        int ans=0;
        if (nq>0) ans=*min_element(dp[nq-1].begin(),dp[nq-1].end());
        cout<<"Case #"<<cn+1<<": "<<ans<<endl;
    }
}
