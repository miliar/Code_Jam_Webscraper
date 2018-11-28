#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

int m[200];
int inc[200];
int n,p,s;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int C,num=0;
    cin >> C;
    while (C)
    {
        C--;num++;
        printf("Case #%d: ",num);
        
        cin >> n >> s >> p;
        for (int i=0;i<n;i++) cin >> m[i];
        for (int i=0;i<n;i++)
        {
            if (m[i]%3==0)
            {
                m[i]=m[i]/3;
                if (m[i]>0) inc[i]=1;else inc[i]=0;
            }
            else if (m[i]%3==1)
            {
                m[i]=m[i]/3+1;
                inc[i]=0;
            }
            else if (m[i]%3==2)
            {
                m[i]=m[i]/3+1;
                if (m[i]>1) inc[i]=1;else inc[i]=0;
            }
        }
            
            int count=0;
            for (int i=0;i<n;i++)
            {
                if (m[i]>=p) count++;
                else if (m[i]==p-1 && inc[i] && s)
                {
                    s--;
                    count++;
                }
            }
            

        
        cout << count << endl;
    }
}
                
        
        
        
