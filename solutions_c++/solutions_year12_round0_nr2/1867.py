#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<list>
#include<queue>
#include<stack>
#include<cstdlib>
#include<sstream>

using namespace std;

int main()
{
    int t;
    scanf("%d",&t);

    for(int i=1; i<=t; i++)
    {
        int n,p,s,cur,max=0;
        cin>>n>>s>>p;
        for(int j=0; j<n; j++)
        {
            cin>>cur;
            int rem = cur%3;
            int x;
            if(rem==1)
            {
                x = cur/3;
                if(x+1>=p && x+1<=10)
                    max++;
            }
            else if(rem==2)
            {
                x = cur/3;
                if(x+1>=p && x+1<=10)
                    max++;
                else if(s>0 && x+2>=p && x+2<=10)
                {
                    max++;
                    s--;
                }
            }
            else
            {
                if((cur/3)>=p)
                    max++;
                else if(cur>=1)
                {
                    x = (cur-1)/3;
                    if(s>0 &&  x+2>=p && x+2<=10)
                    {
                        max++;
                        s--;
                    }
                }
            }
        }
        cout<<"Case #"<<i<<": "<<max<<endl;
    }

    return 0;
}



