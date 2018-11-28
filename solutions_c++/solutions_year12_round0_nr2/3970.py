#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
using namespace std;

int main() {
    
    ifstream infile("B-large.in",ios::in);
    ofstream outfile("result2.txt",ios::out);
    
    if(!infile.is_open()) {
        return -1;
    }
    else {
        int testcase;
        infile >> testcase;
        for(int i=0; i<testcase; i++) {
            int numgooglers;
            int numsurprise;
            int expectedscore;
            int result = 0;
            infile >> numgooglers >> numsurprise >> expectedscore;
            
            for(int j=0; j<numgooglers; j++) {
                int currentscore;
                infile >> currentscore;
                if( ceil(currentscore/3.0) >= expectedscore ) {
                    result++;
                }
                else {
                    if( ceil(currentscore/3.0) >= (expectedscore-1) && currentscore>1 ) {
                        if(currentscore%3==0 ||currentscore%3==2 ) {
                            if(numsurprise>0) {
                                numsurprise--;
                                result++;
                            }
                        }
                    }
                }
            }
            outfile << "Case #" << i+1 << ": " << result << "\n";
            
        }
    }
    return 0;
}
