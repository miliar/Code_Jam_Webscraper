#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<ctime>
#include<cctype>
#include<cassert>
#include<climits>
#include<cerrno>
#include<cfloat>
#include<ciso646>
#include<clocale>
#include<csetjmp>
#include<csignal>
#include<cstdarg>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cwchar>
#include<cwctype>

//containers
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<complex>
#include<string>
#include<stack>
#include<bitset>
#include<istream>
#include<valarray>

//IOs
#include<iostream>
#include<sstream>
#include<iomanip>
#include<fstream>
#include<exception>
#include<ios>
#include<iosfwd>
#include<ostream>
#include<iterator>
#include<stdexcept>
#include<streambuf>


//algorithm & miscellaneous
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<limits>
#include<locale>
#include<memory>
#include<new>
#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned long long
using namespace std;
char a[4][4];
int main(){
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int ca=1;
    int t,x,o,test;
    cin>>test;
    while(test--){
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        int dot=0,flag=0;
        for(int i=0;i<4;i++){
            x=0,t=0,o=0;
            for(int j=0;j<4;j++){
                if(a[i][j]=='X')
                    x++;
                else if(a[i][j]=='O')
                    o++;
                else if(a[i][j]=='T')
                    t++;
                else if(a[i][j]=='.')
                    dot++;
            }
            if(x==3 and t==1 or x==4){
                cout<<"Case #"<<ca<<": X won\n";
                flag=1;
            }
            else if(o==3 and t==1 or o==4){
                flag=1;
                cout<<"Case #"<<ca<<": O won\n";
            }
        }
        if(flag==0){
            x=0,t=0,o=0;
        for(int i=0;i<4;i++){
            if(a[i][i]=='X')
                x++;
            else if(a[i][i]=='O')
                o++;
            else if(a[i][i]=='T')
                t++;
            else if(a[i][i]=='.')
                dot++;
            if(x==3 and t==1 or x==4){
                cout<<"Case #"<<ca<<": X won\n";
                flag=1;
            }
            else if(o==3 and t==1 or o==4){
                flag=1;
                cout<<"Case #"<<ca<<": O won\n";
            }
        }
        }
        x=0,t=0,o=0;
        if(flag==0){
        for(int i=0;i<4;i++){
            if(a[i][3-i]=='X')
                x++;
            else if(a[i][3-i]=='O')
                o++;
            else if(a[i][3-i]=='T')
                t++;
            else if(a[i][3-i]=='.')
                dot++;
            if(x==3 and t==1 or x==4){
                cout<<"Case #"<<ca<<": X won\n";
                flag=1;
            }
            else if(o==3 and t==1 or o==4){
                flag=1;
                cout<<"Case #"<<ca<<": O won\n";
            }
        }
        }
        if(flag==0){
            for(int j=0;j<4;j++){
                x=0,t=0,o=0;
                for(int i=0;i<4;i++){
                    if(a[i][j]=='X')
                        x++;
                    else if(a[i][j]=='O')
                        o++;
                    else if(a[i][j]=='T')
                        t++;
                    else if(a[i][j]=='.')
                        dot++;
                }
                if(x==3 and t==1 or x==4){
                    flag=1;
                    cout<<"Case #"<<ca<<": X won\n";
                }
                else if(o==3 and t==1 or o==4){
                    cout<<"Case #"<<ca<<": O won\n";
                    flag=1;
                }
            }
        }
        if(flag==0){
        }

            if(dot>0 and flag==0)
                cout<<"Case #"<<ca<<": Game has not completed\n";
            else if(flag==0)
                cout<<"Case #"<<ca<<": Draw\n";
        ca++;
    }

    return 0;
}
