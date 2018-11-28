#include<iostream>
using namespace std;

bool A[301][101][101];

void output(int t)
{
     for(int i = 1 ; i <= 10 ; i ++)
     {
             for(int j = 1 ; j <= 10 ; j ++)
                     cout<<A[t][i][j];
             cout<<endl;
     }
}

bool check(int cur)
{
    bool ret = false;
    for(int i = 1 ; i <= 100 ; i ++)
        for(int j = 1 ; j <= 100 ; j ++)
        {
            A[cur][i][j] = A[cur - 1][i][j];
            if(A[cur - 1][i][j] == 1 && A[cur-1][i-1][j] == 0 && A[cur-1][i][j-1] == 0)
                A[cur][i][j] = 0;
            if(A[cur - 1][i][j] == 0 && A[cur-1][i-1][j] == 1 && A[cur-1][i][j-1] == 1)
                A[cur][i][j] = 1;
            if(A[cur][i][j] == 1)
                ret = 1;

        }

    return ret;
}

int main()
{
    freopen("C.in" , "r" , stdin);
    freopen("C.out" , "w" , stdout);
    int T;
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
        memset(A , 0 , sizeof(A));
        int n;
        cin>>n;
        for(int i = 1 ; i <= n ; i ++)
        {
            int x1 , x2 , y1 , y2;
            cin>>x1>>y1>>x2>>y2;
            for(int x = x1 ; x <= x2 ; x ++)
                for(int y = y1 ; y <= y2 ; y ++)
                    A[0][x][y] = true;
        }
        for(int i = 1 ; i <= 1000 ; i ++)
            if(check(i) == false)
            {
                cout<<"Case #"<<caseID<<": "<<i<<endl;
                break;
            }

    }
    return 0;
}
