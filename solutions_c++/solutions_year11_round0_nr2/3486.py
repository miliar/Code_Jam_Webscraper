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
        
        int numCombinations = atoi(tokens[0].c_str());
        vector <string>combinations(numCombinations);
        
        int tokenPosition = 1;
        
        for(int c=0; c<numCombinations; c++)
        {
            combinations[c] = tokens[tokenPosition++];
        }
        
        int numDestructors = atoi(tokens[tokenPosition++].c_str());
        vector<string> destructors(numDestructors);
        for(int d=0; d<numDestructors; d++)
        {
            destructors[d] = tokens[tokenPosition++];
        }
        
        int numInvocations = atoi(tokens[tokenPosition++].c_str());
        vector<char> out;
        string invocations(tokens[tokenPosition++]);
        for(int i=0; i<numInvocations; i++)
        {
            if(i==0 || out.size() == 0)
            {
                out.push_back(invocations[i]);
                //cout << "Added " << invocations[i] << endl;
                continue;
            }

            bool matchFound = true;
            char curLetter = invocations[i];
            while(matchFound)
            {
                matchFound = false;
               
                
                for(int ii=0; ii<numCombinations; ii++)
                {
                    size_t pos = combinations[ii].find(curLetter);
                    if(pos == 0 || pos == 1)
                    {
                        //cout << "Found part of combination " << pos << " " << curLetter << " " << combinations[ii] << endl;
                        size_t pos2 = combinations[ii].find(out[out.size()-1]);
                        if(out[out.size()-1] == curLetter)
                        {
                            if(combinations[ii][0] == combinations[ii][1])
                            {
                                //cout << "Found full duplicate match " << out[out.size()-1] << endl;
                                out.pop_back();
                                curLetter = combinations[ii][2];
                                matchFound = true;
                                break;
                            }
                        }
                        else if(pos2 == 0 || pos2 == 1)
                        {
                            //cout << "Found full match " << out[out.size()-1] << endl;
                            out.pop_back();
                            curLetter = combinations[ii][2];
                            matchFound = true;
                            break;
                        }
                        
                    }
                }
                
            }
            out.push_back(curLetter);
            //cout << "Added " << curLetter << endl;
            
            if(out.size() == 1) continue;
            
            
            for(int j=0; j<numDestructors; j++)
            {
                char lastLetter = out[out.size()-1];
                size_t pos = destructors[j].find(lastLetter);
                if(pos == 0 || pos == 1)
                {
                    for(int k=0; k<out.size()-1; k++)
                    {
                        size_t pos2 = destructors[j].find(out[k]);
                        if((pos2 == 0 || pos2 == 1) && pos != pos2)
                        {
                            //cout << "erasing " << destructors[j] << " " << k << endl;
                            out.clear();
                            //cout << "out size " << out.size() << endl;
                            break;
                        }
                    }
                }
            }
           
        }
        
        cout << "Case #" << jjj+1 << ": [";
        for(int j=0; j<out.size(); j++)
        {
            cout << out[j];
            if( out.size()-1 != j)
            {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }
    
    fclose(fFile);

    return 0;
}