#include <iostream>
#include <string>
#include <vector>

using namespace std;

int vrsta (long long x, long long y)
{
    x = x % 3;
    y = y % 3;
    if ( (x == 0) && (y == 0) )
       return 0;
    if ( (x == 0) && (y == 1) )
       return 1;
    if ( (x == 0) && (y == 2) )
       return 2;
    if ( (x == 1) && (y == 0) )
       return 3;
    if ( (x == 1) && (y == 1) )
       return 4;
    if ( (x == 1) && (y == 2) )
       return 5;
    if ( (x == 2) && (y == 0) )
       return 6;
    if ( (x == 2) && (y == 1) )
       return 7;
    if ( (x == 2) && (y == 2) )
       return 8;
}                  

int main()
{
    int N;
    cin >> N;
    
    for (int q = 0; q < N; q++)
    {
        long long n, A, B, C, D, x0, y0, M, rj = 0, X, Y;
        vector <long long> x (9), y (9), tip (9,0);
        
        x[0]=0; x[1]=0; x[2]=0; x[3]=1; x[4]=1; x[5]=1; x[6]=2; x[7]=2; x[8]=2;
        y[0]=0; y[1]=1; y[2]=2; y[3]=0; y[4]=1; y[5]=2; y[6]=0; y[7]=1; y[8]=2;
        
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        
        X = x0; Y = y0;
        tip[vrsta(X,Y)]++;
        for (int i = 1; i < n; i++)
        {
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
            tip[vrsta(X,Y)]++;
        } 
        
        for (int i = 0; i < 9; i++)
            if ( ((x[i]+x[i]+x[i])%3 == 0)
               && ((y[i]+y[i]+y[i])%3 == 0) && tip[i] >= 3)
                  rj += (tip[i]*(tip[i]-1)*(tip[i]-2))/6;
        
        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++)
                if (j != i)
                   if ((tip[i] >= 2) && (tip[j] >= 1))
                      if (((x[i]+x[i]+x[j])%3 == 0)
                         && ((y[i]+y[i]+y[j])%3 == 0))
                            rj += (tip[i]*(tip[i]-1)*tip[j])/2;
        
        for (int i = 0; i < 9; i++)
            for (int j = i+1; j < 9; j++)
                for (int k = j+1; k < 9; k++)
                    if ((tip[i] >= 1) && (tip[j] >= 1) && (tip[k] >= 1))
                       if (((x[i]+x[j]+x[k])%3 == 0)
                          && ((y[i]+y[j]+y[k])%3 == 0))
                             rj += tip[i]*tip[j]*tip[k];
        
        cout << "Case #" << q+1 << ": " << rj << endl;
    }
    
    return 0;
}                                                  
        
                  
                
        
        
        
        
           
        
