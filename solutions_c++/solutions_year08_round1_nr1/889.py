#include<fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
string mul(int a,int b)
{
       
}
int main()
{
    ifstream inputf;
    int cn=0;
    ofstream outputf;
    char source[101];
    char inputFilename[] = "A-small-attempt0.in";
    char outputFilename[] = "output.list";
    inputf.open(inputFilename, ios::in);
    outputf.open(outputFilename, ios::out);

  inputf >> cn;

    for(int i=1;i<=cn;++i)
    {
        vector<int> v1;
        vector<int> v2;
        int n;
        inputf>>n;
        inputf.getline((char *)source,(streamsize)101);
        for(int j=0;j<n;j++)
        {
                int temp;
         inputf>>temp;
         v1.push_back(temp);        
        }
        inputf.getline((char *)source,(streamsize)101);
        for(int j=0;j<n;j++)
        {
                int temp;
         inputf>>temp;
         v2.push_back(temp);        
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        reverse(v2.begin(),v2.end());
        long long int x=0;
        for(int j=0;j<n;j++)
        {
                    x=x+v1[j]*v2[j];    
        }
        
         outputf << "Case #"<<i<<": "<<x<<endl;
    }
    outputf.close();
    inputf.close();
    return 0;
}
