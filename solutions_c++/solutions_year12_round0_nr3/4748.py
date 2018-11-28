#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int CantDigists;

int NumberDigits (int N)
{
    int Quantity(0);
    
    while (N)
    {
        N /= 10;
        Quantity++;
    }
    
    return Quantity;
}

int Recycle (int N, int Times)
{
    int Aux, Exp;

    Exp = (int)pow(10, Times);
    Aux = N % Exp;
    N /= Exp;
    return (Aux * ((int)pow(10,CantDigists-Times))) + N;
}

int main()
{
    int A, B, T, R, Counter;
    bool Flag;
    
    cin >> T;
    
    for (int i = 1; i <= T; i++)
    {
        cin >> A >> B;
        
        CantDigists = NumberDigits(A);
        Counter = 0;
        if (A > 9)
        {
            for (int j = A; j < B; j++)
            {
                for (int k = j + 1; k <= B; k++)
                {
                    Flag = false;
                    for (int h = 1; h <= CantDigists && !Flag; h++)
                    {
                        R = Recycle (j, h);
                        if (R == k)
                        {
                            Counter++;
                            Flag = true;
                        }
                    }
                }
            }
            cout << "Case #" << i << ": " << Counter << endl; 
        }
        else
            cout << "Case #" << i << ": 0" << endl; 
    }
    
    return EXIT_SUCCESS;
}
