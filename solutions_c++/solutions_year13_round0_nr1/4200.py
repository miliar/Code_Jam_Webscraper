
#include <iostream>
#include <fstream>
#include <map>
#include <vector>


bool Won(std::vector<bool>& GRID)
{
    for (int i = 0; i < 4; ++i)
    {
        bool rowwon = true;
        bool colwon = true;
        for(int j = 0; j < 4; ++j)
        {
            rowwon &= GRID[i + j *4];
            colwon &= GRID[j + i *4];
        }
        if (rowwon || colwon)
            return true;
    }

    bool diag1 = true;
    bool diag2 = true;

    for (int i = 0; i < 4; ++i)
    {
        diag1 &= GRID[i + i * 4];
        diag2 &= GRID[(3 - i) * 4 + i];
    }
    if (diag1 || diag2)
        return true;
}

int main(int argc, char *argv[])
{
    std::string testcase ("/home/gquerol/Test/A-large");
    std::string inputfile = testcase + ".in";
    std::string outputfile = testcase + ".out";

    std::ifstream input(inputfile.c_str());
    std::ofstream output(outputfile.c_str(), std::ios_base::out & std::ios_base::trunc);

    std::cout << "reading " << inputfile << std::endl;


    int nbTests;
    input >> nbTests;

    std::vector<bool> GRIDX;
    std::vector<bool> GRIDO;
    GRIDX.resize(16);
    GRIDO.resize(16);


    for (int testIdx = 1; testIdx < nbTests + 1; ++testIdx)
    {
        std::cout << "solving testcase #" << testIdx << std::endl;
        bool hasEmpty = false;

        for(int i = 0; i < 16; ++i)
        {
            GRIDX[i] = false;
            GRIDO[i] = false;

           char nextchar;
           input >>nextchar;
           if(nextchar == '.')
               hasEmpty = true;
           if(nextchar == 'X' or nextchar == 'T')
               GRIDX[i] = true;
           if(nextchar == 'O' or nextchar == 'T')
               GRIDO[i] = true;
        }

        char* result;
        if (Won(GRIDX))
        {
            result = "X won";
        } else if (Won(GRIDO))
        {
            result = "O won";

        } else if (hasEmpty)
        {
            result = "Game has not completed";
        } else
        {
            result = "Draw";
        }


        std::cout << "Case #" << testIdx << ": " << result << std::endl;
        output << "Case #" << testIdx << ": " << result <<  std::endl;

        std::cout << "end solving testcase #" << testIdx << std::endl;
    }


    std::cout << "writing " << outputfile << std::endl;
}
