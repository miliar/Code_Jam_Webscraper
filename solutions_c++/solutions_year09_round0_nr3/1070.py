/*
OS: Microsoft Windows XP Professional
Compiler: Bloodshed Dev-C++ 4.9.9.2
*/
#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
using namespace std;
int n;
string tmp;
int f[30]={0};
int main()
{
    freopen("wcj.in", "r", stdin);
    freopen("wcj.out", "w", stdout);
    int i, j, k;
    cin>>n; cin.get();
    for (i=1; i<=n; i++)
    {
        memset(f, 0, sizeof(f));
        getline(cin, tmp);
        for (j=0; j<tmp.length(); j++)
        {
            switch (tmp[j])
            {
                case 'w':
                    f[0]++; f[0]%=10000;
                    break;
                case 'e':
                    f[1]+=f[0]; f[1]%=10000;
                    f[6]+=f[5]; f[6]%=10000;
                    f[14]+=f[13]; f[14]%=10000;
                    break;
                case 'l':
                    f[2]+=f[1]; f[2]%=10000;
                    break;
                case 'c':
                    f[3]+=f[2]; f[3]%=10000;
                    f[11]+=f[10]; f[11]%=10000;
                    break;
                case 'o':
                    f[4]+=f[3]; f[4]%=10000;
                    f[9]+=f[8]; f[9]%=10000;
                    f[12]+=f[11]; f[12]%=10000;
                    break;
                case 'm':
                    f[5]+=f[4]; f[5]%=10000;
                    f[18]+=f[17]; f[18]%=10000;
                    break;
                case ' ':
                    f[7]+=f[6]; f[7]%=10000;
                    f[10]+=f[9]; f[10]%=10000;
                    f[15]+=f[14]; f[15]%=10000;
                    break;
                case 't':
                    f[8]+=f[7]; f[8]%=10000;
                    break;
                case 'd':
                    f[13]+=f[12]; f[13]%=10000;
                    break;
                case 'j':
                    f[16]+=f[15]; f[16]%=10000;
                    break;
                case 'a':
                    f[17]+=f[16]; f[17]%=10000;
                    break;
                default:
                    break;
            }
        }
        cout<<"Case #"<<i<<": ";
        cout<<(f[18]/1000)%10;
        cout<<(f[18]/100)%10;
        cout<<(f[18]/10)%10;
        cout<<f[18]%10<<endl;;
    }
    return 0;
}
