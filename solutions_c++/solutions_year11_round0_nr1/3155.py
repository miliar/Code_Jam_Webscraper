#include <iostream>
#include <sstream>
#include <fstream>
#include <iterator>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

void parseStr(ifstream& stream, vector<int>& intVector)
{
    string str;
    getline(stream, str);

    istringstream iss(str);
    copy(istream_iterator<int>(iss), istream_iterator<int>(), intVector.begin());

#ifdef DEBUG
    for (vector<int>::const_iterator iter = intVector.begin(); iter != intVector.end(); ++iter)
    {
        cout << *iter << " ";
    }
    cout << endl;
#endif
}

void parseStr(ifstream& stream, int& numButtons, vector<pair<char, int> >& buttons)
{
    string str;
    getline(stream, str);

    istringstream iss(str);
    iss >> numButtons;

    buttons.clear();
    buttons.resize(numButtons);

    char robot;
    int pos;
    for(int i = 0; i < numButtons; ++i)
    {
        iss >> robot;
        iss >> pos;
        buttons[i] = make_pair(robot, pos);    
    }
    return;
}

void parseStr(ifstream& stream, int& value)
{
    string str;
    getline(stream, str);

    istringstream iss(str);
    iss >> value;
}

vector<pair<char, int> >::const_iterator findNext(char colour,
        vector<pair<char, int> >::const_iterator cur,
        vector<pair<char, int> >::const_iterator endIter)
{
    for (; cur != endIter; ++cur)
    {
        if (cur->first == colour)
            return cur;
    }
    return cur;
}

int abs(int num)
{
    return (num > 0 ? num : num * (-1));
}

int direction(int curPos, int destPos)
{
    return curPos > destPos ? -1 : 1;
}

vector<pair<char, int> >::const_iterator doAction(char colour, int& curPos,
        vector<pair<char, int> >::const_iterator myIter,
        vector<pair<char, int> >::const_iterator otherIter,
        vector<pair<char, int> >::const_iterator endIter)
{
    if (myIter == endIter)
        return endIter;

    if (curPos < myIter->second)
        ++curPos;
    else if (curPos > myIter->second)
        --curPos;
    else if (curPos == myIter->second && myIter < otherIter)
        myIter = findNext(colour, myIter + 1, endIter); // aka press the button
    // else if curPos correct but not our turn wait
    return myIter;
}

int solve(int numButtons, vector<pair<char, int> >& positions)
{
    int seconds = 0;
    int orangePos = 1, bluePos = 1;
    vector<pair<char, int> >::const_iterator orangeIter = findNext('O', positions.begin(), positions.end());
    vector<pair<char, int> >::const_iterator blueIter = findNext('B', positions.begin(), positions.end());
    
    do {
        vector<pair<char, int> >::const_iterator save = orangeIter;
        orangeIter = doAction('O', orangePos, orangeIter, blueIter, positions.end());
        blueIter = doAction('B', bluePos, blueIter, save, positions.end());
        ++seconds;
    } while (orangeIter != positions.end() || blueIter != positions.end());
    
    return seconds;
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
        vector<pair<char, int> > positions;
        int numButtons;
        parseStr(input, numButtons, positions);
        int result = solve(numButtons, positions);
        cout << "Case #" << i << ": " << result << endl;
    }
}

