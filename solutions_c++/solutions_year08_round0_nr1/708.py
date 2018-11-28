#include <cstdio>
#include <string>
#include <set>
using namespace std;

set<string> st;

int main(){
    int i,j,k;
    freopen("a.out","w",stdout);
    int tn,cn=1;
    char tmp[110];
    scanf("%d",&tn);
    while(tn--){
        int s,q,ans=0;
        st.clear();
        scanf("%d",&s);
        getchar();
        for(int i=1;i<=s;i++){
            gets(tmp);
        }
        scanf("%d",&q);
        getchar();
        for(int i=0;i<q;i++){
            gets(tmp);
            st.insert(tmp);
            if(st.size()==s){
                ans++;
                st.clear();
                st.insert(tmp);
            }
        }
        printf("Case #%d: %d\n",cn++,ans);
    }
    return 0;
}
