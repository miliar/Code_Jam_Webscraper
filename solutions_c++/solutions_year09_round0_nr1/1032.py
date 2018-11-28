/*
OS: Microsoft Windows XP Professional
Compiler: Bloodshed Dev-C++ 4.9.9.2
*/
#include <iostream>
#include <string>
#include <cstdlib>
#include <cctype>
using namespace std;
int l, d, n;
string dic[5002];
bool f[16][27]={0};
int main()
{
    freopen("al.in", "r", stdin);
    freopen("al.out", "w", stdout);
    int i, j, k, p, sum;
    bool inside, key;
    string tmp;
    cin>>l>>d>>n;
    for (i=1; i<=d; i++)
        cin>>dic[i];
    for (i=1; i<=n; i++)
    {
        memset(f, 0, sizeof(f));
        p=0;
        inside=false;
        cin>>tmp;
        for (j=0; j<tmp.length(); j++)
        {
            if (islower(tmp[j]))
            {
                if (inside)
                    f[p][tmp[j]-'a']=true;
                else
                {
                    f[p][tmp[j]-'a']=true;
                    p++;
                }                    
            }
            else
            {
                if (tmp[j]=='(')
                    inside=true;
                else
                {
                    inside=false;
                    p++;
                }
            }
        }
        sum=0;
        for (j=1; j<=d; j++)
        {
            key=true;
            for (k=0; k<l; k++)
                if (!f[k][dic[j][k]-'a'])
                {
                    key=false;
                    break;
                }
            if (key)
                sum++;
        }
        cout<<"Case #"<<i<<": "<<sum<<endl;
    }
    return 0;
}
