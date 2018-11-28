#include <iostream>

using namespace std;

unsigned long long ans = 0;

unsigned long long A;

int C;

int N;
int M;

int main()
{
    cin >> C;
    
    for(int i = 1; i <= C; ++i)
    {
        cin >> N >> M >> A;
        
        /// Triangle anchored to the origin - maybe
        
        bool ansFound = false;
        
        for(int p1x = 0; p1x <= 0; ++p1x)
        {
            for(int p1y = 0; p1y <= 0; ++p1y)
            {
                for(int p2x = 0; p2x <= N; ++p2x)
                {
                    if(ansFound)
                        break;
                    
                    for(int p2y = 0; p2y <= M; ++p2y)
                    {
                        if(ansFound)
                            break;
                        
                        for(int p3x = 0; p3x <= N; ++p3x)
                        {
                            if(ansFound)
                                break;
                            
                            for(int p3y = 0; p3y <= M; ++p3y)
                            {
                                /*
                                int dx21 = p2x - p1x;
                                int dx31 = p3x - p1x;
                                
                                int dy21 = p2y - p1y;
                                int dy31 = p3y - p1y;
                                
                                if(dy21*dx31 == dx21*dy31)
                                {
                                    continue;
                                }
                                */
                                /// Determinant method for calc of 2*area
                                
                                int a = abs((p2x*p1y-p1x*p2y) + (p3x*p2y-p2x*p3y) + (p1x*p3y-p3x*p1y));
                                        
                                if(a == A)
                                {
                                    cout << "Case #" << i << ": " << p1x << " " << p1y << " " << p2x << " " << p2y << " " << p3x << " " << p3y << endl;
                                    
                                    ansFound = true;
                                    break;
                                }
                            
                            }
                            
                        }
                            
                    }
                }   
            }
        }
        
        if(!ansFound)
        {
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        }
        
        
    }
}
