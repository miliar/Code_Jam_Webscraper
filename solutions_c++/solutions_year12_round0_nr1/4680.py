#include <iostream>
#include <string>
#include <fstream>

using namespace std;

const string s1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
const string s11="our language is impossible to understand";
const string s2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
const string s22="there are twenty six factorial possibilities";
const string s3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
const string s33="so it is okay if you want to just give up";
 
int main()
{
    int l1,l2,l3,i;
    l1=s1.length();
    l2=s2.length();
    l3=s3.length();
    char a[26];
    for (i=0;i<26;i++) a[i]='a'+i;
    for (i=0;i<l1;i++)
    {
        int c=s1[i]-'a';
        a[c]=s11[i];
    }
    for (i=0;i<l2;i++)
    {
        int c=s2[i]-'a';
        a[c]=s22[i];
    }
    for (i=0;i<l3;i++)
    {
        int c=s3[i]-'a';
        a[c]=s33[i];
    }
    a['z'-'a']='q';
    a['q'-'a']='z';
    int n,j,l;
    char c;
    ifstream fin("A-small-attempt.in");
    ofstream fout("A-small-attempt.out");
    fin>>n;
    c=fin.get();
    for (i=1;i<=n;i++)
    {
        string b="";
        char ch;
        while ((ch=fin.get())!='\n')
        { 
              if (ch!=' ') c=a[ch-'a'];
              else c=ch;
              b=b+c;
        }
        fout<<"Case #"<<i<<": "<<b<<endl; 
    }
    return 0;
}
