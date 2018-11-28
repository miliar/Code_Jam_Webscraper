#include <iostream>
#include <cstdlib>
#include <map>
#include <vector>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <deque>
#include <fstream>
#include <string>
#include <cstring>
#include <dirent.h>
#include <sstream>
#include <errno.h>
#include <sys/stat.h>
#include <cmath>
#include <stdlib.h>
#include <sys/mman.h>
#include <time.h>
#include <sys/time.h>
#include <sys/select.h>

namespace alex{
    
}

using namespace std;
using namespace alex;

string process(string &a, string &b, string &c, string &d);

int main(int argc, char* argv[])
{

    string i1, i2, i3, i4;
    ofstream fout;
    fout.open("output.txt");

    string file_name = "input.txt";
    if (argc >= 2)
        file_name = *(argv+1);
    ifstream fin;
    fin.open(file_name.c_str());
    long long double input_size;
    fin >> input_size;
    
    size_t i = 0;
    label:
        fin >> i1 >> i2 >> i3 >> i4;
        fout<<"Case #"<<i+1<<": "<<process(i1, i2, i3, i4)<<endl;
    if (++i < input_size)
        goto label;


    return 0;
}

bool testX(string &a, string &b, string &c, string &d);
bool testO(string &a, string &b, string &c, string &d);
bool testDraw(string &a, string &b, string &c, string &d);

string process(string &a, string &b, string &c, string &d)
{
    if (testX(a,b,c,d))
        return string("X won");
    if (testO(a,b,c,d))
        return string("O won");
    if (testDraw(a,b,c,d))
        return string("Draw");
    return string("Game has not completed");
}

bool column_test(string &a, string &b, string &c, string &d, char player)
{
    for (int i =0; i<4; ++i)
    {
        if (((a[i] == player) || (a[i] == 'T')) &&
            ((b[i] == player) || (b[i] == 'T')) &&
            ((c[i] == player) || (c[i] == 'T')) &&
            ((d[i] == player) || (d[i] == 'T')))
            return true;
    }
    return false;
}

bool row_test(string &a, string &b, string &c, string &d, char player)
{
    
    if (((a[0] == player) || (a[0] == 'T')) &&
        ((a[1] == player) || (a[1] == 'T')) &&
        ((a[2] == player) || (a[2] == 'T')) &&
        ((a[3] == player) || (a[3] == 'T')))
        return true;
    if (((b[0] == player) || (b[0] == 'T')) &&
        ((b[1] == player) || (b[1] == 'T')) &&
        ((b[2] == player) || (b[2] == 'T')) &&
        ((b[3] == player) || (b[3] == 'T')))
        return true;
    if (((c[0] == player) || (c[0] == 'T')) &&
        ((c[1] == player) || (c[1] == 'T')) &&
        ((c[2] == player) || (c[2] == 'T')) &&
        ((c[3] == player) || (c[3] == 'T')))
        return true;
    if (((d[0] == player) || (d[0] == 'T')) &&
        ((d[1] == player) || (d[1] == 'T')) &&
        ((d[2] == player) || (d[2] == 'T')) &&
        ((d[3] == player) || (d[3] == 'T')))
        return true;
    return false;



    bool testing = true;
    for (int i = 0 ; i< 4; ++i)
    {
        if(a[i] != player || a[i] != 'T')
            testing= false;
    }
    if (testing) return true;
    testing = true;
    for (int i = 0 ; i< 4; ++i)
    {
        if(b[i] != player || b[i] != 'T')
            testing= false;
    }

    if (testing) return true;
    testing = true;

    for (int i = 0 ; i< 4; ++i)
    {
        if(d[i] != player || c[i] != 'T')
            testing= false;
    }

    if (testing) return true;
    testing = true;

    for (int i = 0 ; i< 4; ++i)
    {
        if(d[i] != player || d[i] != 'T')
            testing= false;
    }

    if (testing) return true;
    return false;
}

bool diagonal_test(string &a, string &b, string &c, string &d, char player)
{
    if ((a[0] == player || a[0] == 'T') &&
        (b[1] == player || b[1] == 'T') &&
        (c[2] == player || c[2] == 'T') &&
        (d[3] == player || d[3] == 'T'))
        return true;
    if ((d[0] == player || d[0] == 'T') &&
        (c[1] == player || c[1] == 'T') &&
        (b[2] == player || b[2] == 'T') &&
        (a[3] == player || a[3] == 'T'))
        return true;

    return false;
}

bool testX(string &a, string &b, string &c, string &d)
{
    if (row_test(a,b,c,d,'X') || column_test(a,b,c,d, 'X') || diagonal_test(a,b,c,d,'X'))
        return true;
    return false;
    //diagonals
}

bool testO(string &a, string &b, string &c, string &d)
{
    if (row_test(a,b,c,d,'O') || column_test(a,b,c,d, 'O') || diagonal_test(a,b,c,d,'O'))
        return true;
    return false;
}

bool testDraw(string &a, string &b, string &c, string &d)
{
    //look for dot, if no dot, draw;
    if (a.find(".") != string::npos) return false;
    if (b.find(".") != string::npos) return false;
    if (c.find(".") != string::npos) return false;
    if (d.find(".") != string::npos) return false;
    return true;
}


//8:14 pm - 8:34 pm

