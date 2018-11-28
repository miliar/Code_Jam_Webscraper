#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int r,mx,my,step,x1,y1,x2,y2;
bool the, g[110][110];
int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int testcase;
    scanf("%d",&testcase);
    for (int tc=1;tc<=testcase;++tc)
    {
        cin>>r;
        mx=0;
        my=0;
        memset(g,0,sizeof(g));
        the = false;
        for (int i=1;i<=r;++i) {
            cin>>x1>>y1>>x2>>y2;
            if (x1>x2) swap(x1,x2);
            if (y1>y2) swap(y1,y2);
            mx=max(mx,x2);
            my=max(my,y2);

            for (int k=x1;k<=x2;++k)
            for (int j=y1;j<=y2;++j)
            {
                g[k][j]=true;
                the = the | g[k][j];
            }
        }
        step = 0;
        while (the) {
            step++;
            the = false;
            for (int i=mx;i>=1;--i)
            for (int j=my;j>=1;--j)
            {
                if (g[i][j]) g[i][j]=g[i-1][j] | g[i][j-1];
                else g[i][j] = g[i-1][j] & g[i][j-1];
                the|=g[i][j];
            }
        }
    	cout<<"Case #";
    	cout<<tc<<": ";
    	cout<<step<<endl;
    }
	return 0;
}
