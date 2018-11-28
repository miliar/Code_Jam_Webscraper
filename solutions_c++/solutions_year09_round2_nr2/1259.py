#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

#define two(x)  (1<<x)
#define twol(x) ((long long)1<<x)
#define sqr(x)  ((x)*(x))

main()
{
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int task;
    cin>>task;
    for (int t=1;t<=task;t++)
    {
        long long tmp;
        vector<int> num;
        cin>>tmp;
        while (tmp)
        {
            num.push_back(tmp%10);
            tmp/=10;   
        }   
        cout<<"Case #"<<t<<": ";
        int i=1,min=10;
        while (i<num.size()&&num[i]>=num[i-1])    i++;
        if (i==num.size())
        {
            sort(num.begin(),num.end());
            for (int i=0;i<num.size();i++)
                if (num[i]!=0)
                {
                    cout<<num[i];
                    num[i]=-1;   
                    break;
                }
            cout<<0;
            for (int i=0;i<num.size();i++)  
                if (num[i]!=-1)
                    cout<<num[i];
            cout<<endl;
            continue;   
        }
        for (int j=0;j<i;j++)
            if (num[j]>num[i])  min<?=num[j];
        for (int j=num.size()-1;j>i;j--)
            cout<<num[j];
        cout<<min;
        for (int j=0;j<i;j++)
            if (num[j]==min)    num[j]=-1,min=10;
        vector<int> cur;
        for (int j=0;j<=i;j++)  
            if (num[j]!=-1)
                cur.push_back(num[j]);        
        sort(cur.begin(),cur.end());
        for (int i=0;i<cur.size();i++)
            cout<<cur[i];
        cout<<endl;
    }
}
