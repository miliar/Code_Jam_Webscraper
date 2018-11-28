#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define OFFSET 250

int min4(int a, int b, int c, int d)
{
    return min(min(a, b), min(c, d));
}

int max4(int a, int b, int c, int d)
{
    return max(max(a, b), max(c, d));
}

bool symmetrical(int diamond[501][501], int y, int x, int k)
{
    int i, j;
    for(i=y-2*k; i<=y+2*k; i++)
        for(j=x-2*k; j<=x+2*k; j++)
        {
            if(diamond[OFFSET+i][OFFSET+j]>=0&&diamond[OFFSET+y-(i-y)][OFFSET+j]>=0&&diamond[OFFSET+i][OFFSET+j]!=diamond[OFFSET+y-(i-y)][OFFSET+j])
                return false;
            if(diamond[OFFSET+i][OFFSET+j]>=0&&diamond[OFFSET+i][OFFSET+x-(j-x)]>=0&&diamond[OFFSET+i][OFFSET+j]!=diamond[OFFSET+i][OFFSET+x-(j-x)])
                return false;
        }
    return true;
}

int main()
{
    int diamond[501][501];
    int i, j;
    int k;
    int ans;
    int t, T;
    int minsize; // minsize is the minimum size after enlargement

    cin>>T;
    for(t=1; t<=T; t++)
    {
        cin>>k;
        // initialize to -1, -1 means empty
        for(i=0; i<=500; i++)
            for(j=0; j<=500; j++)
                diamond[i][j] = -1;
        // read the first half of the diamond
        for(i=1; i<=k; i++)
            for(j=1; j<=i; j++)
                cin>>diamond[OFFSET+i][OFFSET+k+1-i+2*(j-1)];
        // read the rest of the diamond
        for(i=k-1; i>=1; i--)
            for(j=1; j<=i; j++)
                cin>>diamond[OFFSET+2*k-i][OFFSET+k+1-i+2*(j-1)];

        minsize = 10000;
        for(i=1; i<=2*k-1; i++)
            for(j=1; j<=2*k-1; j++)
            {
                if(symmetrical(diamond, i, j, k)&& max4( i+abs(j-k) , 2*k-i+abs(j-k) , j+abs(i-k) , 2*k-j+abs(i-k) ) < minsize)
                    minsize = max4( i+abs(j-k) , 2*k-i+abs(j-k) , j+abs(i-k) , 2*k-j+abs(i-k) );
            }

        ans = minsize*minsize-k*k;
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }

    return 0;
}

