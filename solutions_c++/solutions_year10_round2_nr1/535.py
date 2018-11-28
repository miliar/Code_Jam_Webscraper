#include <vector>
#include <algorithm>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;
int main()
{
    //	freopen("D:\\GCJ 2010\\A-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2010\\A-small-attempt0.out","w",stdout);
    //	freopen("D:\\GCJ 2010\\A-small-attempt1.in","r",stdin);freopen("D:\\GCJ 2010\\A-small-attempt1.out","w",stdout);
    	freopen("D:\\GCJ 2010\\A-large.in","r",stdin);freopen("D:\\GCJ 2010\\A-large.out","w",stdout);
    int testcase;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        int n,m;
        string no[101],ne[101];
        cin>>n>>m;
        for(int i=0;i<n;i++)
        {
            cin>>no[i];no[i]+="/";
        }
        for(int i=0;i<m;i++)
        {
            cin>>ne[i];ne[i]+="/";
        }
        sort(no,no+n);sort(ne,ne+m);
        printf("Case #%d: ",caseId);
        int res=0,M=999999,asw=0;
        for(int i=0;i<m;i++)
        {
            res=0,M=999999;
            if(n==0)
            {
                 for(int t=1;t<ne[i].size();t++)
                    {
                        if(ne[i][t]=='/')res++;
                    }
                 M=min(res,M);                 
            }
            for(int j=0;j<n;j++)
            {
                res=0;
                int i1=0;
                while(i1<no[j].size()&&i1<ne[i].size()&&no[j][i1]==ne[i][i1])
                {
                    i1++;
                }
                if(i1<ne[i].size())
                {
                    for(int t=i1;t<ne[i].size();t++)
                    {
                        if(ne[i][t]=='/')res++;
                    }
                }
                M=min(res,M);
            }
            M=min(res,M);

            for(int k=0;k<i;k++)
            {
                res=0;
                int i1=0;
                while(i1<ne[k].size()&&i1<ne[i].size()&&ne[k][i1]==ne[i][i1])
                {
                    i1++;
                }
                if(i1<ne[i].size())
                {
                    for(int t=i1;t<ne[i].size();t++)
                    {
                        if(ne[i][t]=='/')res++;
                    }
                }
                M=min(res,M);
            }
            M=min(res,M);
            asw+=M;
        }
        cout<<asw<<endl;
        
    }
    return 0;
}