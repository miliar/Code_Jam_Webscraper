#include<string>
#include<iostream>
#include<set>
using namespace std;
int main()
{
    freopen("c:\\A-large.in","r",stdin);
    freopen("c:\\output.txt","w",stdout);
    int nn,ii;
    scanf("%d",&nn);
    for (ii=1;ii<=nn;ii++) {
        printf("Case #%d: ",ii);
        int n,m;
        set<string>st;
        scanf("%d%d",&n,&m);
        for (int i=1;i<=n;i++) {
            string s;
            cin>>s;
            int len=s.size();
            st.insert(s);
            for (int j=len-1;j>=0;j--) {
                if (s[j]=='/') {
                    if (j!=0) {
                        st.insert(s.substr(0,j));
                    }
                }
            }
        }
        string s,t;
        int ans=0;
        for (int i=1;i<=m;i++) {
            cin>>s;
            int len=s.size();
            if (st.find(s)==st.end()) {
                st.insert(s);
                ans++;
            }
            for (int j=len-1;j>=0;j--) {
                if (s[j]=='/') {
                    if (j!=0) {
                        t=s.substr(0,j);
                        if (st.find(t)==st.end()) {
                            st.insert(t);
                            ans++;
                        }
                    }
                }
            }
        }
        printf("%d\n",ans);
        
    }

}