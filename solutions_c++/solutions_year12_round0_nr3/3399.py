#include <cstdio>
#include <iostream>
using namespace std;

int h[1001][1001];
int A, B;
int T;

int pow(int x, int y)
{
    int p = 1;
    for(int i = 1; i <= y; i++)
    {
        p *= x;
    }
    return p;
}

int len(int x)
{
    int c = 0;
    while(x)
    {
        c++;
        x = x/10;
    }
    return c;
}

int reorder(int x, int tail)
{
    int sep = pow(10, tail);
    int t_nr = x % sep;
    //cout<<"TAIL: "<<t_nr<<endl;
    int h_nr = x / sep;
    //cout<<"HEAD: "<<h_nr<<endl;
    return t_nr * pow(10, (len(x) - tail)) + h_nr;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>T;
    for(int t = 1; t <= T; t++)
    {
        for(int i = 0; i < 1001; i++)
        {
            for(int j = 0; j < 1001; j++)
            {
                h[i][j] = 0;
            }
        }

        cin>>A>>B;

        for(int i = A; i <= B; i++)
        {
            int l = len(i);
            for(int j = 1; j < l; j++)
            {
                int reordered = reorder(i, j);
                if ((reordered < A) || (reordered > B))
                {
                    continue;
                }
                if (reordered == i)
                {
                    continue;
                }
                if (l == len(reordered))
                {
                    if ((h[i][reordered] == 0) && (h[reordered][i] == 0))
                    {
                        h[i][reordered] = 1;
                        //cout<<i<<" "<<reordered<<endl;
                    }
                }
            }
        }

        int count = 0;

        for(int i = 0; i < 1001; i++)
        {
            for(int j = 0; j < 1001; j++)
            {
                if(h[i][j] == 1)
                {
                    count++;
                }
            }
        }

        cout<<"Case #"<<t<<": "<<count<<endl;
    }
    return 0;
}
