#include <iostream>
using namespace std;

int main()
{
    int T, t;
    int R, r;
    int x1, y1, x2, y2;
    bool bact[101][101], temp[101][101];
    int i, j;
    bool ok;
    int ans;

    cin>>T;
    for(t=1; t<=T; t++)
    {
        cin>>R;
        for(i=0; i<=100; i++)
            for(j=0; j<=100; j++)
                bact[i][j] = temp[i][j] = 0;
        for(r=1; r<=R; r++)
        {
            cin>>x1>>y1>>x2>>y2;
            for(i=y1; i<=y2; i++)
                for(j=x1; j<=x2; j++)
                    bact[i][j] = 1;
        }
        ans = 0;
        ok = true;
        while(ok)
        {
            for(i=1; i<=100; i++)
                for(j=1; j<=100; j++)
                {
                    temp[i][j] = bact[i][j];
                    if(bact[i-1][j]==0&&bact[i][j-1]==0)
                        temp[i][j] = 0;
                    if(bact[i-1][j]==1&&bact[i][j-1]==1)
                        temp[i][j] = 1;
                }
            ans++;
            ok = false;
            for(i=1; i<=100; i++)
                for(j=1; j<=100; j++)
                {
                    bact[i][j] = temp[i][j];
                    if(bact[i][j]==1)
                        ok = true;
                }
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }

    return 0;
}

