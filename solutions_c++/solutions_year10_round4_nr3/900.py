#include <vector>
#include <algorithm>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;
int key[102][102]={0};
int key1[102][102]={0};
int main()
{
    	freopen("D:\\GCJ 2010\\C-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2010\\C-small-attempt0.out","w",stdout);
    //	freopen("D:\\GCJ 2010\\C-small-attempt1.in","r",stdin);freopen("D:\\GCJ 2010\\C-small-attempt1.out","w",stdout);
    //	freopen("D:\\GCJ 2010\\C-large.in","r",stdin);freopen("D:\\GCJ 2010\\C-large.out","w",stdout);
    int testcase;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        for(int i=0;i<102;i++)
        {
            for(int j=0;j<102;j++)
            {
                key[i][j]=0;
            }
        }
        int r,x1,x2,y1,y2;
        int X1=99999999,X2=0,Y1=99999999,Y2=0;
        cin>>r;
        for(int i=0;i<r;i++)
        {
            cin>>y1>>x1>>y2>>x2;
            X1=min(X1,x1);
            X2=max(X2,x2);
            Y1=min(Y1,y1);
            Y2=max(Y2,y2);
            for(int i1=x1;i1<=x2;i1++)
            {
                for(int j1=y1;j1<=y2;j1++)
                {
                    key[i1][j1]=1;key1[i1][j1]=1;
                }
            }
        }
        int flag=1,asw=0;
        while(flag==1)
        {
            flag=0;
            for(int i=X1;i<=X2;i++)
            {
                for(int j=Y1;j<=Y2;j++)
                {
                    if(key[i-1][j]==1&&key[i][j-1]==1){key1[i][j]=1;}
                    else if(key[i-1][j]==0&&key[i][j-1]==0){key1[i][j]=0;}
                }
            }
            for(int i=X1;i<=X2;i++)
            {
                for(int j=Y1;j<=Y2;j++)
                {
                    key[i][j]=key1[i][j];
                    if(key[i][j]==1)flag=1;
                }
            }
            asw++;
        }
        printf("Case #%d: ",caseId);
        cout<<asw<<endl;

    }
    return 0;
}