#include <cstdlib>
#include <iostream>
#include <fstream>

#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int isplit(vector<int>& v, const string& str, char c)
{
    v.clear();
    string::const_iterator s = str.begin();
    while (true) {
        string::const_iterator begin = s;

        while (*s != c && s != str.end()) { ++s; }

    v.push_back(strtol(string(begin, s).c_str(),0,10));

    if (s == str.end()) {
            break;
        }

        if (++s == str.end()) {
            //v.push_back("");
            break;
        }
    }
    return v.size();
}

int split(vector<string>& v, const string& str, char c)
{
    v.clear();
    string::const_iterator s = str.begin();
    while (true) {
        string::const_iterator begin = s;

        while (*s != c && s != str.end()) { ++s; }

    v.push_back(string(begin, s));

    if (s == str.end()) {
            break;
        }

        if (++s == str.end()) {
            v.push_back("");
            break;
        }
    }
    return v.size();
}

int main(int argc, char *argv[])
{
    
    std::ifstream in("A-small.in");
    std::ofstream out("A-small.out");
        
    string TestCases;
    std::getline(in,TestCases);
    int testcases = strtol(TestCases.c_str(), 0, 10);
    
    std::vector<int> Params;
    std::vector<int> Freq;
    
    string line;
    
    long P, K, L;
    long sum, f, k;
    long keys;
        
    for(int i=1; i<=testcases; i++)
    {

        std::getline(in,line);
        isplit(Params, line, ' ');
        
        P = Params.at(0);
        K = Params.at(1);
        L = Params.at(2);
        
        std::getline(in,line);
        isplit(Freq, line, ' ');
        
        std::sort(Freq.begin(), Freq.end());
        
        sum = 0;
        k = 1;
        keys = K;
        
        for(std::vector<int>::reverse_iterator ii = Freq.rbegin(); ii!=Freq.rend();)
        {
           f = 0;
           for(int j=1; j<=keys; j++)
           {
               f +=(*ii);
               ++ii;
               if(ii == Freq.rend()) break;
           }
           sum += k*f;
           k++;
        }
        out << "Case #" << i << ": " << sum << endl;
           
    }//end of testcases
            
    in.close();
    out.close();
   
    system("PAUSE");
    return EXIT_SUCCESS;
}
