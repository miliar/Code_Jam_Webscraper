#include <iostream>
#include <vector>
#include <stdio.h>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;

#define PI acos(-1.0)
#define clear(x) memset(x,0,sizeof(x))
#define read(x) scanf("%d",&x)
#define reads(x) scanf("%s",x)
#define write(x) printf("%d",x)
#define writeln(x) printf("%d\n",x)
#define writes(x) printf("%s",x)

long long r,k,n,temp,last,start,geld,p1,p2;
long long re[2100],ti[2100],b[2100],c[2100],a[2100];

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int testcase;
	read(testcase);
	for (int tc=1;tc<=testcase;++tc)
	{
        read(r);
        read(k);
        read(n);
        for (int i=0;i<n;++i)
        {
            read(a[i]);
            a[i+n]=a[i];
        }
        temp=a[0];
        last=0;
        for (int i=0;i<n;++i)
        {
            while ((last<i+n-1) && (temp+a[last+1]<=k))
            {
                temp+=a[last+1];
                last++;
            }
            b[i]=last%n;
            c[i]=temp;
            temp-=a[i];
        }
        for (int i=0;i<n;++i) re[i]=-1;
        start=0;
        geld=0;
        for (int i=1;i<=r;++i)
        {
            if (re[start]==-1)
            {
                re[start]=geld;
                ti[start]=i;
                geld+=c[start];
                start=b[start]+1;
                start%=n;
            } else
            {
                p1=(r-ti[start]+1)/(i-ti[start])-1;
                p2=(r-ti[start]+1)%(i-ti[start]);
                geld+=(geld-re[start])*p1;
                for (int j=1;j<=p2;++j)
                {
                    geld+=c[start];
                    start=b[start]+1;
                    start%=n;
                }
                break;
            }
        }
		writes("Case #");
		write(tc);
		writes(": ");
		writeln(geld);
	}
	return 0;
}
