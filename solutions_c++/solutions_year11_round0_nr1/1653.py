#include <iostream>
#include <cstdio>
#include <stdlib.h>
using namespace std;
const int maxn=200;
int t1,n,t[maxn];
bool b[maxn];
char ch;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>t1;int z=t1;
    while (t1--){
        cin>>n;
        for (int i = 0; i < n; ++i){
            cin>>ch >>t[i];
            if (ch == 'O') b[i] = true;
                else b[i] = false;
        }
        int i=1,st=t[0],x=t[0],p[2];
        bool bo=b[0];
        p[bo]=t[0];p[1-bo]=1;
        while (i<n){
            if (b[i] != bo){
                if ((abs(p[b[i]] - t[i])) <= x){
                    x = 1;
                    ++st;
                } else {
                    int y = abs(p[b[i]] - t[i]) - x + 1;
                    st += y;
                    x = y;
                }
                p[b[i]] = t[i];
                bo = b[i];
            } else {
                st += abs(p[bo] - t[i]) + 1;
                x += abs(p[bo] - t[i]) + 1;
                p[bo] = t[i];
            }
            i++;
        }
        cout<<"Case #" <<z-t1 <<": " <<st <<endl;
    }
}
