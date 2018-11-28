#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;



string getArg(string line, int i)
{
    if(--i != 0)
    {
        line = line.substr(line.find(' ')+1);
        line = getArg(line, i);
    }
    
    if(line.find(' ') == line.npos)
        return line;
    else
        return line.substr(0, line.find(' '));
}



int main(int argc, char *argv[])
{
    vector<string> dictionary;
    unsigned int L_, D_, N_;
    string buff;

    // Get arguments
    getline(cin, buff);
    L_ = atoi(getArg(buff, 1).c_str());
    D_ = atoi(getArg(buff, 2).c_str());
    N_ = atoi(getArg(buff, 3).c_str());
    
    // Setup dictionary
    for(unsigned int i = 0; i< D_; i++)
    {
        getline(cin, buff);
        dictionary.push_back(buff);
    }

    for(unsigned int i = 0; i< N_; i++)
    {
        unsigned int ret = 0;
        getline(cin, buff); 
        vector<string> tokens;

        for(unsigned int j=0; j < L_; j++)
        {
            string symbols;
            int tail;
            if(buff[0] != '(')
            {
                tokens.push_back(buff.substr(0,1));
                buff = buff.substr(1, buff.npos);
                continue;
            }
            tail = buff.find(')');
            symbols = buff.substr(1, tail-1);
            tokens.push_back(symbols);
            if(tail != buff.npos)
                buff = buff.substr(tail+1, buff.npos);
        }

        for(unsigned int j = 0; j< D_; j++)
        {
            bool validword = true;
            for(unsigned int k = 0; k < L_; k++)
            {
                if(tokens[k].find(dictionary[j][k]) == tokens[k].npos)
                {
                    validword = false;
                    break;
                }
            }
            if(validword)
            {
                ret += 1;
            }
        }

        cout << "Case #" << i+1 << ": " << ret << endl;

    }


//    system("pause");
    return 0;
}