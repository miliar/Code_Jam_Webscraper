#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

bool p[1000000];
int li[500000];
int co;
long long N;

int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int ntest;
    cin>>ntest;
    memset(p,1,sizeof(p));
    for (int i = 2; i<1000000; i++)
        if (p[i])
            for (int j = i*2; j<1000000; j += i)
                p[j] = 0;
    co = 0;
    for (int i = 2; i<1000000; i++)
        if (p[i]) li[co++] = i;
    for (int run = 1; run<=ntest; run++) {
        cout<<"Case #"<<run<<": ";
        cin>>N;
        long long ans = 0;
        for (int i = 0; i<co && N>=li[i]; i++) {
            long long tN = N;
            long long tmp = 0;
            while (tN>=li[i]) {
                tmp++;
                tN /= li[i];
            }
            ans += tmp;
            if (N>=li[i]) ans--;
        }
        if (N>1) cout<<ans+1<<endl;
        else cout<<0<<endl;
    }
    return 0;
}
