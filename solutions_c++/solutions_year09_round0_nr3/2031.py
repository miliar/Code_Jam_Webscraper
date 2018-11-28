#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;
string message_("welcome to code jam");

int countOrderedString(string m)
{
    unsigned int ret=1;
    for(unsigned int i=0; i< message_.size()-1; i++)
    {
        int tail = m.find(message_[i+1]);
        ret = ret * tail;
        m = m.substr(tail, m.npos);
    }
    ret = ret * m.length();
    return ret;
}

int countPhrases(string &m, int start, int stage)
{
    unsigned int ret=0;

    for(unsigned int i=start; i < m.length(); i++)
    {
        if(message_[stage] == m[i])
        {
            if(stage == message_.length()-1)
                ret += 1;
            else
            {
                ret += countPhrases(m, i+1, stage+1);
            }
        }
    }

    return ret;
}

int main(int argc, char* argv[])
{
    string line;
    unsigned int N_;

    getline(cin, line);
    N_ = atoi(line.c_str());
    

    for(unsigned int i=0; i<N_; i++)
    {
        char buff[256];
        getline(cin, line);
        string str_buf;
        bool done=false;
        int ret; 
        for(unsigned int j=0; j< line.length(); j++)
        {
            if(message_.find(line[j]) != message_.npos)
                str_buf.push_back(line[j]);
        }
        line = str_buf;
        if(line.find('w') != line.npos)
            line = line.substr(line.find('w'), line.npos);

        if(line.length() < message_.length())
            ret = 0;
        else
            ret = countPhrases(line, 0, 0);

        sprintf_s(buff, "Case #%d: %04d", i+1, ret % 10000);
        cout << buff << endl;
    }

    //system("pause");
	return 0;
}

