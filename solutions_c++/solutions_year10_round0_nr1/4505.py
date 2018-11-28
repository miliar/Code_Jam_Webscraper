#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <math.h>
#include <stdio.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    int no,n,k;
    char c;
    scanf("%d%c",&no,&c);
    vector <bool> p;
    vector <bool> s;
    for(int kk=1;kk<=no;kk++)
    {
        scanf("%d %d%c",&n,&k,&c);
        
        
        for(int i=0;i<n;i++)
        {
            s.push_back(false);
        }
        for(int i=0;i<k;i++)
        {
            for(int ap=0;ap<n;ap++)
            {
                if(ap==0)
                    p.push_back(true);
                else
                    p.push_back(false);
            }
            for(int ap=0;ap<n-1;ap++)
            {
                if(p[ap]&&s[ap])
                {
                    p[ap+1]=true;
                }
                else
                    goto ash;
            }
            ash:

            for(int j=0;j<n;j++)
            {
                if(p[j])
                {
                    if(s[j])
                    {
                        s[j]=false;
                    }
                    else
                    {
                        s[j]=true;
                    }                    
                }
            }
            p.erase(p.begin(),p.end());
        }
        for(int ap=0;ap<n;ap++)
            {
                if(ap==0)
                    p.push_back(true);
                else
                    p.push_back(false);
            }
            for(int ap=0;ap<n-1;ap++)
            {
                if(p[ap]&&s[ap])
                {
                    p[ap+1]=true;
                }
                else
                    goto ashu;
            }
            ashu:
        if(p[n-1]&&s[n-1])
            printf("Case #%d: ON\n",kk);
        else
            printf("Case #%d: OFF\n",kk);
        p.erase(p.begin(),p.end());
        s.erase(s.begin(),s.end());
    }
    return 0;
}
