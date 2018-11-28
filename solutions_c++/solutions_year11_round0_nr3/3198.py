#include <iostream>
#include <sstream>
#include <fstream>
#include <iterator>
#include <cstdlib>
#include <vector>
#include <list>
#include <algorithm>
#include <climits>

using namespace std;

void parseStr(ifstream& stream, vector<int>& intVector)
{
    string str;
    getline(stream, str);

    istringstream iss(str);
    copy(istream_iterator<int>(iss), istream_iterator<int>(), intVector.begin());
}

template <class T>
void debugV(T& intVector)
{
    for (typename T::const_iterator iter = intVector.begin(); iter != intVector.end(); ++iter)
    {
        cout << *iter << " ";
    }
    cout << endl;
}

void parseStr(ifstream& stream, int& value)
{
    string str;
    getline(stream, str);

    istringstream iss(str);
    iss >> value;
}

int check(vector<int>& v1, vector<int>& v2)
{
    int actualLhs, actualRhs, patrickLhs, patrickRhs;
    actualLhs = actualRhs = patrickLhs = patrickRhs = 0;

    for (int j = 0; j < v1.size(); ++j)
    {
        actualLhs += v1[j];
        patrickLhs ^= v1[j];
    }
    for (int j = 0; j < v2.size(); ++j)
    {
        actualRhs += v2[j];
        patrickRhs ^= v2[j];
    }

    //cerr << actualLhs << " " << actualRhs << " " << patrickLhs << " " << patrickRhs << endl;
    if (patrickLhs == patrickRhs)
    {
        return max(actualLhs, actualRhs);
    }
    return -1;
}

int recurse(vector<int> v1, vector<int> v2, int cur)
{
    if (v2.size() == 1 || cur >= v2.size())
    {
        return check(v1, v2);
    }

    v1.push_back(v2[cur]);
    v2.erase(v2.begin() + cur);
    
    int t1 = recurse(v1, v2, cur);
    int t2 = recurse(v1, v2, cur + 1);
    return max(check(v1, v2), max(t1, t2));
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        cerr << "Input file missing" << endl;
        exit(-1);
    }
    ifstream input;
    input.open(argv[1]);
    if (!input.is_open())
    {
        cerr << "Cannot open file " << argv[1] << endl;
        exit(-2);
    }

    int testCases;
    parseStr(input, testCases);
    cerr << "Test cases " << testCases << " total" << endl;

    for (int i = 1; i <= testCases; ++i)
    {
        int numCandy;
        parseStr(input, numCandy);
        
        vector<int> candyValues;
        candyValues.resize(numCandy);
        parseStr(input, candyValues);

        int result = -1;
        
        vector<int> v1, v2;
        v1.resize(numCandy);
        v2.resize(numCandy);
        copy(candyValues.begin(), candyValues.end(), v2.begin());
        result = recurse(v1, v2, 0);
        
        if (result != -1)
            cout << "Case #" << i << ": " << result << endl;
        else
            cout << "Case #" << i << ": NO" << endl;
    }
}

