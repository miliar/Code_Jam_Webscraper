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

string inFile;
string outFile;

void setTestFiles()
{
    inFile="input.txt";
    outFile="output.txt";
}

void setSmallFiles()
{
    inFile="A-small-attempt0.in";
    outFile="small.txt";
}

void setLargeFiles()
{
    inFile="A-large.in";
    outFile="large.txt";
}

int lb[1000];
int rb[1000];
int n;

class Node
{
public:
    int y;
    int x1;
    int x2;
    int y1;
    int y2;
    bool operator<(const Node& rhs) const
    {
        int xc = x1*rhs.x2 - x2*rhs.x1;
        if(xc<0)
            return true;
        if(xc==0)
        {
            if(y<rhs.y)
                return true;
            int yc=y1*rhs.y2 - y2*rhs.y1; 
            if(yc<0)
                return true;
        }
        return false;
    }
    bool operator==(const Node& rhs) const
    {
        return y==rhs.y && (x1*rhs.x2 - x2*rhs.x1) && (y1*rhs.y2 - y2*rhs.y1);
    }

};

void intersect(int j,int k,set<Node>& nodes)
{
    int dyl=lb[k]-lb[j];
    int dyr=rb[k]-rb[j];
    if((dyl>0 && dyr<0) || (dyl<0 && dyr>0))
    {
        Node node;
        node.x1=abs(dyl);
        node.x2=abs(dyr);
        int temp=node.x1*rb[j]+node.x2*lb[j];
        int temp2=node.x1+node.x2;
        node.y=temp/(temp2);
        node.y1=temp%temp2;
        node.y2=temp2;
        nodes.insert(node);
    }
}

int main()
{
    //setTestFiles();
    //setSmallFiles();
    setLargeFiles();
    ifstream in(inFile.c_str());
    ofstream out(outFile.c_str());

    int lineNum;
    in>>lineNum;
    string line;
    getline(in,line);
    
    for(int i=0;i<lineNum;i++)
    {        
        set<Node> nodes;
        in>>n;
        for(int j=0;j<n;++j)
        {
            in>>lb[j]>>rb[j];
        }
        for(int j=0;j<n;++j)
        {
            for(int k=j+1;k<n;++k)
            {
                intersect(j,k,nodes);
            }
        }
        int result=nodes.size();
        ostringstream oss;
        oss<<"Case #"<<i+1<<": "<<result;
        out<<oss.str()<<endl;
        cout<<oss.str()<<endl;
    }

    in.close();
    out.close();
    return 0;
}
