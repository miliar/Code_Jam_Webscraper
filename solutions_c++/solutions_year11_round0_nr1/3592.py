#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>


using namespace std;

const int MAXN = 110;
const int orange = 0, blue = 1;
int Pos[MAXN];
char Cat[MAXN];
int N;
int main()
{
    //freopen("test.in","r",stdin);

    freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    int T;
    cin>>T;
    int tc=1;
    while(T--) {

        cin>>N;
        int op=1,bp=1;
        int timeo = 0, timeb = 0, ret = 0;
        for(int i = 1; i <= N; i++) {
            char c;cin>>Cat[i];

            cin>>Pos[i];

            if(Cat[i]=='O') {

                if(timeo>=timeb) {
                    timeo+=abs(Pos[i]-op)+1;

                }
                else {
                    if(Pos[i]==op) {
                        timeo=timeb+1;
                    }
                    else {

                        if(timeo+abs(Pos[i]-op)+1<=timeb) timeo=timeb+1;
                        else timeo+=abs(Pos[i]-op)+1;
                    }
                }
                op=Pos[i];
            }
            else {
                if(timeb>=timeo) {
                    timeb+=abs(Pos[i]-bp)+1;

                }
                else {
                    if(Pos[i]==bp) {
                        timeb=timeo+1;
                    }
                    else {
                        if(timeb + abs(Pos[i]-bp)+1 <= timeo) timeb = timeo+1;
                        else timeb+=abs(Pos[i]-bp)+1;
                    }
                }
                bp=Pos[i];
            }
            ///if(i==2)cout<<timeo<<" "<<timeb<<endl;

        }

        cout<<"Case #"<<tc++<<": "<<max(timeo,timeb)<<endl;
    }
    return 0;
}
