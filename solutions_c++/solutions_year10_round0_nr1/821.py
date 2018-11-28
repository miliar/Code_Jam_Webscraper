#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("D:\A-large.in");
    ofstream fout("D:\A-large.out");
    int T, N, K;
    fin >> T;
    for (int i = 1 ; i <= T; i++)
    {  
       fin >> N >> K;
       bool ans = true;
       while (true)
       {
             if (K % 2 == 0) {ans = false; break;}
             K >>= 1;         
             N -= 1;
             if (N == 0) break;
       }
    
       fout << "Case #" << i << ": ";
       if (ans == true) fout << "ON" << endl;
       else fout << "OFF" << endl;
    }
}
