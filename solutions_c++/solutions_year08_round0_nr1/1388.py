#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;


 typedef vector<string> vs;
 typedef vector<int> vi; 
 typedef vector<vi> vvi; 
 typedef pair<int,int> ii; 
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end()



 vector< pair <int,string> > searchEngine;
vector<string> query;
vector< pair<int,string> > temp;
 

int mySearch(string s,int startIndex)
{
    for(int i=startIndex;i<query.size();i++)
    {
        if(query[i]==s)
            return i;
    }
    return -1;

}
int findMax()
{
    int max=0;
    for(int i=0;i<searchEngine.size();i++)
    {
        if(searchEngine[i].first==-1)
            return i;
        if(searchEngine[i].first>searchEngine[max].first)
            max=i;
    }
    return max;
}
int process()
{
    int indexInQuery=0;
    int cnt=0;
    int engine=0;
    while(indexInQuery<query.size())
    {
        for(int i=0;i<searchEngine.size();i++)
        {
            searchEngine[i].first=mySearch(searchEngine[i].second,indexInQuery);
        }
        engine=findMax();
        if( searchEngine[engine].first==-1)
            return cnt;
        cnt++;
        indexInQuery=searchEngine[engine].first;
        for(int i=0;i<searchEngine.size();i++)
        {
            searchEngine[i]=temp[i];
        }
    }
}
int main()
{
    int N=0,S=0,Q=0;
    ifstream inFile("A-large.in");
    ofstream outFile("A-large.out");
    char* read=new char[102];
    inFile>>N;
    int num=1;
    while(N>0)
    {
        inFile>>S;
        inFile.ignore();
        for(int i=1;i<=S;i++)
        {
            inFile.getline(read,101);
            string engine(read);
            int xx =engine.size();
            searchEngine.push_back( make_pair(-1,engine) );
        }
        inFile>>Q;
        inFile.ignore();
        for(int i=1;i<=Q;i++)
        {
            inFile.getline(read,101);
            string s(read);
            query.push_back(s);
        }
        for(int i=0;i<searchEngine.size();i++)
        {
            temp.push_back(searchEngine[i]);
        }
        
        outFile<<"Case #"<<num<<": "<<process()<<endl;
        temp.clear();
        searchEngine.clear();
        query.clear();
        N--;
        num++;
    }
    return 0;
}