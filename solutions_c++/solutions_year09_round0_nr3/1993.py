#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iomanip>
using namespace std;
   
string find_string = "welcome to code jam";

// number of sub-sentences of length i ending in character j
int ways[19][500];
 
int main()
{
    int T;
    string line;
    
    cin >> T;
    getline(cin, line);
    for (int i = 0; i < T; i++)
    {
        memset(ways, 0, sizeof(ways));
        getline(cin, line);
        
        for (size_t j = 0; j < line.size(); j++)
        {
            if (line[j] == 'w')
                ways[0][j] = (ways[0][j] + 1) % 10000;
            else
                for (size_t k = 1; k < find_string.size(); k++)
                    if (find_string[k] == line[j])
                        ways[k][j] = (ways[k][j] + ways[k - 1][j - 1]) % 10000;
            
            if (j > 0)
                for (size_t k = 0; k < find_string.size(); k++)
                    ways[k][j] = (ways[k][j] + ways[k][j - 1]) % 10000;
        }
        
        cout << "Case #" << i + 1 << ": " << setw(4) << setfill('0')
             << ways[find_string.size() - 1][line.size() - 1] << endl;
    }
    
    return 0;    
}
