#include<iostream>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<utility>
#include<iomanip>
#include<queue>
using namespace std;
#define clr(a) memset(a,0,sizeof(a))
#define fill(a,v) memset(a,v,sizeof(a))
#define PB push_back
#define pi acos(-1.0)
#define eps 1e-9


int main()
{
    string s;
    int tc,kk=1,l,i;

    //freopen("A-small-attempt3.in","r",stdin);
    //freopen("A-small-attempt3.out","w",stdout);
    cin>>tc;
    char c;
    getchar();
   // cin>>c;
    while(tc--)
    {
        getline(cin,s);
        l=s.length();
        cout<<"Case #"<<kk++<<": ";
        for(i=0;i<l;i++)
        {
            switch(s[i])
            {
                case 'y':
                    cout<<'a';
                    break;
                case 'n':
                    cout<<'b';
                    break;
                case 'f':
                    cout<<'c';
                    break;
                case 'i':
                    cout<<'d';
                    break;
                case 'c':
                    cout<<'e';
                    break;
                case 'w':
                    cout<<'f';
                    break;
                case 'l':
                    cout<<'g';
                    break;
                case 'b':
                    cout<<'h';
                    break;
                case 'k':
                    cout<<'i';
                    break;
                case 'u':
                    cout<<'j';
                    break;
                case 'o':
                    cout<<'k';
                    break;
                case 'm':
                    cout<<'l';
                    break;
                case 'x':
                    cout<<'m';
                    break;
                case 's':
                    cout<<'n';
                    break;
                case 'e':
                    cout<<'o';
                    break;
                case 'v':
                    cout<<'p';
                    break;
                case 'z':
                    cout<<'q';
                    break;
                case 'p':
                    cout<<'r';
                    break;
                case 'd':
                    cout<<'s';
                    break;
                case 'r':
                    cout<<'t';
                    break;
                case 'j':
                    cout<<'u';
                    break;
                case 'g':
                    cout<<'v';
                    break;
                case 't':
                    cout<<'w';
                    break;
                case 'h':
                    cout<<'x';
                    break;
                case 'a':
                    cout<<'y';
                    break;
                case 'q':
                    cout<<'z';
                    break;
                default:
                    cout<<s[i];
                break;

            }

        }
        cout<<endl;

    }
return 0;
}
