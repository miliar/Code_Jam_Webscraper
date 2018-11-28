#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,t1;
    cin >> t;
    int i,j;
    int cp,d,n;
    char c1,c2,c3;
    char c[256][256];
    bool p[256][256];
    
    bool flag;
    
    char str[120];
    int strlen;
    for(t1=0;t1<t;t1++)
    {
        for(i=0;i<256;i++)
        {
            for(j=0;j<256;j++)
            {
                c[i][j]=-1;
                p[i][j]=0;
            }
        }
        cin >> cp;
        for(i=0;i<cp;i++)
        {
            cin >> c1 >> c2 >> c3;
            c[c1][c2]=c3;
            c[c2][c1]=c3;
        }
        
        cin >> d;
        for(i=0;i<d;i++)
        {
            cin >> c1 >> c2;
            p[c1][c2]=1;
            p[c2][c1]=1;
        }
        
        cin >> n;
        strlen=0;
        for(i=0;i<n;i++)
        {
            flag=1;
            cin >> c1;
            if(strlen>0 && c[c1][str[strlen-1]]!=-1)
            {
                str[strlen-1]=c[c1][str[strlen-1]];
                flag=0;
            }
            if(flag)
            {
                for(j=0;j<strlen;j++)
                {
                    if(p[str[j]][c1]){flag=0;break;}
                }
                if(!flag)
                {
                    strlen=0;
                } else
                {
                    str[strlen++]=c1;
                }
            }
        }
        cout << "Case #" << t1+1 << ": [";
        for(i=0;i<strlen;i++)
        {
            if(i>0){cout << ", ";}
            cout << str[i];
        }
        cout << "]\n";
    }
    return 0;
}
