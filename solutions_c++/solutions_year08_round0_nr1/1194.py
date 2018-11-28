#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <set>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    ofstream fout ("a.out");
    ifstream fin ("a.in");
    int n;
    int a;
    int b;
    int res;
    vector <string> engines;
    vector <string> queries;
    set <string> used;
    string t;
    getline(fin, t);
    stringstream ss;
    ss<<t;
    ss>>n;
    //fout << n << endl;
    for(int i=0; i<n; i++)
    {
        res=0;
        getline(fin, t);
        stringstream ssa;
        ssa<<t;
        ssa>>a;
        engines.clear();
        
        for(int j=0; j<a; j++)
        {
            string s;
            getline(fin, s);
            engines.push_back(s);
            //fout << engines[j] << endl;
        }
        getline(fin, t);
        stringstream ssb;
        ssb<<t;
        ssb>>b;
        queries.clear();
        for(int j=0; j<b; j++)
        {
            string s;
            getline(fin, s);
            queries.push_back(s);
        }
        
        used.clear();
        for(int j=0; j<b; j++)
        {
            used.insert(queries[j]);
            //fout << used.size() << endl;
            if(used.size()==a)
            {
                res++;
                used.clear();
                used.insert(queries[j]);
            }
        }
        
        fout << "Case #" << (i+1) << ": " << res << endl;
    }
    //system("PAUSE");
    return 0;
}
