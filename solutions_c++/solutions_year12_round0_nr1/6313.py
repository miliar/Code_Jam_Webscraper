//
//  main.cpp
//  Speaking In Tongues

#include <iostream>
#include <fstream>

using namespace std;

int Googlerese[26] = { 
    -24,
    -6,
    -2,
    -15,
    -10,
    3,
    -15,
    -16,
    5,
    -11,
    2,
    5,
    1,
    12,
    4,
    -2,
    -9,
    -2,
    5,
    -3,
    11,
    6,
    17,
    11,
    24,
    9
};

int main (int argc, const char * argv[])
{
    int n, i = 1;
    char str[255];
    ifstream infile;
    ofstream outfile;
    
    infile.open("A-small-attempt0.in");
    outfile.open("output.txt");
    
    
    infile.getline(str, 255);
    n = atoi(str);
    
    for (; n>0; n--) {
        
        infile.getline(str, 255);

        int m = (int)strlen(str);
                
        for (int j =0; j < m; j++) 
        {
            if (str[j] == ' ') continue;
            str[j] -= Googlerese[str[j] - 97];
        }
        
        cout << "Case #" << i << ": " << str << endl;
        outfile << "Case #" << i << ": " << str << endl;
        i++;
    }
    getchar();
    
    return 0;
}
