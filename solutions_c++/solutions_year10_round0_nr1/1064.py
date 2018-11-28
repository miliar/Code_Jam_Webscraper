/*

 */
#include <iostream>
#include <cstring>
#include <cstdio>
#define maxv(a,b) (a>=b ? a : b)
#define minv(a,b) (a<=b ? a : b)
using namespace std;
int Case,n,k;
bool state[11],can[11];
bool check()
{
    for (int i=1;i<=n;i++) 
        if (!state[i]) return false;
    return true;
}
void display()
{
    cin>>Case;
    for (int ca=1;ca<=Case;ca++) {
        cout<<"Case #"<<ca<<": ";
        cin>>n>>k;
        memset(state,0,sizeof(state));
        memset(can,0,sizeof(can));
        state[0]=can[0]=1;
        while (k--) {
            for (int i=1;i<=n;i++) 
                can[i]=(can[i-1]&&state[i-1]);
            for (int i=1;i<=n;i++) 
                if (can[i]) state[i]=!state[i];
            }
        if (check()) cout<<"ON"<<endl;
        else cout<<"OFF"<<endl;
        }
}
int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    display();
    return 0;
}

