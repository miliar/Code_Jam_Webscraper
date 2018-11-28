#include <cstdlib>
#include <iostream>
#include <string>s

using namespace std;

// declaración de prototipo
string intToBinary(string);

int main()
{
    freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
    
    int T, N, pos;
    string K, bin;
    
    cin >> T;
    
    for (int t = 0; t < T; t++) // Tests
    {
        cin >> N >> K;
        
        bin = intToBinary(K);
        if (bin.length() < N)
           cout << "Case #" << t + 1 << ": OFF" << endl;
        else
        {
            bin = bin.substr(bin.length() - N);
            pos = bin.find("0"); 
            if (pos > -1)
               cout << "Case #" << t + 1 << ": OFF" << endl;
            else
               cout << "Case #" << t + 1 << ": ON" << endl; 
        }
    }
    
    /*string T;
    cin >> T;
    while (T != "0")
    {
          cout << T << " - " << intToBinary(T) << endl;
          cin >> T;
    }*/
    
    return 0;
    
}


string intToBinary(string num)
{
       string aux = num;
       string aux2;
       string bin = "";
       size_t found;
       int val;
       int x;
       
       while (aux != "0" && aux != "1")
       {
           aux2 = "";
           val = 0;
           for (int i = 0; i < aux.length(); i++)
           {
               val = (val%2) * 10 + ((int)aux[i]-48);
               aux2 = aux2 + (char)(val/2+48);
           }
           found = aux2.find_first_not_of("0");
           aux = aux2.substr(found);
           val = val%2;
           bin = (char)(val+48) + bin;
       }
       bin = aux + bin;
        
       return bin;
}
