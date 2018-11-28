#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <queue>

using namespace std;

// global
string needle = "welcome to code jam"; // length 19
//string needle = "ab";
string haystack;



// get line
string gl()
{
    char chGl [100];
    gets (chGl);
    string gl = chGl;
    return gl;
}

// get line as integer
int gli()
{
    string gli = gl();
    return atoi(gli.c_str());
}


/*
// contains positions of the letters "welcome.."
class node
{
    public:
        int nPos; // position in needle
        int hPos; // position in haystack

        node(int a, int b)
        {
            nPos = a;
            hPos = b;
        }

};
*/

// recursive
// count Occurences
// needle position, haystack position
int countOcc (int nPos, int hPos)
{
    if (nPos > needle.length()) return 0;
    if (hPos > haystack.length()) return 0;

    int count;
    string letter;

    letter = needle[nPos];
    size_t found = haystack.find(letter, hPos);

    // not found
    if (found == string::npos)
    {
        return 0;
    }

    // if is found


    // search for next occurence of this letter
    count = countOcc (nPos, found+1) % 10000;

    // if complete needle is found
    if (nPos == needle.length() - 1)
    {
        return 1 + count;
    }

    // search for next letter in needle
    count = (count + countOcc (nPos+1, found+1)) % 10000;

    //printf ("TEST %d %d %d\n", nPos, hPos, count);
    return count;
}


int main()
{
    string letter, input;
    int i, N;
    size_t found;

    // input output streams
    freopen ("C-small.in", "r", stdin);
    freopen ("output.txt", "w", stdout);

    // number of cases
    N = gli();
    if (N < 1)
        printf ("Error: input file not found\n");

    // for each case
    for (int caseId=1; caseId<=N; caseId++)
    //for (int caseId=1; caseId<=1; caseId++)
    {
        // read input
        input = gl();

        haystack = "";
        // extract only relevant characters
        for (i=0; i<input.length(); i++)
        {
            letter = input[i];
            //printf ("%s", letter.c_str());

            found = needle.find (letter); // is this letter actually used?

            if (found != string::npos)
            {
                haystack += letter;
            }
        }
        //printf ("%s\n", haystack.c_str());

        printf ("Case #%d: %04d\n", caseId, countOcc(0,0));
    }

    /*
    queue<node> s;
    s.push (node(0,0));

    while (s.empty()) = false)
    {
        node top = s.top();
        s.pop();

    }
    */

    return 0;
}
