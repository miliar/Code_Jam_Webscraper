#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int x,ans,p;
int m[2050];
bool the, g[110][110];
int search(int x,int y) {
    int dmin;
    if (x==1) dmin= min(m[y*2],m[y*2+1]);
    else  dmin= min(search(x-1,y*2),search(x-1,y*2+1));
    if (dmin<x) ans++;
    return dmin;
}
int main() {
 //   freopen("input.txt","r",stdin);
 //   freopen("output.txt","w",stdout);
    int testcase;
    scanf("%d",&testcase);
    for (int tc=1;tc<=testcase;++tc)
    {
        cin>>p;
        for (int i=0;i<(1<<p);++i) {
            cin>>m[i];
        }
        for (int i=1;i<=p;++i)
        for (int j=1;j<=(1<<(p-i));++j) {
            cin>>x;

        }
        ans=0;
        search(p,0);

    	cout<<"Case #";
    	cout<<tc<<": ";
    	cout<<ans<<endl;
    }
	return 0;
}
