#include<fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

int main()
{
    ifstream inputf;
    int cn=0;
    int L,D;
    ofstream outputf;
    char inputFilename[] = "B-small-practice(2).in";
    char outputFilename[] = "output.list";
    inputf.open(inputFilename, ios::in);
    outputf.open(outputFilename, ios::out);
    inputf>>cn;
    for(int i1=0; i1<cn; i1++)
    {
         
         outputf << "Case #"<<i1+1<<": "<<ret<<endl;        
    }
    outputf.close();
    inputf.close();
    //cin>>cn;
    return 0;
}
