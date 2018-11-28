#include <iostream>
#include <cstdio>
using namespace std;

int des[10];

int sdvig(int a, int l,int n)
{
    return a%(des[l-n])*des[n]+a/des[l-n];
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int f=1;
    int n;


    for (int i=0;i<10;i++)
    {
        des[i]=f;
        f*=10;
    }
    cin >> n;
    for (int i=0;i<n;i++)
    {
        long long int cnt=0;
        cout << "Case #" << i+1 << ": ";
        int a,b,l=0;
        cin >> a >> b;
        while (des[l]<=a) l++;
        for (int j=a;j<=b;j++)
        {
            if (des[l]<=j) l++;
            int p=1;
            int t=sdvig(j,l,p);
            while (t!=j)
            {
                if (t>j&&t<=b) cnt++;
                p++;
                t=sdvig(j,l,p);
            }

        }
        cout << cnt << endl;
    }
    return 0;
}
