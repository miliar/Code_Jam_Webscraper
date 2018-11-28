#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

string git(string s)
{
 string mx="ourlangeismpbtdhwyxfckjv qz",my="ejpmyslckdxvnribtahwfoug zq";
 string res="";
 for(int i=0; i<s.length();i++)
  for(int k=0; k<my.length(); k++)
   if(s[i] == my[k])
    res+=mx[k];

   return res;   
}

int main()
{
    //ifstream cinn; cinn.open("A-small-attempt3.in");
    //ofstream out; out.open("A-small-attempt3.out");
    int cas = 1;
    int n;
    string s1;
    getline(cin,s1);
    stringstream ss; 
    ss << s1;
    ss>>n;
    
    while(cas<=n)
    {
              getline(cin,s1);
              
              if(cas==n)
               cout<<"Case #"<<cas++<<": "<<git(s1);
              else
               cout<<"Case #"<<cas++<<": "<<git(s1)<<endl;
    }
    
    //system("pause");
    return 0;                  
}
