#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    char s[106],a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t=0,n=1;
    ifstream f("C:\\Users\\avi\\Desktop\\input.in",ios::in);
    ofstream of("C:\\Users\\avi\\Desktop\\output.out");
    f.getline(s,105);
    t=s[0]-48;
    t=t*10 +( s[1]-48);
    while(t--)
    {
       for(int i=0;i<101;s[i]='\0',i++);
       f.getline(s,105);
       of<<"Case #"<<n++<<": ";
       for(int i=0;s[i]!='\0';i++)
       {
           if(s[i]==' ')
           of<<" ";
           else
           of<<a[s[i]-97];
       }
       of<<endl;
    }
    f.close();
    of.close();
system("pause");
}
