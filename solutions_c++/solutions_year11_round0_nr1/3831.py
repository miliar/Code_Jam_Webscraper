#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

#include <stdio.h>

void grabline(char *dest, int len, FILE *f)
{
    char c = fgetc(f);
    int cnt = 0;

    while(c != EOF && c != '\n')
    { 
        if(cnt > len-1)
        break;
        dest[cnt] = c;
        cnt++;
        c = fgetc(f);
        
    } 
    dest[cnt] = '\0';
}

struct sort_pred {
    bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
        return left.first < right.first;
    }
};

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while(std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}


std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    return split(s, delim, elems);
}


int main(int argc, char *argv[])
{
    //cout << "Opening " << argv[1] << endl;
    FILE* fFile = fopen(argv[1], "r");

    char line[1024];
    int lineLength = 1024;

    int cases;

    fscanf(fFile, "%d\n", &cases);

    //cout << "cases " << cases << endl;

    for(int jjj=0; jjj<cases; jjj++)  
    {
        int timeTaken = 0;
        
        grabline(line, lineLength, fFile);
        string sentence(line);
        vector<string>tokens = split(sentence, ' ');
        tokens.erase(tokens.begin());
        int steps = tokens.size()/2;
        //vector<int> stepTime
        //cout << "Tokens size = " << tokens.size() << endl;
        if(steps*2 != tokens.size()) cout << "Mismatched input!!!!" << endl;
       
        int last[2]= {-1,-1};
        int pos[2] = {1,1};
        int curTime = 0;
        
        for(int i=0; i<steps; i++)
        {
            int idx;
            if(tokens[i*2] == "O")
            {
                idx = 0;
            }
            else
            {
                idx = 1;
            }

            int dP = atoi(tokens[i*2+1].c_str());
            int timeTaken;
            if(last[idx] == -1)
            {
                timeTaken = abs(dP - pos[idx]) + 1;
                if(timeTaken <= curTime)
                {
                    curTime += 1; //Time for pressing switch
                }
                else
                {
                    curTime = timeTaken;
                }
            }
            else
            {
                timeTaken = abs(dP - pos[idx]) + 1;
                if(timeTaken + last[idx] <= curTime)
                {
                    curTime += 1;
                }
                else
                {
                    curTime = timeTaken + last[idx];
                }
            }
            pos[idx] = dP;
            last[idx] = curTime;
            //cout << idx << " " <<pos[idx] << " " <<curTime << endl;
        }
        cout << "Case #" << jjj+1 << ": " << curTime << endl;
    }
    
    fclose(fFile);

    return 0;
}