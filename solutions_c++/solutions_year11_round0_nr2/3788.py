//============================================================================
// Name        : magicka.cpp
// Author      : Aziz
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream> //Standard input/output
#include <fstream> //File input/output
#include <cstdlib> //C library
#include <cmath> //Math library
#include <algorithm> //Some algorithms like sorting
#include <vector> //Vectors (Array lists)
#include <string> //Strings
#include <map> //Maps
#include <set> //Maps

using namespace std;

ifstream fin ("magicka.in");
ofstream fout ("magicka.out");

int T;
int main() {
	fin >> T;
	for(int y = 0; y < T; y++){
            int t;
            string tS;
            set<pair<char,char> > base, nBase;
            map<pair<char,char>, char > trans;
            vector<int> result;
            fin >> t;
            for(int x = 0; x < t; x++){
                    fin >> tS;
                    pair<char, char> temp = make_pair(tS[0],tS[1]);
                    pair<char, char> temp2 = make_pair(tS[1],tS[0]);
                    base.insert(temp);
                    base.insert(temp2);
                    trans[temp] = tS[2];   
                    trans[temp2] = tS[2];                    
            }
            fin >> t;
            for(int x = 0; x < t; x++){
                    fin >> tS;
                    pair<char, char> temp = make_pair(tS[0],tS[1]);
                    pair<char, char> temp2 = make_pair(tS[1],tS[0]);
                    nBase.insert(temp);                   
                    nBase.insert(temp2);                   
            }
            fin >> t >> tS;
            for(int x = 0; x < t; x++){
                    result.push_back(tS[x]);
                    pair<int,int> temp;
                    if(result.size() > 1)
                        temp = make_pair(result[result.size()-2], result.back());
                    while((result.size() > 1) && (base.find(temp) != base.end())){
                          result.pop_back();
                          result.pop_back();
                          result.push_back(trans[temp]);
                          if(result.size() > 1)
                              temp = make_pair(result[result.size()-2], result.back());
                    }
                    if(result.size() > 1)
                        for(int z = 0; (result.size()>1) && z < (result.size()-1); z++)
                                if(nBase.find(make_pair(result[z],result.back())) != nBase.end())
                                                                                  result.clear();
                                                                                  

            }
            if(result.size()>0){
                fout << "Case #" << y+1 << ": [";
                for(int x = 0; x < (result.size()-1);x++)
                        fout << (char)result[x] << ", ";
                fout << (char)result[result.size()-1] << "]\n";
                }
            else
                fout << "Case #" << y+1 << ": []\n";
        }
    return EXIT_SUCCESS;
}
