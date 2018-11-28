#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
using namespace std;

map<string, int> names;
vector<vector<int> >children;

int putMap(string str)
{
    if (names.find(str) == names.end())
    {
       int s = names.size();
       names[str] = s;
       return s;
    }
    return names[str];
}

int recurse(int index)
{
    if (children[index].size() == 0) return 1;
    vector<int> values;
    
    for (int i = 0; i < children[index].size(); i++)
    {
        int result = recurse(children[index][i]);
        values.push_back(result);
    }
        sort(values.begin(), values.end());
        
        if (values.size() == 1)
        {
           return max(2, values[0]);
        }
        
        int themax = values.size() + 1;
        for (int j = 0; j < values.size(); j++)
        {
            int ans = values[values.size()-1-j] + j;
            if (themax < ans) themax = ans;
        }
        return themax;
        
        return max(
               values[values.size()-1],
               values[values.size()-2] + 1);
}

int main()
{    
    ifstream infile("happy.txt");
    int cases;
    infile >> cases;
    ofstream out("sad.txt");
    
    for (int c = 0; c < cases; c++)
    {
        int numMixes;
        infile >> numMixes;
        
        names.clear();
        children = vector<vector<int> >(numMixes);
        
        for (int i = 0; i < numMixes; i++)
        {
            string root;
            infile >> root;
            int rootIndex = putMap(root);
            int ingredi;
            infile >> ingredi;
            //cout << c << " " << root << " " << rootIndex <<  " " << ingredi << endl;
            for (int j = 0; j < ingredi; j++)
            {
                string str;
                infile >> str;
                if (str[0] >= 'a' && str[0] <= 'z')
                   continue;
                int index = putMap(str);
                children[rootIndex].push_back(index);
            }
        }
        
        out << "Case #" << (c+1) << ": " << recurse(0) << endl;
    }
    system("PAUSE");
    return 0;
}
                
