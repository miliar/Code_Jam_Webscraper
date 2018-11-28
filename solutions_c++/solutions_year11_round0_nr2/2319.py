#include<iostream>
#include<fstream>
using namespace std;
//ifstream fin("MAGICKA.IN");
ifstream fin("B-large.in");
ofstream fout("B-large.out");
string C[37];
string D[29];
int nC,nD;
string S;
int nS;

bool combine(string& s)
{
    if(s.length()==0||s.length()==1)
       return false;
    
    for(int i=0;i<nC;i++)
       if(C[i][0]==s[s.length()-2]&&C[i][1]==s[s.length()-1]
          || C[i][1]==s[s.length()-2]&&C[i][0]==s[s.length()-1])
       {
             s = s.substr(0,s.length()-2) + C[i].substr(2,1);
             return true;
       }
    return false;
}

bool oppose(string& s)
{
    if(s.length()==0||s.length()==1)
       return false; 
    for(int i=0;i<s.length()-1;i++)
        for(int j=0;j<nD;j++)
        {
            if(D[j][0]==s[i]&&D[j][1]==s[s.length()-1]
               || D[j][1]==s[i]&&D[j][0]==s[s.length()-1])
            {
               s = "";
               return true;
            }
        }
    return false;
}

void process(int t)
{
    fout<<"Case #"<<t<<": ["; 
    fin>>nC;
    for(int i=0;i<nC;i++)
        fin>>C[i];
    fin>>nD;
    for(int i=0;i<nD;i++)
        fin>>D[i];
    fin>>nS>>S;
    string s = "";
    for(int i=0;i<nS;i++)
    {
        s += S.substr(i,1);
        bool b = combine(s);
        if(!b)
           oppose(s);
    }
    for(int i=0;i<s.length();i++)
    {
        if(i!=0)
           fout<<", ";
        fout<<s[i];
    }
    fout<<"]\n";
}

int main()
{
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);
    //system("pause");
    return 0;
}
