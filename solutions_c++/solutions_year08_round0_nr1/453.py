#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("A-small-attempt3.in");
    int test;
    in >> test;


    for (int i=0; i<test; ++i)
    {
        int enginenum;
        in >> enginenum;

        string temp;
        getline(in, temp);

        map<string, bool> queryqueen;
        map<string, bool>::iterator pos;
        for (int k=0; k<enginenum; ++k)
        {
            string engine;
            getline(in, engine);
            //cout << i << " " << engine << endl;
            queryqueen[engine] = false;
        }

        int count = 0;
        int querynum;
        in >> querynum;
        getline(in, temp);
        int app = 0;
        //for (pos=queryqueen.begin(); pos!=queryqueen.end(); ++pos)
        //    pos->second = false;
        //cout << i << " " << querynum << endl;

        for (int j=0; j<querynum; ++j)
        {
            //cout << "???" << endl;
            string item;
            getline(in, item);
            //cout << i << " " << j << " " << item << endl;
            if (queryqueen[item] == false)
            {
                queryqueen[item] = true;
                ++app;
            }
            if (app == enginenum)
            {
                ++count;
                for (pos=queryqueen.begin(); pos!=queryqueen.end(); ++pos)
                {
                    pos->second = false;
                }
                queryqueen[item] = true;
                app = 1;
            }
        }
        cout << "Case #" << i+1 << ": " << count << endl;
    }
}
