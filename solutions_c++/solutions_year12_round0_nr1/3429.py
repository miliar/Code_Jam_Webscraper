// Code jam 2012
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    string fname1 = "A-small-attempt0.txt";
    string fname2 = "tonguesOutput.txt";
    
    ifstream file(fname1.c_str());
    ofstream outFile(fname2.c_str());
    

    string googlerese = " yhesocvxduiglbkrztnwjpfmaq";
    string str, output;
    int alphSize = 26;
    int len, index;
    
    int count;
    file >> count;
    getline (file, str); // clear existing line of count
    
    for (int x=1; x<=count; x++)
    {
        getline(file, str);
        output = "";
        len = str.length();
        
        for (int i = 0; i < len; i++)
        {
            if (str[i] == ' ')
               output += ' ';
            else {
               index = str[i] - 'a' + 1;
               output += googlerese[index];
            }   
            
        }
        
        outFile << "Case #" << x <<": " << output << endl;
        
        
        
    }
    
    
    
    file.close();
    outFile.close();
    
    
    system("pause");
    return 0;
}
