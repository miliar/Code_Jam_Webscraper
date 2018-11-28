#include <iostream>
#include <strstream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <iterator>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define MAXLENGTH 512
#define THRESHOLD 10000

using namespace std;

int doit(const char* patt, const int pl, const int pr,
    const char* astr, const int sl, const int sr)
{
    int count = 0;
    //cout<<pl<<" "<<pr<<" "<<sl<<" "<<sr<<endl;
    int cr = sl;
    while(cr < sr)
    {
        if(astr[cr] == patt[pl])
        {
            if(pl == pr-1)
                count++;
            else
                count += doit(patt, pl+1, pr, astr, cr+1, sr);
        }
        cr++;
    }
    //char c;
    //cin>>c;
    return count % THRESHOLD;
}

int main()
{
    const char* pattern = "welcome to code jam";
    const int plen = strlen(pattern);
    cout<<"pattern length: "<<plen<<endl;

    char* astr = new char[MAXLENGTH];

    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small-attempt0.out");
    //ifstream fin("C-large.in");
    //ofstream fout("C-large.out");
    int casenum = 0;
    fin>>casenum;
    cout<<"casenum: "<<casenum<<endl;
    fin.getline(astr, MAXLENGTH);
    for(int i = 0; i < casenum; i++)
    {
        fin.getline(astr, MAXLENGTH);
        cout<<"astr: "<<astr<<endl;
        fout<<"Case #"<<i+1<<": ";
        fout.fill('0');
        fout.width(4);
        int count = doit(pattern, 0, plen, astr, 0, strlen(astr));
        fout<<count<<endl;
        cout<<"doit: "<<count<<endl;
    }

    return 0;
}
