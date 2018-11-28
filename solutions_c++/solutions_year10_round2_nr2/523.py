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
    //	freopen("D:\\GCJ 2010\\B-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2010\\B-small-attempt0.out","w",stdout);
    //	freopen("D:\\GCJ 2010\\B-small-attempt1.in","r",stdin);freopen("D:\\GCJ 2010\\B-small-attempt1.out","w",stdout);
    	freopen("D:\\GCJ 2010\\B-large.in","r",stdin);freopen("D:\\GCJ 2010\\B-large.out","w",stdout);
    int testcase;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        int N,K,B,T;
        int a[51]={0},v[51]={0},s[51]={0};
        cin>>N>>K>>B>>T;
        for(int i=0;i<N;i++)
        {
            cin>>a[i];
        }
        for(int i=0;i<N;i++)
        {
            cin>>v[i];
        }
        printf("Case #%d: ",caseId);
        int no=0,i1=N-1,t1=0;
        while(no<K&&i1>=0)
        {
            if(T*v[i1]+a[i1]>=B){s[t1]=1;no++;}else s[t1]=-1;
            t1++;i1--;
        }
        if(no<K)cout<<"IMPOSSIBLE"<<endl;
        else 
        {
            int cur = 0;
            for(int i=0,x=0;i<t1;i++)
            {
                if (s[i] ==1)
                {
                    cur += i-x;
                    x++;
                }
            }
            cout<<cur<<endl;
        }
    }
    return 0;
}