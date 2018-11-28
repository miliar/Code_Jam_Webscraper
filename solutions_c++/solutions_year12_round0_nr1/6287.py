#include <iostream>
#include <fstream>
#include <string>


using namespace std;
#define fout cout

char cha[]={'q','a','m','f','p','j','w','n','t','z','r','k','b','l','g','i','u','d','x','v','c','o','s','e','h','y'};
char getChange(char ch)
{
     return cha[('z'-ch)];
}

int main()
{
    int test;
    ifstream fin("A-small-attempt10.in",ios::in);
    ofstream fout("A-small-attempt10.out",ios::out);
    int n;
    fin>>n;
    int i;
    for(i=0;i<=n;i++){
        string str;
        sizeof(str,0,sizeof(str));
        getline(fin,str);
        if(i==0) continue;
        int number=0;
        int len=str.length();
        cout<<"Case #"<<i<<": ";
        for(number=0;number<len;number++){
            if((str[number]>='a')&&(str[number]<='z'))cout<<getChange(str[number]);
            else cout<<str[number];
        }
        if(i!=n)cout<<endl;
    }
    return 0;
}
