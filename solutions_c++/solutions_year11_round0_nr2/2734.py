#include<assert.h>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>
#include<cstring>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf

char cRule[300][300];

class Rules
{
    public:
    char combine[300][300];
    bool oppose[300][300];
    Rules()
    {

    }
    void ClearRule()
    {
        int i,j;
        for(i=0;i<300;i++)
            for(j=0;j<300;j++)
                combine[i][j] = NULL, oppose[i][j] = false;
    }
    void AddCombine(char * str)
    {
        combine[str[0] ] [ str[1] ] = str[2];
        combine[str[1] ] [ str[0] ] = str[2];
    }
    bool DoesCombine(char a, char b)
    {
        if ( combine[a][b]  == NULL)
            return false;
        return true;
    }
    char GetCombine(char a, char b)
    {
        return combine[a][b];
    }
    void AddOppose(char * str)
    {
        oppose[str[0] ] [ str[1] ] = true;
        oppose[str[1] ] [ str[0] ] = true;
    }
    bool IsOppose(char a, char b)
    {
        return oppose[a][b];
    }


};
Rules myRule;
class Answer
{
    public:
    vector<char> res;
    Answer()
    {
        res.clear();
    }
    bool FoundOpposite(char ch)
    {
        int i;
        for(i=0;i<res.size();i++)
            if ( myRule.IsOppose(res[i],ch))
                return true;
        return false;
    }
    void ProcessChar(char ch)
    {
        if ( res.size()>0)
        {
            if ( myRule.DoesCombine(res.back(),ch) )
            {
                char cmb = myRule.GetCombine(res.back(),ch);
                res.pop_back();
                res.pb(cmb);
            }
            else if ( FoundOpposite(ch) )
            {
                res.clear();
            }
            else
                res.pb(ch);


        }
        else
            res.pb(ch);
    }
    void Print()
    {
        //[R, I, R]
        pf("[");
        int i;
        for(i=0;i<res.size();i++)
        {
            if ( i> 0 ) cout<<", ";
            cout<<res[i];
        }
        cout<<"]";
    }
};

int main()
{
 //freopen("sample.in","r",stdin);

 freopen("b.in","r",stdin);
 freopen("b.ans","w",stdout);

 int t;
 sf("%d",&t);
 int kase=1;
 while (t--)
 {
     myRule.ClearRule();
     int c;
     sf("%d",&c);
     while(c--)
     {
         char str[100];
         sf("%s",str);
         myRule.AddCombine(str);
     }
     int d;
     sf("%d",&d);
     while(d--)
     {
         char str[100];
         sf("%s",str);
         myRule.AddOppose(str);
     }
     int n;
     sf("%d",&n);
     char source[1000];
     sf("%s",source);
     Answer myans;
     int i;
     for(i=0;i<n;i++)
     {
         myans.ProcessChar(source[i]);
     }
     pf("Case #%d: ",kase++);
     myans.Print();
     cout<<endl;

 }
 return 0;
}
