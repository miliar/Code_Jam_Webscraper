#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
using namespace std;

vector<string> v;
int l,d,n;

int main() {
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    scanf("%d%d%d",&l,&d,&n);
    for (int i=0; i<d; i++) {
        string s; char ts[5000];
        scanf("%s",ts);
        s=ts;
        v.push_back(s);
        }
    for (int i=0; i<n; i++) {
        string str; char ts[5000];
        scanf("%s",ts);
        str=ts;
        set<char> s[20];
        for (int j=0; j<l; j++)
            if (str[0]=='(') {
               str.erase(str.begin());
               do {
                   s[j].insert(str[0]);
                   str.erase(str.begin());
                   } while (str[0]!=')');
               str.erase(str.begin());
               }
               else {
               s[j].insert(str[0]);
               str.erase(str.begin());
               }
        int cnt=0;
        for (int j=0; j<d; j++) {
            for (int k=0; k<l; k++)
                if (s[k].find(v[j][k])==s[k].end()) goto bye;
            cnt++;
            bye: ;
            }
        printf("Case #%d: %d\n",i+1,cnt);
        }
    
}
