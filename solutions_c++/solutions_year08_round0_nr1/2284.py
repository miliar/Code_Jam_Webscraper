#include <string>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
int tst()
{
    int s,q;
    scanf("%d\n",&s);
    vector<string> S;
    vector<string> Q;
    char tmp[1000];
    for(int i=0;i<s;i++)
    {
        gets(tmp);
        S.push_back(string(tmp));
    }
    scanf("%d\n",&q);
    for(int i=0;i<q;i++)
    {
        gets(tmp);
        Q.push_back(string(tmp));
    }
    map<string,int> m;
    for(int i=0;i<S.size();i++)
        m[S[i]] = i;
    vector<int> ss(s);
    vector<int> qq(q);
    for(int i=0;i<s;i++)ss[i]=m[S[i]];
    for(int i=0;i<q;i++)qq[i]=m[Q[i]];
    vector<vector<int> > wyst(s,vector<int>(1,q));
    for(int i=q-1;i>=0;i--)
        wyst[qq[i]].push_back(i);
    int num = -1;
    int ans=0;
    while(num<q)
    {
        for(int i=0;i<s;i++)
            num = max(num,wyst[i].back());
        for(int i=0;i<s;i++)
            while(wyst[i].back()<num)
                wyst[i].pop_back();
        ans++;
    }
    return ans-1;

}
int main()
{
    int n;
    scanf("%d\n",&n);
    for(int i=0;i<n;i++)
    {
        printf("Case #%d: %d\n",i+1,tst());
    }

}
