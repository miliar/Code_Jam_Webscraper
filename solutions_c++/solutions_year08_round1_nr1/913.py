#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;


ifstream fcin("A-small-attempt.in");
ofstream fcout("A-small-attempt.out");

int main()
{
    
    vector<int> vector1;
    vector<int> vector2;
    
    int suma = 0, a, c, testCases, large,number, index = 1;
    
    
    fcin >> testCases;
    
    for(int b = 0; b < testCases; b++){
    
        suma = 0;
        
        fcin >> large;
    
    
        for(c = 0; c < large; c++){
            fcin >> number;
            vector1.push_back(number);
        }
        
        for(c = 0; c < large; c++){
            fcin >> number;
            vector2.push_back(number);
        } 
        
                sort(vector1.begin(),vector1.end());
        sort(vector2.begin(),vector2.end());
        
        for(a = 0; a < large; a++)
            suma += vector1[a] * vector2[large-a-1];
        
        fcout << "Case #" << index << ": " << suma << endl;
        index++;
        vector1.clear();
        vector2.clear();
    }
    
    

    system("pause");
}
