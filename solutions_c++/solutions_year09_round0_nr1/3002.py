#include<iostream>
#include<conio.h>
#include<string>
#include<vector>
#include<fstream>

using namespace std;

int main() {
    vector<string> alienWords;
    vector<string> ambigiousWords;
    
    int wordLength;
    int numWordsDict;
    int numWordsTransmitted;
    
    ofstream out("p1.out");
    ifstream in("A-large.in");
    in >> wordLength >> numWordsDict >> numWordsTransmitted;
    for (int i=0; i<numWordsDict; i++) {
        string temp;
        in >> temp;
        alienWords.push_back(temp);
    }
    for (int i=0; i<numWordsTransmitted; i++) {
        string temp;
        in >> temp;
        ambigiousWords.push_back(temp);
    }
    
    for (int i=0; i<numWordsTransmitted; i++) {
        int numMatches = 0;
        string ambigWord = ambigiousWords[i];
        for (int j=0; j<numWordsDict; j++) {
            string currWord = alienWords[j];
            int origWordPtr = 0;
            bool bracketFlag = false;
            bool selected = false;
            string formedWord = "";
            
            for (int k=0; k<ambigWord.length(); k++) {
                if (ambigWord[k] == ')') {
                   selected = false;
                   bracketFlag = false;
                } else if (ambigWord[k] == '(') {
                   bracketFlag = true;
                } else {
                   if (!selected && ambigWord[k] == currWord[origWordPtr]) {
                      formedWord += ambigWord[k];
                      origWordPtr++;
                      if (bracketFlag) selected = true;
                   }
                }
            }
            if (formedWord == currWord) 
               numMatches++;
        }
        out << "Case #" << i+1 << ": " << numMatches << endl;
    }
    return 0;   
}
