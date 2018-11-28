#include <vector>
#include <algorithm>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;
char res[51][51];
char a[51][51];
int main()
{
    //	freopen("D:\\GCJ 2010\\A-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2010\\A-small-attempt0.out","w",stdout);
    //	freopen("D:\\GCJ 2010\\A-small-attempt1.in","r",stdin);freopen("D:\\GCJ 2010\\A-small-attempt1.out","w",stdout);
   // freopen("D:\\GCJ 2010\\A-small-attempt3.in","r",stdin);freopen("D:\\GCJ 2010\\A-small-attempt3.out","w",stdout);
    	freopen("D:\\GCJ 2010\\A-large.in","r",stdin);freopen("D:\\GCJ 2010\\A-large.out","w",stdout);
    int testcase;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        memset(a,0,sizeof(a));
        memset(res,0,sizeof(res));
        int N,K;
        cin>>N>>K;
        for(int j=N-1;j>=0;j--)
        {
            for(int i=0;i<N;i++)
            {
                cin>>a[i][j];
            }
        }
    //    for(int i=0;i<N;i++){for(int j=0;j<N;j++)cout<<a[i][j];cout<<endl;}
        int tx=0,ty=0;
        for(int j=0;j<N;j++)
        {
            tx=N-1;ty=j;
            for(int i=N-1;i>=0;i--)
            {
                if(a[i][j]!='.'){res[tx][ty]=a[i][j];tx--;}
            }
        }
//        for(int i=0;i<N;i++){for(int j=0;j<N;j++)cout<<res[i][j];cout<<endl;}

        int flag11=1,flag12=1,flag21=1,flag22=1,flag31=1,flag32=1;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                int t1=0;
                if(flag11!=0||flag12!=0&&i+K<=N)
                {
                    char rr1='R',rr2='B';
                    t1=0;
                    for(int k=0;k<K;k++)
                    {
                        if(res[i+k][j]!=rr1){t1++;k=K;}
                    }
                 //   if(i>0&&res[i-1][j]==rr1)t1++;
                 //   if(i+K<N&&res[i+K][j]==rr1)t1++;
                    if(t1==0)flag11=0;
                    t1=0;
                     for(int k=0;k<K;k++)
                    {
                        if(res[i+k][j]!=rr2){t1++;k=K;}
                    }
               //      if(i>0&&res[i-1][j]==rr2)t1++;
                //     if(i+K<N&&res[i+K][j]==rr2)t1++;
                     if(t1==0)flag12=0;
                }
                if(flag21!=0||flag22!=0&&j+K<=N)
                {
                    char rr1='R',rr2='B';
                    t1=0;
                    for(int k=0;k<K;k++)
                    {
                        if(res[i][j+k]!=rr1){t1++;k=K;}
                    }
               //     if(j>0&&res[i][j-1]==rr1)t1++;
               //     if(j+K<N&&res[i][j+K]==rr1)t1++;
                    if(t1==0)flag21=0;
                    t1=0;
                     for(int k=0;k<K;k++)
                    {
                        if(res[i][j+k]!=rr2){t1++;k=K;}
                    }
                //     if(j>0&&res[i][j-1]==rr2)t1++;
                //     if(j+K<N&&res[i][j+K]==rr2)t1++;
                     if(t1==0)flag22=0;
                }
                if(i+K<=N&&j+K<=N)
                {
                    char rr1='R',rr2='B';
                    t1=0;
                    for(int k=0;k<K;k++)
                    {
                        if(res[i+k][j+k]!=rr1){t1++;k=K;}
                    }
               //     if(i>0&&j>0&&res[i-1][j-1]==rr1)t1++;
               //     if(i+K<N&&j+K<N&&res[i+K][j+K]==rr1)t1++;
                    if(t1==0)flag31=0;
                    t1=0;
                    for(int k=0;k<K;k++)
                    {
                        if(res[i+k][j+k]!=rr2){t1++;k=K;}
                    }
               //     if(i>0&&j>0&&res[i-1][j-1]==rr2)t1++;
              //      if(i+K<N&&j+K<N&&res[i+K][j+K]==rr2)t1++;
                    if(t1==0)flag32=0;
                }
                if(i+K<=N&&j-K>=-1)
                {
                    char rr1='R',rr2='B';
                    t1=0;
                    for(int k=0;k<K;k++)
                    {
                        if(res[i+k][j-k]!=rr1){t1++;k=K;}
                    }
               //     if(i+K<N&&j-K>=0&&res[i+K][j-K]==rr1)t1++;
               //     if(i-1>=0&&j+1<N&&res[i-1][j+1]==rr1)t1++;
                    if(t1==0)flag31=0;
                    t1=0;
                    for(int k=0;k<K;k++)
                    {
                        if(res[i+k][j-k]!=rr2){t1++;k=K;}
                    }
              //      if(i+K<N&&j-K>=0&&res[i+K][j-K]==rr2)t1++;
               //     if(i-1>=0&&j+1<N&&res[i-1][j+1]==rr2)t1++;
                    if(t1==0)flag32=0;
                }
                if(flag31==0&&flag32==0){i=N;j=N;}
            }
        }
        printf("Case #%d: ",caseId);
        int a=0,b=0;
        if(flag11==0||flag21==0||flag31==0)a=1;
        if(flag12==0||flag22==0||flag32==0)b=1;
        if(a==1&&b==1)cout<<"Both"<<endl;
        else if(a==0&&b==0)cout<<"Neither"<<endl;
        else if(a==1)cout<<"Red"<<endl;
        else cout<<"Blue"<<endl;
    }
    return 0;
}