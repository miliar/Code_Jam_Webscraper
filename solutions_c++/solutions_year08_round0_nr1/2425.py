#include<fstream>
#include<vector>
#include<string>
#include<iostream>
#include<cstdio>
#include<set>
using namespace std;
int main()
{
    ifstream inFile;
    ofstream outFile;
    char inputFilename[] = "A-large.in";
    char outputFilename[] = "out.list";
    inFile.open(inputFilename, ios::in);
    outFile.open(outputFilename, ios::out);
    int N=0;
    inFile >> N;
    for(int i=1;i<=N;++i)
    {
        int S=0,Q=0;
        inFile >> S;
        vector<string> se;
        char s[101];
        inFile.getline((char *)s,(streamsize)101);
        for(int j=0;j<S;++j)
         {
                      inFile.getline((char *)s,(streamsize)101);
                      
         }
         inFile >> Q;
        vector<string> qe;
        inFile.getline((char *)s,(streamsize)101);
        for(int j=0;j<Q;++j)
         {
                      inFile.getline((char *)s,(streamsize)101);
                      string ss(s);
                      qe.push_back(ss);
         }
         int cnt=0;
         set<string>x;
         for(int j=0;j<qe.size();++j)
         {
                 x.insert(qe[j]);
                 if(x.size()==S)
                 {
                 cnt++;
                 x.clear();x.insert(qe[j]);
                 }
         }
         outFile << "Case #"<<i<<": "<<cnt<<endl;
    }
    inFile.close();
    outFile.close();
    return 0;
}
