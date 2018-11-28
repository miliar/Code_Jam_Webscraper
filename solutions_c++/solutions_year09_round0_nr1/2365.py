#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


const int SIZE = 5005;




int main()
{
    ifstream fin("A.in");
    ofstream fout("A.out");

    int L,D,N;
    fin>>L>>D>>N;
    string Words[SIZE];
    for(int w=0; w<D; w++)    // inputting the dictionary words
        fin>>Words[w];
    

    for(int x=1; x<=N; x++) {
        string OkWords[SIZE][2];
        int current=1;

        for(int i=0; i<D; i++)
            OkWords[i][0]=Words[i];
        int oldInd = D, newInd = 0;
        for(int i=0; i<L; i++) {
            vector<char> possibleLetters;
            char ch; fin>>ch;
            if(ch=='(') {
                fin>>ch;
                while(ch!=')') {
                    possibleLetters.push_back(ch);
                    fin>>ch;
                }
            }
            else
                possibleLetters.push_back(ch);
            
            for(int j=0; j<oldInd; j++) {
                bool isOk=false;
                for(int k=0; k<possibleLetters.size(); k++) {
                    if(OkWords[j][1-current][i] == possibleLetters[k]) {
                        isOk=true;
                        break;
                    }
                }
                if(isOk)
                    OkWords[newInd++][current] = OkWords[j][1-current];
            }
            current = 1-current;
            oldInd = newInd;
            newInd = 0;
        }

        fout<<"Case #"<<x<<": "<<oldInd<<endl;
    }

    fin.close();
    fout.close();
    return 0;
}