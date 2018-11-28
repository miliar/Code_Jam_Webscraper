#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
#include <fstream>

using namespace std;

bool win(int A,int B,bool first)
{
    if(A==B)
        return !first;
    int x=max(A,B);
    int y=min(A,B);
    int r=x%y;
    if(r==0)
        return first;
    if(first)
    {
        if(win(r,y,!first))
            return true;
        return (r+y<x) && win(r,y,first);
    }
    else
    {
        if(!win(r,y,!first))
            return false;
        if((r+y<x) && !win(r,y,first))
            return false;
        return true;
    }
}

void test()
{
    cout<<win(3,5,true)<<endl;
    exit(0);
}

int main()
{
    //test();
    // read data
    //ifstream in("test.txt");
    //ofstream out("output.txt");

    ifstream in("C-small-attempt1.in");
    ofstream out("output1.txt");

    int lineNum;
    in>>lineNum;
    string line;
    getline(in,line);
    
    for(int k=0;k<lineNum;k++)
    {       
        int a1,a2,b1,b2;
        int count=0;
        in>>a1>>a2>>b1>>b2;
        for(int i=a1;i<=a2;i++)
        {
            for(int j=b1;j<=b2;j++)
            {
                if(win(i,j,true))
                    count++;
            }
        }
        out<<"Case #"<<k+1<<": "<<count<<endl;
    }

    // write data and close
    in.close();
    out.close();

    return 0;
}
