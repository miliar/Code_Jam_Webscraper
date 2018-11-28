#include "iostream"
#include "math.h"
#include "string"
#include "stdlib.h"
using namespace std;
int t, sum;
int b[64];
__int64 zhuan(int aa, int bb)
{
    int i;
    __int64 sum = 0;
    for (i=0;i<aa;i++)
    {
        sum += b[i]*pow((double)bb, (double) (aa-i-1));
    }
    return sum;
}

int main(){

    int i, j, k;
    freopen("D:\\google\\A-small-attempt1.in", "r", stdin);
    freopen("D:\\google\\A-small-attempt1.out", "w", stdout);
    cin>>t;
    for (k=0;k<t;k++)    
    {
        sum = 0;
        char text[64];
        cin>>text;
        int aa = strlen(text), bb = 1;
        int bit = 0, max = 1;
        b[0] = 1;
        for (i=1;i<aa;i++)
        {
            for (j=0;j<i;j++)
            {
                if (text[i] != text[j]) continue;
                b[i] = b[j];
                break;
            }
            if (j==i)
            {
                bb++;
                if (bb == 2) b[i] = 0;
                else b[i] = bb - 1;
            }
        }
        if (bb<2) bb=2;
        cout<<"Case #"<<k+1<<": ";
        cout<<zhuan(aa, bb)<<endl;
    }
}

