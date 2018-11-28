#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n;
    cin>>n;
    for (int cn=0;cn<n;++cn){
        int k;
        string s;
        cin>>k>>s;
        vector<int> p(k);
        for (int i=0;i<k;++i) p[i]=i;
        int ans=s.size();
        string tmp=s;
        do{
            for (int i=0;i<s.size();i+=k){
                for (int j=0;j<k;++j){
                    tmp[i+j]=s[i+p[j]];
                }
            }
            int siz=1;
            for (int i=1;i<tmp.size();++i){
                if (tmp[i]!=tmp[i-1]) ++siz;
            }
            ans<?=siz;
        }while(next_permutation(p.begin(),p.end()));
        cout<<"Case #"<<cn+1<<": "<<ans<<endl;
    }
}
