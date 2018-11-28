#include <iostream>
using namespace std;

const string t="welcome to code jam";
const int modnum=10000;
int ret[1000][20];

main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int tot;
    cin>>tot;
    scanf("\n");
    for (int task=0;task<tot;task++)
    {
        string s;
        getline(cin,s);
        scanf("\n");
        memset(ret,0,sizeof(ret));
        for (int i=0;i<=s.length();i++)
            ret[i][0]=1;
        for (int j=1;j<=19;j++)
            for (int i=1;i<=s.length();i++)
                ret[i][j]=(ret[i-1][j]+(s[i-1]==t[j-1]?ret[i-1][j-1]:0))%modnum;
        printf("Case #%d: %04d\n",task+1,ret[s.length()][19]);   
    }
}
