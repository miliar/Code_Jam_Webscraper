/* 
 * File:   main.cpp
 * Author: sharad
 *
 * Created on 13 February, 2011, 2:47 PM
 */

#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

map<string,char> combines;
map<string,bool> opposes;

int main(int argc, char** argv) {
    

    int n_testCases = 0;
    cin >> n_testCases;

    for(int i=0; i < n_testCases; ++i) {
        
        int C, D, N;
        combines.clear(); opposes.clear();
        cin >> C;
        for(int j=0; j< C; j++) {
            string combineset = "";
            cin >> combineset;
            string key1 = combineset.substr(0,2);
            string key2 = key1.substr(1,1) + key1.substr(0,1);
            combines[key1] = combineset[2];
            combines[key2] = combineset[2];
        }
        
        cin >> D;
        for(int j=0; j< D; j++) {
            string opposeSet = "";
            cin >> opposeSet;
            string key2 = opposeSet.substr(1,1) + opposeSet.substr(0,1);
            opposes[key2] = true;
            opposes[opposeSet] = true;
        }

        cin >> N;
        string input;
        cin >> input;
        string output;

        for(int j=0; j<N; j++) {

            output.append(1,input[j]);
            
            bool combine_str = output.length() > 1 ? true: false;
            
            while(combine_str) { // combine the possible combinations
                int curLen = output.length();
                string key = output.substr(curLen-2,2);
                map<string,char>::iterator it;
                it = combines.find(key);
                if(it != combines.end()) {
                    string replacement(1,it->second);
                    output = output.replace(curLen-2,2,replacement);
                    combine_str = output.length() > 1 ? true: false;
                } else {
                    combine_str = false;
                }
                
            }

            // eliminate based on the last string
            bool eliminate_str = output.length() > 1 ? true: false;
            if(eliminate_str) {
                int start_index = 0;
                int end_index = output.length()-1;
                while(eliminate_str && start_index < end_index) {
                    string key = output.substr(start_index,1) + output.substr(end_index,1);
                    map<string,bool>::iterator it;
                    it = opposes.find(key);
                    if(it != opposes.end()) {
                        output.clear();
                        eliminate_str = false;
                    } else {
                        start_index++;
                    }
                }   
            }
        }

        cout << "Case #" << i << ": ";
        string finalOutPut("[");
        for(int j=0; j<output.length(); j++) {
            finalOutPut += output.substr(j,1) + ", ";
        }
        if(finalOutPut.length() > 1) {
            finalOutPut = finalOutPut.substr(0,finalOutPut.length()-2);
        }
        cout << finalOutPut << "]"<<endl;

    }

    return 0;
}

