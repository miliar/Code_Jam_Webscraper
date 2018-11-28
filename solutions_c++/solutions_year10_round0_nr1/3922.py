#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    
    string y;
    
    int T;
    int N;
    long K;
    
    fin >> T;  
    for (int i=0; i<T; i++)
    {  
        fin >> N >> K;    
        
        // convert to some sort of binary
        long cycle = pow(2.0,N);
        if ((K % cycle) == cycle-1)
        {
               y = "ON";
        }
        else
        {
            y = "OFF";
        }
        
        fout << "Case #" << i+1 << ": " << y << endl;
        
    }
    
    
    return 0;
}
    
