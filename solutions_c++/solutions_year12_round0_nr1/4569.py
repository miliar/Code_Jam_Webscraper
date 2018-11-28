#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    int t,i,a[26],len=0,x,j;
    string s1,s2;
    scanf("%d\n",&t);
    ofstream ef;
    s1="yhesocvxduiglbkrztnwjpfmaq";
    ef.open("output.txt");
    for(j=0;j<t;j++)
    {
              getline(cin,s2);
              len=s2.length();
              for(i=0;i<len;i++)
              {
                                x=s2[i];
                                if(x!=32){
                                x-=97;
                                s2[i]=s1[x];}
              }
              ef<<"Case #"<<j+1<<": "<<s2<<"\n";
    }
    ef.close();
    return 0;
}
