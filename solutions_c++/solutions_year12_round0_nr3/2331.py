#include <vector>
#include <algorithm>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;
int key[2000001]={0};
int main()
{
    	freopen("D:\\GCJ 2012\\C-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2012\\C-small-attempt0.out","w",stdout);
    //	freopen("D:\\GCJ 2012\\C-small-attempt1.in","r",stdin);freopen("D:\\GCJ 2012\\C-small-attempt1.out","w",stdout);
    //	freopen("D:\\GCJ 2012\\C-large.in","r",stdin);freopen("D:\\GCJ 2012\\C-large.out","w",stdout);
    int testcase;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    int A,B;
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        cin>>A>>B;
        for(int i=0;i<=B;i++)key[i]=0;
        A=max(10,A);
        int asw=0;
        int t,t1,t2,p;
        for(int i=A;i<=B;i++)
        {
            t=i;
            t1=i;
            p=1;
            int j=0;
            while(t1>0)
            {
                j++;
                t1/=10;
                p*=10;
            }
            t1=t;
            int num=1,k=10;
            while(num<j)
            {
                t2=t1/k+(t1%k)*p/k;
                if(t2>t&&t2>=A&&t2<=B&&(t2/(p/10)!=0)&&key[t2]!=t){asw++;key[t2]=t;}
                t1=t;
                num++;
                k*=10;
            }
        }
        printf("Case #%d: %d\n",caseId,asw);

    }
    return 0;
}