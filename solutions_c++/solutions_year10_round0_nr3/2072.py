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
    	freopen("D:\\GCJ 2010\\C-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2010\\C-small-attempt0.out","w",stdout);
    //	freopen("D:\\GCJ 2010\\C-small-attempt1.in","r",stdin);freopen("D:\\GCJ 2010\\C-small-attempt1.out","w",stdout);
    //	freopen("D:\\GCJ 2010\\C-large.in","r",stdin);freopen("D:\\GCJ 2010\\C-large.out","w",stdout);
    int testcase;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        int r,k,n;
        int a[1001]={0};
        cin>>r>>k>>n;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        long long t=0,t1=0,res=0,flag=1,asw=0;
        while(r--)
        {
            flag=1;t1=0;
            while(flag)
            {
                t1++;
            res+=a[t];
            if(res>k){res-=a[t];flag=0;}
            else t++;
            if(t>=n)t=0;
            if(t1==n)flag=0;
            }
            asw+=res;
            res=0;
        }
        printf("Case #%d: ",caseId);
        cout<<asw<<endl;
    }
    return 0;
}