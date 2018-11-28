#include<iostream>
#include<string>
#include<cstring>
using namespace std;
int main()
{
    char a[26];
    char str[1000];
    int i,j,p;
    string s[3],str1;
    string s1[3];
    s[0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    s[1]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    s[2]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    s1[0]="our language is impossible to understand";
    s1[1]="there are twenty six factorial possibilities";
    s1[2]="so it is okay if you want to just give up";
    for(i=0;i<3;i++)
    {
        for(j=0;j<s[i].size();j++)
        {
            if(s[i][j]>=97)
            {
                p=s[i][j]-97;
                a[p]=s1[i][j];
            }
        }
    }
    a[25]='q';
    a[16]='z';
    int t;
    p=1;
    cin>>t;
    cin.ignore();
    while(t--)
    {
        //string str1;
        //cin.ignore();
        cin.getline(str,1000);
        str1.clear();
        for(i=0;i<strlen(str);i++)
        {
            if(str[i]>=97)
            {
                str1=str1+a[str[i]-97];
            }
            else
                str1=str1+str[i];
        }
        cout<<"Case #"<<p<<": "<<str1<<endl;
        p++;
    }
}


