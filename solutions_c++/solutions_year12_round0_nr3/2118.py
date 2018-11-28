#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <fstream>

using namespace std;

int main()
{
	string s1,s2,tmp;
	int n,t,i,j,p,q,a,b,k,c;
    set<int> coll;
    ostringstream convert;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>t;
    for (i = 1; i <= t; i++)
    {
        c = 0;
        fin>>a>>b;
        for (j = a; j <= b; j++)
        {
            coll.clear();
            convert.str("");
            convert<<j;
            s1 = convert.str();

            for (k = 1; k < s1.length(); k++)
            {
                s2 = s1.substr(k,s1.length()-k)+s1.substr(0,k);
                istringstream convert1(s2);
                convert1>>q;

                if ((q > j) && (q <= b)) coll.insert(q);
            }
            c+=coll.size();
        }
        fout<<"Case #"<<i<<": "<<c<<endl;
    }
    fout.close();
	return 0;
}
