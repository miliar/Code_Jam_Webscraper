#include<iostream>
#include<fstream>
#include <string>
using namespace std;
int main()
{
    string s;
    string str;
    char ar[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

fstream fout("output.txt",ios::out);
//ifstream fin;
//fin.open("A-small-attempt1.txt");
int test=0,i=0,j=0,l=0;
cin >> test;
//cout<<test;
cin.ignore();
for(i=1;i<=test;i++)
{
l=0;
getline(cin,str);
cout<<str<<endl;
l=str.length();
for(j=0;j<l;j++)
{
                if(str[j]!=' ')
                {
                             str[j]=ar[str[j]-97];
                }
}
//cout<<str<<endl;
fout <<"Case #"<<(i)<<": "<<str<< "\n";
}

return 0;
}
