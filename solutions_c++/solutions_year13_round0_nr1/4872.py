#include <fstream>
#include <iostream>
#include <string>

using namespace std;
void getStatus(char b[4][4]);
int main(int argc, char* argv[])
{
    if (argc != 2) { 
        std::cout << "Usage is *.exe inout.txt";
        std::cin.get();
        exit(0);
    }
   string line;
    int numberOfTC;
   ifstream myfile (argv[1]);
   if (myfile.is_open())
   {

       if(myfile.good())
       {
            getline (myfile,line);
            numberOfTC = atoi(line.c_str());
       }
       char b[4][4];
       for(int k = 0; k < numberOfTC; ++k)
       {
           for (int p =0; p<4; ++p)
           {
                getline (myfile,line);
                for (int q =0; q<4; ++q)
                {
                    b[p][q] = line[q];
                }
           }
           getline (myfile,line);
           std ::cout << "Case #" << k+1 << ": ";
           getStatus(b);
       }
    myfile.close();
   }
   return 0;
}

//2a+2b = 10
//a+3b = 11
//4b = 12
//4a = 8
//3a+b = 9
//// 3*2=6 4*2 = 8
//// 3*3=9 4*3 = 12
void getStatus(char b[4][4])
{
    bool draw = true; 
    // rows
    for(int i=0; i<4; i++)
    {
        int sumX = 0;
        int sumO = 0;
        for(int j=0; j<4; j++)
        {
            if(b[i][j] == 'X')
            {
                sumX +=1;
            }
            if(b[i][j] == 'O')
            {
                sumO +=1;
            }
            if(b[i][j] == 'T')
            {
                sumX +=1;
                sumO +=1;
            }
            if(b[i][j] == '.')
            {
                draw = false;
                break;
            }
        }
        if(sumX == 4)
        {
            std::cout << "X won" << std::endl;
            return;
        }
        if(sumO == 4)
        {
            std::cout << "O won" << std::endl;
            return;
        }
    }

    // coloumns
    for(int j=0; j<4; j++)
    {
        int sumX = 0;
        int sumO = 0;
        for(int i=0; i<4; i++)
        {
            if(b[i][j] == 'X')
            {
                sumX +=1;
            }
            if(b[i][j] == 'O')
            {
                sumO +=1;
            }
            if(b[i][j] == 'T')
            {
                sumX +=1;
                sumO +=1;
            }
            if(b[i][j] == '.')
            {
                draw = false;
                break;
            }
        }
        if(sumX == 4)
        {
            std::cout << "X won" << std::endl;            
            return;
        }
        if(sumO == 4)
        {
            std::cout << "O won" << std::endl;            
            return;
        }
    }

    {
        int sumX = 0;
        int sumO = 0;

        for(int i=0; i<4; ++i)
        {
            if(b[i][i] == 'X')
            {
                sumX +=1;
            }
            if(b[i][i] == 'O')
            {
                sumO +=1;
            }
            if(b[i][i] == 'T')
            {
                sumX +=1;
                sumO +=1;
            }
            if(b[i][i] == '.')
            {
                draw = false;
                break;
            }

        }
        if(sumX == 4)
        {
            std::cout << "X won" << std::endl;
            return;
        }
        if(sumO == 4)
        {
            std::cout << "O won" << std::endl;
            return;
        }    
    }

        {
        int sumX = 0;
        int sumO = 0;

        for(int i=0; i<4; ++i)
        {
            if(b[3-i][i] == 'X')
            {
                sumX +=1;
            }
            if(b[3-i][i] == 'O')
            {
                sumO +=1;
            }
            if(b[3-i][i] == 'T')
            {
                sumX +=1;
                sumO +=1;
            }
            if(b[3-i][i] == '.')
            {
                draw = false;
                break;
            }
        }
        if(sumX == 4)
        {
            std::cout << "X won" << std::endl;            
            return;
        }
        if(sumO == 4)
        {
            std::cout << "O won" << std::endl;            
            return;
        }    
    }
    if(draw == true)
    {
        std::cout << "Draw" << std::endl;
    }
    else
    {
        std::cout << "Game has not completed" << std::endl;
    }
}

