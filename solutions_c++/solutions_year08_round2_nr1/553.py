#include <iostream>

using namespace std;

unsigned long long  N;

unsigned long long  n;
unsigned long long  A;
unsigned long long  B;
unsigned long long  C;
unsigned long long  D;

unsigned long long  x0;
unsigned long long  y0;

unsigned long long  M;

unsigned long long treeX[100000];
unsigned long long treeY[100000];

unsigned long long numAfterDiv[100000][3][3];

int main()
{
    cin >> N;
    
    for(int task = 1; task <= N; ++task)
    {
        unsigned long long ans = 0;
        
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        
        unsigned long long tx = x0;
        unsigned long long ty = y0;
        
        treeX[0] = x0;
        treeY[0] = y0;
        
        /*
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < 3; ++j)
                for(int k = 0; k < 3; ++k)
                    numAfterDiv[i][j][k] = 0;
        */
        
        for(int i = 1; i < n; ++i)
        {
            tx = (A*tx+B)%M;
            ty = (C*ty+D)%M;
            
            treeX[i] = tx;
            treeY[i] = ty;
            //numAfterDiv[i]
        }

        for(int i = 0; i < n; ++i)
        {
            for(int j = i+1; j < n; ++j)
            {
                for(int k = j+1; k < n; ++k)
                {
                    if(((treeX[i]+treeX[j]+treeX[k])%3)==0)
                        if(((treeY[i]+treeY[j]+treeY[k])%3)==0)
                            ++ans;
                    //ans += ((((treeX[i]+treeX[j]+treeX[k])%3)==0) && ((treeY[i]+treeY[j]+treeY[k])%3)==0));
                }
            }
        }
        
        
        cout << "Case #" << task << ": " << ans << endl; 
    }
}

