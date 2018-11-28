#include <iostream>

#include <fstream>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

typedef vector<unsigned long> TIV;
typedef vector<short> TSV;


int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int numCases = 0;
    in >> numCases;

    for(int c = 0; c < numCases; c++) {
        TIV candies;
        int numCandies = 0;
        unsigned long candyValue = 0;
        in >> numCandies;
        for(int i = 0; i < numCandies; i++) {
            in >> candyValue;
            candies.push_back(candyValue);
        }

        sort(candies.begin(), candies.end());

        unsigned long seanVal = 0;
        unsigned long currentSeanSum = 0;
        unsigned long currentPatValue = 0;
        unsigned long patVal = 0;

        unsigned long seanStartVal = 0;
        unsigned long seanSum = 0;

        int numPatItems = 1;

        while( numPatItems < candies.size() ) {
            TIV::iterator it(candies.begin());
            for( ; it != candies.end(); ++it ){
                patVal = 0;
                TIV::iterator pit(it);
                int i = 0;
                for( ; i < numPatItems && pit != candies.end(); i++, ++pit) {
                    patVal ^= *pit;
                }

                if(i != numPatItems){
                    break;
                }

                seanStartVal = 0;
                seanSum = 0;
                TIV::iterator ssit(candies.begin());
                for( ; ssit != it; ++ssit ){
                    seanStartVal ^= *ssit;
                    seanSum += *ssit;
                }

                for( ; pit != candies.end(); ++pit ) {
                    seanStartVal ^= *pit;
                    seanSum += *pit;
                }

                if( patVal == seanStartVal && seanSum > currentSeanSum ){
                    seanVal = seanStartVal;
                    currentPatValue = patVal;
                    currentSeanSum = seanSum;
                }
            }
            numPatItems++;
        }

        out << "Case #" << c + 1 << ": ";
        if( currentPatValue == seanVal && seanVal != 0 ) {
            out << currentSeanSum;
        }
        else {
            out << "NO";
        }
        out << endl;
    }

    in.close();
    out.close();
    return 0;
}
