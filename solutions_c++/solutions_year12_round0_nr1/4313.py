#include<iostream>
#include<fstream>
using namespace std;
int a[26];
int main()
{
    ifstream fin1,fin2;
    fin1.open("input1.txt");
    fin2.open("input2.txt");
    char c1,c2;
    for(int i=0;i<26;i++)a[i]=(int)(' ')-97;
    a[(int)('q')-97]=(int)('z')-97;
    while(!fin1.eof())
    {
    fin1>>c1;fin2>>c2;
    if(c1!=' ')
             a[(int)c1-97] = (int)c2 - 97;
    }
    a[25]=(int)('q')-97;
   /*for(int i=0;i<26;i++)
    {
            cout<<(char)(i+97)<<"---->"<<(char)(a[i]+97)<<endl;
    }
    */
    string str;
    fin1.close();fin2.close();
    ifstream fin;fin.open("input.txt");
    ofstream fout;fout.open("output.txt");
    int t;fin>>t;
    getline(fin,str);
    for(int i=1;i<=t;i++)
    {
            fout<<"Case #"<<i<<": ";
            getline(fin,str);
            for(int j=0;j<str.length();j++){if(str[j]==' ')fout<<' ';else fout<<(char)(a[(int)str[j]-97]+97);}
            fout<<endl;
    }
    
}
    
