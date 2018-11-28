#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

    int cost[16][16][1<<16];
    int cost1[20][20];
    int cost2[20][20];
void tst()
{
    int k;
    char in2[50001];
    scanf("%d\n%s",&k,in2);
    string in(in2);
    int n = in.size();
    int d = n/k;
    bzero(cost1,sizeof(cost1));
    bzero(cost2,sizeof(cost2));
    for(int i=0;i<k;i++)
        for(int j=0;j<k;j++)
        {
            if(i==j)
                continue;
            for(int s = 0;s<d;s++)
            {
                cost1[i][j] +=  in[s*k+i]!=in[s*k+j];
            }
            for(int s = 0;s+1<d;s++)
            {
                cost2[i][j] += in[s*k+i] != in[(s+1)*k+j];
            }
//            cout << i << ' ' << j << ' ' << cost2[i][j] << endl;
        }

    bzero(cost,sizeof(cost));
    for(int mask=1;mask<(1<<k);mask++)
    {
        for(int b=0;b<k;b++)
        {
            for(int e=0;e<k;e++)
            {
                int& c = cost[b][e][mask];
                if( ((mask&(1<<b))==0) ||
                (b==e && mask != (1<<b)) ||
                ((mask&(1<<e))==0) )
                {
                    c = 1000000;
                    continue;
                }

                if(mask == (1<<b))
                    continue;

                c = 1000000;
                for(int x = 0; x < k; x++)
                {
                    if(x==e)
                        continue;
                    if(mask&(1<<x)==0)
                        continue;
                    c <?= cost[b][x][mask-(1<<e)] + cost1[x][e];
                }
//                cout << mask << ' ' << b << ' ' << e << ' ' << c << endl;
            }
        }
    }
    int minim = 1000000;
    for(int b=0;b<k;b++)
        for(int e=0;e<k;e++)
        {
            if(b==e)
                continue;
            minim <?= cost[b][e][(1<<k)-1] + cost2[e][b];
        }

    cout << minim+1;
}

int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        cout << "Case #"<<i<<": ";tst();cout<<endl;
    }
}
