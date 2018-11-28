
#include <cstring>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream> 
using namespace std;

typedef pair<int, int> PAIR;

void parseInput(const string &inpFile, vector< pair<int, int> > &data){
    ifstream in;
    in.open(inpFile.c_str());
    int tmp, tmp2;
    if (in.is_open()){
        in >> tmp;
        data.reserve(tmp);
        
        cout << "INPUT: \n";
        
        for (int i=0;i<data.capacity();i++){
            in >> tmp >> tmp2;
            cout << tmp << " " << tmp2 << "\n";
            data.push_back(pair<int, int>(tmp, tmp2));
        }
    }
}


void recycledNumbers(const string &inpFile, const string &outFile){
    vector< pair<int, int> > data;
    parseInput(inpFile, data);
    
    ofstream out;
    out.open(outFile.c_str());
    
    int counter;
    
    for (int k=0;k<data.size();k++){
        counter = 0;
        
        PAIR p = data[k];
        
        for (int i=p.first;i<=p.second;i++){
            stringstream s;
            s << i;
            string str (s.str());
            char tmp;
            int tmpInt;
            
//            cout << i << ": ";
                        
            for (int j=0; j<str.size(); j++){
                tmp = str[0];
                str.erase(0, 1);
                str = str + tmp;
                stringstream s2(str);
                s2 >> tmpInt;
                
//                cout << tmpInt << " ";

                if ((tmpInt >=p.first) && (tmpInt <=p.second) && (tmpInt != i)){
                    counter ++;
                }
            }
            
//            cout << "\n";

        }
        
        out << "Case #" << k+1 << ": " << counter/2 << "\n";
        cout << "Case #" << k+1 << ": " << counter/2 << "\n";
        
    }
}


int main(int argc, const char* argv[]){
    
    recycledNumbers(string(argv[1]), string(argv[2]));
    
    return 0;
}

