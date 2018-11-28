#include<fstream>
#include<vector>
#include<string>
#include<iostream>
#include<cstdio>
#include<set>
using namespace std;
int main()
{
    ifstream inputf;
    int cn=0;
    ofstream outputf;
    char inputFilename[] = "A-large.in";
    char outputFilename[] = "output.list";
    inputf.open(inputFilename, ios::in);
    outputf.open(outputFilename, ios::out);
    inputf >> cn;
    for(int i=1;i<=cn;++i)
    {
        int ts=0;
        int query=0;
         int count=0;
        vector<string> sou;
        vector<string> inp;
        char source[101];
        inputf >> ts;
        int c=0;
        inputf.getline((char *)source,(streamsize)101);
        for(int j=0;j<ts;++j)
         {
                      inputf.getline((char *)source,(streamsize)101);
                      c++;       
         }
         
        inputf >> query;
        inputf.getline((char *)source,(streamsize)101);
        for(int j=0;j<query;++j)
         {
                      inputf.getline((char *)source,(streamsize)101);
                      string ss(source);
                      inp.push_back(ss);
                      c++;
         }
         set<string>sou1;
         for(int j=0;j<inp.size();++j)
         {
                 sou1.insert(inp[j]);
                 if(sou1.size()==ts)
                 {
                 count++;
                 sou1.clear();sou1.insert(inp[j]);
                 }
                 c++;  //total steps
         }
         outputf << "Case #"<<i<<": "<<count<<endl;
    }
    outputf.close();
    inputf.close();
    return 0;
}
