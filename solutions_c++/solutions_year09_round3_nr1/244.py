#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int n,cnt=0;
vector<int> v;
map<char,int> m;

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&n);
    for (int i=0; i<n; i++) {
        v.clear();
        char tc[100];
        scanf("%s",tc);
        string str=tc;
        m.clear(); cnt=0;
        for (int j=0; j<str.length(); j++)
            if (m.find(str[j])==m.end()) {
               if (cnt==0) { m[str[j]]=1; cnt=1; }
                  else if (cnt==1) { m[str[j]]=0; cnt=2; }
                  else { m[str[j]]=cnt; cnt++; }
               v.push_back(m[str[j]]);
               }
               else v.push_back(m[str[j]]);
        cnt=max(2,cnt);
        /*
        printf("%d\n",cnt);
        for (int j=0; j<str.length(); j++)
            printf("%d ",v[j]);
        printf("\n");
        */
        long long ans=0,nowb=1;
        for (int j=v.size()-1; j>=0; j--) {
            ans+=nowb*v[j];
            nowb*=cnt;
            }
        printf("Case #%d: ",i+1);
        cout << ans << endl;
        }
    
}
