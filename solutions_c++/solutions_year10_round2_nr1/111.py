#include<iostream>
#include<string>
#include<vector>

using namespace std;


vector <string> DIR[256];
void DIVIDE(string &S,vector<string> &V)
{
     V.clear();
     string Last="";
     for (int i=0;i<S.size();++i)
     {
         if (S[i]=='/')
         {
             if (Last!="") V.push_back(Last);
             Last="";
         } else
         Last+=S[i];
     }
     if (Last!="") V.push_back(Last);        
}
int COMPARE(vector<string> &A,vector<string> &B)
{
    int t=0;
    while (t<A.size() && t<B.size() && A[t]==B[t]) ++t;
    return t;    
}
int Solve()
{
    int n,m;
    cin>>n>>m;
    string tmp;
    for (int i=0;i<n;++i)
    {
        cin>>tmp;
        DIVIDE(tmp,DIR[i]);
    }
    for (int i=0;i<m;++i)
    {
        cin>>tmp;
        DIVIDE(tmp,DIR[n+i]);
    }    
    int Ans=0;
    for (int i=0;i<m;++i)
    {
        int MAX=0;
        for (int j=0;j<i+n;++j)
            MAX=max(MAX,COMPARE(DIR[j],DIR[i+n]));
            Ans+=int(DIR[i+n].size())-MAX;
    }
    return Ans;
}

int main()
{
    freopen("A-large.in","r",stdin);

    freopen("A-Ans-large.txt","w",stdout);
    int T;
    cin>>T;
    for (int i=1;i<=T;++i)
        printf("Case #%d: %d\n",i,Solve());    
    return 0;
}
