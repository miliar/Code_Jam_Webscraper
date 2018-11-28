#include <string>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

struct Combo {
    char one, two, combo;
} ;

int getCases()
{
    int i = 0;
    cin >> i;
    return i;
}

void calculateCase( int caseNum, string &output ) {

    std::vector<Combo> combinations;
    std::vector<Combo> opposed;
    
    int numCombos = 0;
    cin >> numCombos;
    for (int i = 0; i < numCombos; ++i) {
        char one, two, combo;
        cin >> one >> two >> combo;
        Combo c;
        c.one = one;
        c.two = two;
        c.combo = combo;
        combinations.push_back(c);
    }

    int numOpposed = 0;
    cin >> numOpposed;
    for (int i = 0; i < numOpposed; ++i) {
        char one, two;
        cin >> one >> two;
        Combo c;
        c.one = one;
        c.two = two;
        opposed.push_back(c);
    }

    std::vector<char> result;

    int numInput = 0;
    cin >> numInput;
    for (int i = 0; i < numInput; ++i) {
        char next;
        cin >> next;
        result.push_back(next);

        // Combine (until you can't combine no more)
        bool noCombine = false;

        while(!noCombine) {
            next = result.back();
            bool combine = false;
            for (int j = 0; j < combinations.size(); ++j) {
                if (combinations[j].one == next) {
                    char target, combo;
                    target = combinations[j].two;
                    combo = combinations[j].combo;
                    if (result[result.size() - 2] == target) {
                        result[result.size() - 2] = combo;
                        result.pop_back();
                        combine = true;
                        break;
                    }
                } else if (combinations[j].two == next) {
                    char target, combo;
                    target = combinations[j].one;
                    combo = combinations[j].combo;
                    if (result[result.size() - 2] == target) {
                        result[result.size() - 2] = combo;
                        result.pop_back();
                        combine = true; 
                        break;
                    }
                }
            }
            if (!combine) noCombine = true;
        }


        // Clear if opposed
        for (int j = 0; j < opposed.size(); ++j) {

            if (opposed[j].one == next) {
                char danger = opposed[j].two;
                for (int k = 0; k < result.size(); ++k) {
                    if (result[k] == danger) {
                        result.clear();
                        break;
                    }
                }
            }
            if (opposed[j].two == next) {
                char danger = opposed[j].one;
                for (int k = 0; k < result.size(); ++k) {
                    if (result[k] == danger) {
                        result.clear();
                        break;
                    }
                }
            }
        }

    }
    // Finally, the output
    string thisCase = "Case #";
    stringstream convert;
    convert << caseNum;
    thisCase += convert.str();
    thisCase += ": [";
    std::vector<char>::iterator it = result.begin();
    std::vector<char>::iterator end = result.end();
    if (it < end) {
        thisCase += *it;
        ++it;
        while (it < end) {
            thisCase += ", ";
            thisCase += *it;
            ++it;
        }
    }
    thisCase += "]\n";

    output += thisCase;

    return;

}

int main ()
{
    int cases = getCases();
    string output = "";
    for (int caseNum = 1; caseNum <= cases; ++caseNum)
        calculateCase( caseNum, output );

    cout << output;
}

