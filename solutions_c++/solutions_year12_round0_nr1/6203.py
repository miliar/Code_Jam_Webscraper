#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    char map[27][2];
    map[0] [0] = 'a'; map[0] [1] = 'y';
    map[1] [0] = 'b'; map[1] [1] = 'n';
    map[2] [0] = 'c'; map[2] [1] = 'f';
    map[3] [0] = 'd'; map[3] [1] = 'i';
    map[4] [0] = 'e'; map[4] [1] = 'c';
    map[5] [0] = 'f'; map[5] [1] = 'w';
    map[6] [0] = 'g'; map[6] [1] = 'l';
    map[7] [0] = 'h'; map[7] [1] = 'b';
    map[8] [0] = 'i'; map[8] [1] = 'k';
    map[9] [0] = 'j'; map[9] [1] = 'u';
    map[10][0] = 'k'; map[10][1] = 'o';
    map[11][0] = 'l'; map[11][1] = 'm';
    map[12][0] = 'm'; map[12][1] = 'x';
    map[13][0] = 'n'; map[13][1] = 's';
    map[14][0] = 'o'; map[14][1] = 'e';
    map[15][0] = 'p'; map[15][1] = 'v';
    map[16][0] = 'q'; map[16][1] = 'z';
    map[17][0] = 'r'; map[17][1] = 'p';
    map[18][0] = 's'; map[18][1] = 'd';
    map[19][0] = 't'; map[19][1] = 'r';
    map[20][0] = 'u'; map[20][1] = 'j';
    map[21][0] = 'v'; map[21][1] = 'g';
    map[22][0] = 'w'; map[22][1] = 't';
    map[23][0] = 'x'; map[23][1] = 'h';
    map[24][0] = 'y'; map[24][1] = 'a';
    map[25][0] = 'z'; map[25][1] = 'q';
    map[26][0] = ' '; map[26][1] = ' ';
    
    ifstream ipFile("input.in");
    ofstream opFile("result.out");
    
    string line;
    int i,j,ncase;
    
    getline(ipFile, line);
    int cases = atoi(line.c_str());
    
    ncase = 1;
    //cout << cases << endl;
    
    if ( ipFile.is_open())
    {
         while (ipFile.good() && ncase <= cases)
         {
               opFile << "Case #" << ncase << ": ";
               getline (ipFile, line);
               for (i =0; i < line.length() ; i++)
               {
                   for(j=0; j<26; j++)
                      if (map[j][1] == line.at(i))
                         break;
                   opFile << map[j][0];      
               }
               ncase++;
               if (ncase <= cases )
                  opFile << endl;
               //cout << line << endl;
               //system("pause");               
         }         
         ipFile.close();
    }
    opFile.close();
    
    return 0;
}   
