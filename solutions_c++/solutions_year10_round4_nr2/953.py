#include <vector>
#include <algorithm>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;
int key[((1<<10)+10)]={0};
int val[10][((1<<10)+1)]={0};
int main()
{
    //	freopen("D:\\GCJ 2010\\B-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2010\\B-small-attempt0.out","w",stdout);
    freopen("D:\\GCJ 2010\\B-small-attempt4.in","r",stdin);freopen("D:\\GCJ 2010\\B-small-attempt4.out","w",stdout);
    //	freopen("D:\\GCJ 2010\\B-large.in","r",stdin);freopen("D:\\GCJ 2010\\B-large.out","w",stdout);
    int testcase;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        int n,t,flag1,flag2,asw,res=0;
        cin>>n;
        int s=(1<<n);
        for(int i=0;i<s;i++)
        {
            scanf("%d",&t);
            key[i]=n-t;
            res+=(n-t);
        }
        for(int i=n-1;i>=0;i--)
        {
            for(int j=0;j<(1<<i);j++)
            {
                cin>>val[i][j];
                //  scanf("%d",&val[i][j]);
            }
        }
        asw=0;flag1=0;flag2=0;        
        printf("Case #%d: ",caseId);
        if(res==0)cout<<0<<endl;
        else
        {
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<(1<<i);j++)
                {
                    flag1=0;flag2=0;
                    for(int m=((s/((1<<i)))*j);m<(s/(1<<i))*(j+1);m++)
                    {
                        if(key[m]>0){key[m]--;flag1=1;}
                        if(key[m]>0)flag2=1;
                    }
                    if(flag1==1)asw++;
                    if(flag2==0){for(int i1=0;i1<s;i1++){if(key[i1]>0){i1=s;flag2=1;}}}
                    if(flag2==0){i=n;}
                }
            }
            cout<<asw<<endl;
        }
    }
    return 0;
}