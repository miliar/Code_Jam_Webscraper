#include <iostream>
#include "set.h"
#include "simpio.h"
#include "/Users/leungtimothy/Desktop/StanfordCPPLib/strlib.h"
using namespace std;

int main() {
    int A,B;
    int n;
    string str;
    bool isKey;
    Vector<int> tuple;
    Vector<Vector<int> > list;
    int numCases;
    
    ifstream fin;
    ofstream fout;
    fin.open("/Users/leungtimothy/Desktop/problem3.txt");
    fout.open("/Users/leungtimothy/Desktop/problem3result.txt");
    fin >> numCases;
    for (int num = 0 ; num < numCases; num++) {
    fin >> A;
    fin >> B;
    int m;


    while (A<=B) {
        n = A;
        str = integerToString(n);
        int len = str.length();
        string newStr;
        for (int i = 1; i < len; i++) {
            newStr = str.substr(len-i, i) + str.substr(0,len-i);
            isKey = false;
            tuple.clear();
            if (newStr[0]!='0') {
                m = stringToInteger(newStr);
                if (m > n and m <=B) {
                    tuple.add(n);
                    tuple.add(m);
                }
            }
            if (tuple.size()>0) {
                for (int i = 0; i < list.size(); i++) {
                    if (tuple[1] == list[i][0]) {
                        isKey = true;
                    }
                }
                if (!isKey) {
                    list.add(tuple);
                }
            }
        }
        A++;
    }
     
        fout << "Case #" << num+1 << ": "<< list.size() << endl;
        cout << "Case #" << num+1 << ": "<< list.size() << endl;  
        list.clear();
    }
    return 0;
}
