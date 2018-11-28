#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool Compare(char c1, char c2)
{
     if(c1=='0') return false;
     if(c2=='0') return true;
     return c1<c2;
}

int main()
{
    ifstream fin("b-input.in");
    ofstream fout("b-output.out");
    int N, T;
    fin >> T;
    for(int c=0; c<T; c++)
    {
        fin >> N;
        ostringstream sout;
        sout << N;
        string nstr=sout.str();
        string maxnstr=nstr;
        string minnstr=nstr;
        sort(maxnstr.begin(), maxnstr.end());
        sort(minnstr.begin(), minnstr.end(), &Compare);
        reverse(maxnstr.begin(), maxnstr.end());
        if(nstr==maxnstr)
        {
            ostringstream ret;
            ret << minnstr[0] << "0";
            minnstr.erase(minnstr.begin());
            sort(minnstr.begin(), minnstr.end());
            for(int i=0; i<minnstr.size(); i++) ret << minnstr[i];
            fout << "Case #" << c+1 << ": " << ret.str() << endl;
            continue;
        }
        vector <int> digits;
        for(int i=0; i<nstr.size(); i++) digits.push_back(nstr[i]-'0');
        next_permutation(digits.begin(), digits.end());
        string ret="";
        for(int i=0; i<digits.size(); i++) ret+=(char)(digits[i]+'0');
        fout << "Case #" << c+1 << ": " << ret << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
