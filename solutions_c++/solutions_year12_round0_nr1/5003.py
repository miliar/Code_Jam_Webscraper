#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,i,w;
    string p="yhesocvxduiglbkrztnwjpfmaq";
    string s,c;
    scanf("%d",&t);
    c=getchar();
    ofstream fout;
    fout.open("out2.txt");
    for(w=0;w<t;w++)
    {
                     getline(cin,s);
                     int i=0;
                     fout<<"Case #"<<w+1<<": ";
                     int l=s.length();
                     for(i=0;i<l;i++)
                     {
                                     if(s[i]!=32)
                                      {
                                      int pos=s[i]-'a';
                                      s[i]=p[pos];
                                      }
                                      
                                      fout<<s[i];
                     }
                    fout<<endl; 
    }
    fout.close();
    //system("pause");
    return 0;
}
                     
                     
    
