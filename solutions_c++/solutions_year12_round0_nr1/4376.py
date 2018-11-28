#include<iostream>
#include<string>
using namespace std;
string s;
int a;
int main()
{
    cin>>a;
    getline(cin, s);
    for(int i=1; i<=a; i++)
    {
      getline(cin, s);
        for(int j=0; j<s.size(); j++)
        {
            if(s[j]=='a'){s[j]='y';continue;}
            if(s[j]=='b'){s[j]='h';continue;}
            if(s[j]=='c'){s[j]='e';continue;}
            if(s[j]=='d'){s[j]='s';continue;}
            if(s[j]=='e'){s[j]='o';continue;}
            if(s[j]=='f'){s[j]='c';continue;}
            if(s[j]=='g'){s[j]='v';continue;}
            if(s[j]=='h'){s[j]='x';continue;}
            if(s[j]=='i'){s[j]='d';continue;}
            if(s[j]=='j'){s[j]='u';continue;}
            if(s[j]=='k'){s[j]='i';continue;}
            if(s[j]=='l'){s[j]='g';continue;}
            if(s[j]=='m'){s[j]='l';continue;}
            if(s[j]=='n'){s[j]='b';continue;}
            if(s[j]=='o'){s[j]='k';continue;}
            if(s[j]=='p'){s[j]='r';continue;}
            if(s[j]=='q'){s[j]='z';continue;}
            if(s[j]=='r'){s[j]='t';continue;}
            if(s[j]=='s'){s[j]='n';continue;}
            if(s[j]=='t'){s[j]='w';continue;}
            if(s[j]=='u'){s[j]='j';continue;}
            if(s[j]=='v'){s[j]='p';continue;}
            if(s[j]=='w'){s[j]='f';continue;}
            if(s[j]=='x'){s[j]='m';continue;}
            if(s[j]=='y'){s[j]='a';continue;}
            if(s[j]=='z'){s[j]='q';continue;}

        }
        cout<<"Case #"<<i<<": "<<s<<endl;
    }
    cin>>s;
}

