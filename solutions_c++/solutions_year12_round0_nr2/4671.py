#include <iostream>
#include <string>
#include <memory.h>
#include <stdio.h>

using namespace std;

const int maxt=31+31;
int m[maxt],a[maxt],b[maxt];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    for (int i=0;i<maxt;i++)
        if (i % 3 == 0) a[i]=i/3;
        else if (i % 3 == 1) a[i]=i/3+1;
        else a[i]=i/3+1;

    memset(m,0,sizeof(m));
    m[0]=1;m[29]=1;m[30]=1;
    for (int i=0;i<10;i++) m[i*3+1]=1;
    /*
    for (int i=2;i<28;i++)
        if (m[i]==0) b[i]=a[i]+1;*/

    for (int times=1;times<=T;times++)
    {
        int ans=0,n,s,p,x;
        cin >> n >> s >> p;
        for (int i=0;i<n;i++)
        {
            cin >> x;
            if (m[x]==0) {
                if (a[x]>=p) {
                    ans++;
                } else
                if (a[x]+1>=p&&s) {
                    s--;
                    ans++;
                }
            } else if (a[x]>=p) ans++;
        }
        cout << "Case #" <<  times << ": " << ans << endl;
    }
}
