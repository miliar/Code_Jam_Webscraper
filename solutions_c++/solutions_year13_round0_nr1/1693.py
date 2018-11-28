#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
#define FOR(i,c,n) for(int i=(c);(i)<(n);++(i))
#define FR(i,n) FOR(i,0,n)


string s[4];
bool check(char ch)
{
    FR(i,4)
    {
        int sum=0;
        FR(j,4) if(s[i][j]==ch || s[i][j]=='T') sum++;
        if(sum==4) return true;
    }
    FR(j,4)
    {
        int sum=0;
        FR(i,4) if(s[i][j]==ch || s[i][j]=='T') sum++;
        if(sum==4) return true;
    }
    int sum;
    sum=0;FR(i,4) if(s[i][i]==ch || s[i][i]=='T') sum++;if(sum==4) return true;
    sum=0;FR(i,4) if(s[i][3-i]==ch || s[i][3-i]=='T') sum++;if(sum==4) return true;
    return false;
}
bool isComplete()
{
    FR(i,4) if(s[i].find('.')!=string::npos) return false;
    return true;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;cin>>t;
    for(int i=1;i<=t;++i)
    {
        printf("Case #%d: ",i);
        for(int j=0;j<4;++j)cin>>s[j];
        if(check('X')) cout<<"X won"<<endl;
        else if(check('O')) cout<<"O won"<<endl;
        else if(isComplete()) cout<<"Draw"<<endl;
        else cout<<"Game has not completed"<<endl;
    }
    return 0;
}
