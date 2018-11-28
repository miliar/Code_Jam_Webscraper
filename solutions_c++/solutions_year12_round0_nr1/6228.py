#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;

int main()
{
    int t;
    char arr[28];
    arr[(int)'a'-97]='y';
    arr[(int)'b'-97]='h';
    arr[(int)'c'-97]='e';
    arr[(int)'d'-97]='s';
    arr[(int)'e'-97]='o';
    arr[(int)'f'-97]='c';
    arr[(int)'g'-97]='v';
    arr[(int)'h'-97]='x';
    arr[(int)'i'-97]='d';
    arr[(int)'j'-97]='u';
    arr[(int)'k'-97]='i';
    arr[(int)'l'-97]='g';
    arr[(int)'m'-97]='l';
    arr[(int)'n'-97]='b';
    arr[(int)'o'-97]='k';
    arr[(int)'p'-97]='r';
    arr[(int)'q'-97]='z';
    arr[(int)'r'-97]='t';
    arr[(int)'s'-97]='n';
    arr[(int)'t'-97]='w';
    arr[(int)'u'-97]='j';
    arr[(int)'v'-97]='p';
    arr[(int)'w'-97]='f';
    arr[(int)'x'-97]='m';
    arr[(int)'y'-97]='a';
    arr[(int)'z'-97]='q';
    
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.txt");
    
    fin>>t;
    string s;
    getline(fin,s);     //needed
    int cnt=0;
    
    while(t--)
    {
     ++cnt;
     getline(fin,s);
     int l=s.length();
     for(int i=0;i<l;++i)
     {
      if(s[i]>='a' && s[i]<='z')
      {
       s[i]=arr[(int)s[i]-97];
      }
      else if(s[i]>='A' && s[i]<='Z')
           {
            s[i]=arr[(int)s[i]-65];
           }
     }
     fout<<"Case #"<<cnt<<": "<<s<<"\n";
    }
    
    fin.close();
    fout.close();
    
    //system("pause");
    return 0;
}
     
