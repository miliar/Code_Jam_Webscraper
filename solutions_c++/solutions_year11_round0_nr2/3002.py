#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
int trans[28][28];
vector <int > pret[28];
string s;
int H=1-'A';
int a[28];
void nula()
{
    for (int i=0; i<28;i++)
     a[i]=0;
}
vector <int > res;
int T,i,j,c,d,n,t;
bool flag;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (t=1; t<=T;t++)
    {
        for (i=0;i<28;i++)
         for (j=0; j<28;j++)
            trans[i][j]=0;
         for (i=0; i<28; i++)
            pret[i].clear();
        cin>>c;
        for (i=0; i<c;i++)
        {
         cin>>s;
         trans[s[0]+H][s[1]+H]=trans[s[1]+H][s[0]+H]=s[2]+H;
        }
        cin>>d;
        for (i=0; i<d;i++)
        {
         cin>>s;
         pret[s[0]+H].push_back(s[1]+H);
         pret[s[1]+H].push_back(s[0]+H);
        }
        res.clear();
        cin>>n;
        cin>>s;
        nula();
       for (i=0; i<n;i++)
       {
        if (res.size()==0)
        {
            res.push_back(s[i]+H);
            a[s[i]+H]++;
            continue;
        }
        if (trans[res[res.size()-1]][s[i]+H])
        {
            a[res[res.size()-1]]--;
            a[trans[res[res.size()-1]][s[i]+H]]++;
         res[res.size()-1]=trans[res[res.size()-1]][s[i]+H];
         continue;
        }
        flag=false;
        for (j=0; j<pret[s[i]+H].size();j++)
         if (a[pret[s[i]+H][j]]!=0)
         {
             nula();
             res.clear();
             flag=true;
         }
         if (flag) continue;
         res.push_back(s[i]+H);
         a[s[i]+H]++;
       }
       cout<<"Case #"<<t<<": [";
       for (i=0; i<res.size();i++)
        if (i==0) cout<<char(res[i]-H);
       else cout<<", "<<char(res[i]-H);
       cout<<"]"<<endl;
    }

    return 0;
}
