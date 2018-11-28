#include <iostream>

#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

void splitNumber(int inNumber, vector<char> &digits)
{
    if(inNumber > 0) {
        int rem = inNumber % 10;

        digits.push_back(char(rem));

        splitNumber(inNumber / 10, digits);
    }
}

int joinNumber(int inNumber, int inPower, vector<char> inDigits){
    if(inDigits.size() > 0){
        inNumber += inDigits[0]*inPower;
        inDigits.erase(inDigits.begin());
        return joinNumber(inNumber, inPower*10, inDigits);
    }
    return inNumber;
}

int rotateNumber(int inNumber, int inRotations){
    vector<char> digits;
    splitNumber(inNumber, digits);

    while(inRotations-- > 0) {
        char digit = digits[0];
        digits.erase(digits.begin());
        digits.push_back(digit);
    }

    return joinNumber(0, 1, digits);
}

bool contains(const vector< pair<int, int> > &inCollection, int inN, int inM){
    vector< pair<int, int> >::const_iterator it(inCollection.begin());

    for(;it != inCollection.end(); it++) {
        if(((*it).first == inN && (*it).second == inM)
           || ((*it).first == inM && (*it).second == inN)) {
            return true;
        }
    }

    return false;
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int numCases = 0;
    in >> numCases;

    for(int c = 0; c < numCases; c++) {
        int a = 0;
        int b = 0;

        in >> a;
        in >> b;

        vector< pair<int,int> > pairs;
        for(int n = a; n < b; n++)
        {
            vector<char> digits;
            splitNumber(n, digits);
            if(digits.size() > 0) {
                for(int k = 0; k < (digits.size() - 1); k++){
                    char digit = digits[0];
                    digits.erase(digits.begin());
                    digits.push_back(digit);

                    if(digit != 0) {
                        int num = joinNumber(0, 1, digits);
                        if(num > n && num >= a && num <= b && !contains(pairs, num, n)) {
                            pairs.push_back(pair<int, int>(num, n));
                            //out << "case " << c << " n " << n << " num " << num << endl;
                        }
                    }
                }
            }
        }

        out << "Case #" << c + 1 << ": " << pairs.size() << endl;
    }

    in.close();
    out.close();

    return 0;
}
