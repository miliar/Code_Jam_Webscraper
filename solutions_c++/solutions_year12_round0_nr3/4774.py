// GCJ2012_C.cpp : Defines the entry point for the console application.
//

#include <set>
using namespace std;

int main(int argc, char* argv[])
{
    freopen("c:/txt/C-large.txt","r",stdin);
    freopen("c:/txt/GCJ2012-C-LResult.txt","w",stdout);
    int T, a, b, i, j, k;
    scanf("%d",&T);
    for(i=0;i<T;i++)
    {
        scanf("%d %d",&a, &b);
        int cnt=0;
        for(int n=a;n<=b;n++)
        {
            set<int> s1;
            int t=n;
            int a[20]={0};
            int d=0;
            while(t)
            {
                a[d++]=t%10;
                t/=10;
            }
            for(j=d;j<2*d;j++)
            {
                a[j]=a[j-d];
            }
            for(j=1;j<d;j++)
            {
                int m=0;
                for(k=j+d-1;k>=j;k--)
                {
                    m*=10;
                    m+=a[k];
                }
                if(m>n && m<=b)
                {
                    s1.insert(m);
                    //printf("m=%d, n=%d\n", m, n);
                }
            }
            cnt+=s1.size();
        }
        printf("Case #%d: %d\n", i+1, cnt);
    }
    return 0;
}

