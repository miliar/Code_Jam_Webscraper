#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char mapping[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'}; 

int main(int argc, char **argv)
{
    ifstream iFile("input.txt");
    if(iFile.fail())
    {
        cout<<"Unable to open input file!"<<endl;
        exit(1);
    }
    
    char temp[255];
    iFile.getline(temp, 255);
    int rowNo = atoi(temp);
    ofstream oFile("output.txt");
    for(int j=0; j<rowNo; j++)
    {
        iFile.getline(temp, 255);
        string input(temp);
        char cInput[input.size()];
        strcpy(cInput, input.c_str());
        
        for(int i=0;i<input.size();i++)
        {
            if(cInput[i]==' ')
                continue;
            cInput[i] = mapping[((int)cInput[i]) - 97];
        }
        oFile<<"Case #"<<(j+1)<<": "<<cInput<<endl;
    }
    oFile.close();
    iFile.close();
    return 0;
}
