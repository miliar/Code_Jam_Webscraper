#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <sstream>
#include <string>
#include <stdio.h>
using namespace std;
int  N,M;
string W[11111];
string L[111];
bool contains[26];
bool denied[26];

bool match(string mask,string S)
{
    int i,I=mask.length();
    if(S.length()!=I) return false;

    for(i=0;i<I;i++)
        if(mask[i]!='-'&&mask[i]!=S[i])
            return false;
        else if(mask[i]=='-'&&denied[S[i]-'a'])
            return false;
    return true;
}
bool match(string mask,char a,string S)
{
    int i,I=mask.length();
    bool let=false;
    if(S.length()!=I) return false;

    for(i=0;i<I;i++)
    {
         if(mask[i]!='-'&&mask[i]!=S[i])
            return false;
        else if(mask[i]=='-'&&denied[S[i]-'a'])
            return false;
        if(S[i]==a) let=true;
    }

    return let;
}
int matchcount(string mask)
{
    int i,cnt=0;
    for(i=0;i<N;i++)
        if(match(mask,W[i]))
            cnt++;
    return cnt;
}
int matchcount(string mask,char a)
{
    int i,cnt=0;
    for(i=0;i<N;i++)
        if(match(mask,a,W[i]))
            cnt++;
    return cnt;
}



void testord(string ord)
{
    int best=0,bi=0,i,cur,j,I,cnt,cntC,k;
    string mask;

    for(i=0;i<N;i++)
    {
        mask=W[i];
        I=mask.length();
        for(j=0;j<26;j++)
        {
            denied[j]=0;
            contains[j]=0;
        }
        for(j=0;j<I;j++)
        {
            contains[mask[j]-'a']=1;
            mask[j]='-';
        }

        if(matchcount(mask)==1) cur=0;
        else
        {
            cur=0;
            cnt=matchcount(mask);
            for(j=0;j<26;j++)
            {
                cntC=matchcount(mask,ord[j]);
                denied[ord[j]-'a']=1;
                if(cntC>0)
                {



                    if(!contains[ord[j]-'a'])
                    {
                        cur++;
                        cnt=cntC;
                    }
                    for(k=0;k<I;k++)
                        if(W[i][k]==ord[j])
                            mask[k]=ord[j];
                }
            }

        }
        //cout<<W[i]<<" "<<cur<<endl;
        if(cur>best)
        {
            best=cur;
            bi=i;
        }
    }

    cout<<" "<<W[bi];
}
void test()
{
    cin>>N>>M;
    int i;
    for(i=0;i<N;i++)
        cin>>W[i];
    for(i=0;i<M;i++)
        cin>>L[i];

    for(i=0;i<M;i++) testord(L[i]);

}
int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,T;
    cin>>T;
    for(i=0;i<T;i++)
    {
      cout<<"Case #"<<i+1<<":";
      test();
      cout<<endl;
    }
    return 0;
}
