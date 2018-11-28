//
//  Qualification Round 2011 - B
//
//  Diogo Tridapall
//

#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <vector>

using namespace std;


struct combine_t{
    string b;
    string c;
};


string combine(const string bases, const vector<combine_t> combinations){
    string c;
    for (int i=0; i<(int)combinations.size(); ++i) {
        if (string::npos!=combinations[i].b.find(bases)){
            c = combinations[i].c;
            break;
        }
    }
    return c;
}


int main (int argc, const char * argv[]){

    string inFileName;
    string outFileName;

    switch (argc) {
        case 2:
            inFileName = argv[1];
            outFileName.assign(inFileName, 0, inFileName.find_last_of(".in")-2);
            outFileName+=".out";
            break;
        default:
            cout << "Usage: " << argv[0] << " inputFile" << endl;
            exit(0);
            break;
    }
    
    fstream inFile(inFileName.c_str(),fstream::in);
    if (!inFile.is_open()) {
        cout << "File " << inFileName << " is not open!" << endl;
        exit(1);
    }
    fstream outFile(outFileName.c_str(),fstream::out);
    if (!outFile.is_open()) {
        cout << "File " << outFileName << " is not open!" << endl;
        exit(1);
    }
    
    
    int T;    
    
    if(!(inFile >> T)){
        cout << "Error, can't read T!" << endl;
        exit(1);
    }
    
    for (int iT = 0; iT < T; ++iT) {
        int C, D, N;
        
        vector<combine_t> combinations;
        if(!(inFile >> C)){
            cout << "Error, can't read C!" << endl;
            exit(1);
        }
        combinations.reserve((size_t)C);
        for (int iC=0; iC<C; ++iC) {
            char c;
            combine_t comb;
            inFile >> c;
            comb.b.push_back(c);
            inFile >> c;
            comb.b.push_back(c);
            inFile >> c;
            comb.c.push_back(c);
            combinations.push_back(comb);
            swap(comb.b[0], comb.b[1]);
            combinations.push_back(comb);
        }
        
        vector<string> opose;
        if(!(inFile >> D)){
            cout << "Error, can't read D!" << endl;
            exit(1);
        }
        opose.reserve((size_t)D);
        for (int iD=0; iD<D; ++iD) {
            char c;
            string op;
            inFile >> c;
            op.push_back(c);
            inFile >> c;
            op.push_back(c);
            opose.push_back(op);
            swap(op[0], op[1]);
            opose.push_back(op);
        }
        

        if(!(inFile >> N)){
            cout << "Error, can't read N!" << endl;
            exit(1);
        }
        string eList;
        for (int iN=0; iN<N; ++iN) {
            char c;
            inFile >> c;
            eList.push_back(c);
            if(1>=eList.size())
                continue;
            {//combine
                string comb = combine(eList.substr(eList.size()-2,2), combinations);
                if (0!=comb.size())
                    eList.replace(eList.end()-2, eList.end(), comb);
            }
            {//clear
                for (int i=0; i<(int)eList.size()-1; ++i) {
                    string pair;
                    pair.push_back(eList.at(i));
                    pair.push_back(eList[eList.size()-1]);
                    if (opose.end()!=find(opose.begin(), opose.end(), pair)){
                        eList.clear();
                        break;
                    }
                }
            }
        }

        
        
        
        
        outFile << "Case #" << iT+1 << ": [";
        for (int i=0; i<(int)eList.size()-1; ++i)
            outFile << eList[i] << ", ";
        if (0!=eList.size()) {
            outFile << eList[eList.size()-1];
        }
        outFile << "]" << endl;
        
    
    }
    
    
    inFile.close();
    outFile.close();
    return 0;
}


















