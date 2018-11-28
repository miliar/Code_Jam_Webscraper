#include <iostream>
#include <map>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

int len(int a)
{
    int l=0;
    while (a!=0)
    {
        l++;
        a=a/10;
    }

    return l;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out3-l.txt","w",stdout);

    int n,a,b;
    cin >> n;

    for (int j=0; j<n; j++)
    {
        int ans=0;
        cin >> a >> b;
        for (int i=a; i<=b; i++)
        {
            int l=len(i);
            int tmp=i;
            do
            {
                int t=tmp%10;
                tmp=tmp/10;
                tmp=tmp+(int)pow(10,l-1)*t;

                if ((tmp > i) && (tmp <=b && tmp >= a))
                {
                   ans++;
                }
            }while (tmp!=i);
        }
        cout << "Case #" << j+1 << ": " << ans << endl;
    }

    return 0;
}
