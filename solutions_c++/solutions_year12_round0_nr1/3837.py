#include <iostream>
#include <string>
#include <vector>

#include <cassert>

using namespace std;

/*
void addToMapping(string& mapping, string& from, string& to)
{
    assert(from.size() == to.size());
    char currFrom, currTo;
    for(int i = 0; i < from.size(); ++i)
    {
        if (from[i] == ' ') {
            continue;
        }
        currFrom = from[i] - 'a';
        assert(0 <= currFrom && 26 > currFrom);
        if (mapping[currFrom] != -1) {
            assert(mapping[currFrom] == to[i]);
        } else
        {
            mapping[currFrom] = to[i];
        }
    }
}
*/

string translate(string& mapping, string& from)
{
    char currFrom;
    string ret;
    ret.reserve(from.length());
    for(int i = 0; i < from.size(); ++i)
    {
        if(from[i] == ' ') {
            ret.push_back(' ');
            continue;
        }
        currFrom = from[i]-'a';
        assert (currFrom >= 0 && currFrom < 26);
        ret.push_back(mapping[currFrom]);
    }
    return ret;
}

int main()
{

    string mapToGooglerese("yhesocvxduiglbkrztnwjpfmaq");

	int numTests;
	cin >> numTests;
    string dummy;
    getline(cin, dummy);
    for (int i = 0; i < numTests; ++i)
    {
        string googlerese, english;
        getline(cin, googlerese);
        cout << "Case #" << i+1 << ": " <<
            translate(mapToGooglerese, googlerese) << endl;
    }
}
