#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <stdlib.h>
#include <list>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream inFile(argv[1], ifstream::in);
    ofstream outFile(argv[2], ofstream::out);
    string sLine; int T;

    //The function prototype for getline is:
    //istream& getline(istream& is, string& s, char delimiter = '\n');
    //There's a conversion operator defined that converts an istream to a void*, 
    //which is further converted to a bool by using a simple != NULL rule. 
    //The void* converter will be a non-NULL value if the stream is ready and NULL if an error occurs.
    if(getline(inFile, sLine)) //!! global "getline()"
    {
        //Do here whatever you need to do
        istringstream buffer(sLine, istringstream::in);
        buffer >> T;
    }
    else{
        cout << "ERROR in file format!" << endl;
        return -1;
    }

    for(int i0 = 0; i0 < T; i0 ++){
        int C, D, N;        
        if(getline(inFile, sLine))
        {
            char *line = (char*)sLine.c_str();
            C = atoi(strtok(line, " "));
            char **comb = NULL;
            if(C > 0){
                comb = new char*[C];
                for (int i1 = 0; i1 < C; i1 ++)
                    comb[i1] = new char[3];
                line = strtok(NULL, " "); int idx = 0;
                for(int i1 = 0; i1 <= strlen(line) - 3; i1 += 3)
                {
                    comb[idx][0] = line[i1];
                    comb[idx][1] = line[i1+1];
                    comb[idx][2] = line[i1+2];
                    idx ++; 
                }
            }
            D = atoi(strtok(NULL, " "));
            char **opp = NULL;
            if(D > 0){
                opp = new char*[D];
                for (int i1 = 0; i1 < D; i1 ++)
                    opp[i1] = new char[2];
                line = strtok(NULL, " "); int idx = 0;
                for(int i1 = 0; i1 <= strlen(line) - 2; i1 += 2)
                {
                    opp[idx][0] = line[i1];
                    opp[idx][1] = line[i1+1];
                    idx ++; 
                }
            }
            N = atoi(strtok(NULL, " "));
            string input = strtok(NULL, " ");
            
            int flags[26];
            for(int i1 = 0; i1 < 26; i1 ++) flags[i1] = 0;
            list<char> queue;
            
            for(int i1 = 0; i1 < N; i1 ++){
                char curr = input[i1];
                flags[curr-65] ++;
                
                if(queue.empty()) queue.push_back(curr);
                else{ //first check combine then oppose
                    char prev = queue.back(); int i2 = 0;
                    for(; i2 < C; i2 ++){
                        if(comb[i2][0] == prev && comb[i2][1] == curr)
                        {
                            //cout << "Here 1 " << comb[i2][2] << endl;
                            queue.pop_back();
                            queue.push_back(comb[i2][2]);
                            flags[comb[i2][0]-65] --;
                            flags[comb[i2][1]-65] --;
                            flags[comb[i2][2]-65] ++;
                            break;
                        }
                        if(comb[i2][0] == curr && comb[i2][1] == prev)
                        {
                            //cout << "Here 2 " << comb[i2][2] << endl;
                            queue.pop_back();
                            queue.push_back(comb[i2][2]);
                            flags[comb[i2][0]-65] --;
                            flags[comb[i2][1]-65] --;
                            flags[comb[i2][2]-65] ++;
                            break;
                        }
                    }//for
                    if(i2 == C) queue.push_back(curr);
                    for(i2 = 0; i2 < D; i2 ++){
                        if(opp[i2][0] == opp[i2][1] && flags[opp[i2][0]-65] >= 2)
                        { 
                            //cout << "Here 3" << endl;
                            queue.clear(); 
                            for(int i3 = 0; i3 < 26; i3 ++) flags[i3] = 0;
                            break; 
                        }
                        else if(flags[opp[i2][0]-65] >= 1 && flags[opp[i2][1]-65] >= 1)
                        { 
                            //cout << "Here 4" << opp[i2][0] << " " << opp[i2][1] << endl;
                            queue.clear(); 
                            for(int i3 = 0; i3 < 26; i3 ++) flags[i3] = 0;
                            break; 
                        }
                    }//for
                }//else
                /*list<char>::iterator it;
                for ( it=queue.begin() ; it != queue.end(); it++ )
                    cout << " " << *it;
                cout << endl;*/
            }//for(int i1 = 0; i1 < N; i1 ++)
            //cout << endl;
            
            outFile << "Case #" << i0+1 << ": ";
            if(queue.empty())
                outFile << "[]" << endl;  
            else{
                outFile << "[";
                outFile << queue.front();
                queue.pop_front();
                while(!queue.empty()){
                    outFile << ", "; outFile << queue.front();
                    queue.pop_front();
                }
                outFile << "]" << endl;
            }
            
        }//if(getline(inFile, sLine))
        else{
            cout << "ERROR in file format!" << endl;
            return -1;
        } 
    }//for(int i0 = 0; i0 < T; i0 ++)
}
