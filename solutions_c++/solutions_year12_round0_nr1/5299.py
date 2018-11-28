#include<iostream>
#include<fstream>
#include<conio.h>
#include<string>
#include<map>
using namespace std;
int main()
{
    char a[26];
a[0]='y';
a[1]='h';
a[2]='e';
a[3]='s';
a[4]='o';
a[5]='c';
a[6]='v';
a[7]='x';
a[8]='d';
a[9]='u';
a[10]='i';
a[11]='g';
a[12]='l';
a[13]='b';
a[14]='k';
a[15]='r';
a[16]='z';
a[17]='t';
a[18]='n';
a[19]='w';
a[20]='j';
a[21]='p';
a[22]='f';
a[23]='m';
a[24]='a';
a[25]='q';
    map<char,char> arr;
    map<char,char>::iterator it;
    ofstream f;
    ifstream fip;
    f.open("op.txt",ios::out);
    fip.open("A-small-attempt0.in",ios::in);
    /*string str,str1;
    getline(fip,str);
    getline(fip,str1);
    for(int i=0;str[i]!='\0';i++)
    {
            arr.insert(pair<char,char>(str[i],str1[i]));
    }
    getline(fip,str);
    getline(fip,str1);
    for(int i=0;str[i]!='\0';i++)
    {
            arr.insert(pair<char,char>(str[i],str1[i]));
    }
    getline(fip,str);
    getline(fip,str1);
    for(int i=0;str[i]!='\0';i++)
    {
            arr.insert(pair<char,char>(str[i],str1[i]));
    }
    for(int i=0;i<26;i++)
    {
            f<<"a["<<i<<"]='"<<(arr.find('a'+i))->second<<"';"<<endl;
            cout<<(char)('a'+i)<<" "<<(arr.find('a'+i))->second<<endl;
    }*/
    /*while(f)
    {
            char a,b;
            f>>a>>b;
            arr.insert(pair<char,char>(a,b));
            cout<<(int)(a-'a')<<" "<<(int)(b-'a')<<endl;
    }
    */
    
    for(int i=0;i<26;i++)
    {
            arr.insert(pair<char,char>('a'+i,a[i]));
    }
    int t;
    string str;
    fip>>t;
    getline(fip,str);
    for(int i=0;i<t;i++)
    {
              getline(fip,str);
              f<<"Case #"<<i+1<<": ";
              for(int j=0;str[j]!='\0';j++)
              {
                      if(str[j]!=' ')
                          f<<(arr.find(str[j]))->second;
                      else
                          f<<" ";
              }
              f<<endl;
    }
    f.close();
    fip.close();
    //getch();
    return 0;
}
