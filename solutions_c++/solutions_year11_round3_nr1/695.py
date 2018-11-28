#include<iostream>

using namespace std;

int T;
int n,m;
string s[100];
char out[100][100];

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
    cin>>T;
    for (int ii=1;ii<=T;ii++) {
        cout<<"Case #"<<ii<<":\n";
        cin>>n>>m;
        for (int i=1;i<=n;i++)
            cin>>s[i];
        bool flag=true;
        for (int i=1;i<=n;i++)
            for (int j=0;j<m;j++) {
                if (!flag) break;
                if (s[i][j]=='.') {s[i][j]='.';continue;}
                if (s[i][j]=='#') {
                   if (i>=n || j>=m-1 || s[i][j+1]!='#' || s[i+1][j]!='#' || s[i+1][j+1]!='#') {flag=false;break;}
                   s[i][j]='/';
                   s[i][j+1]='\\';
                   s[i+1][j]='\\';
                   s[i+1][j+1]='/';
                   
                }
            }
        if (!flag) cout<<"Impossible\n";
           else {
                for (int i=1;i<=n;i++) {
                    for (int j=0;j<m;j++)
                        cout<<s[i][j];
                    cout<<endl;
                }
           }
    }
    
    return 0;
}
