#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;

char s[1011];
int main()
{
    int t;
    cin>>t;
    gets(s);
for(int i=1;i<=t;i++)
{
    gets(s);
cout<<"Case #"<<i<<": ";
int h = strlen(s);
            for(int i=0;i<h;i++)
            {
                    
                    if(s[i]=='a')cout<<'y';
                    else if(s[i]=='b')cout<<'h';
                    else if(s[i]=='c')cout<<'e';
                    else if(s[i]=='d')cout<<'s';
                    else if(s[i]=='e')cout<<'o';
                    else if(s[i]=='f')cout<<'c';
                    else if(s[i]=='g')cout<<'v';
                    else if(s[i]=='h')cout<<'x';
                    else if(s[i]=='i')cout<<'d';
                    else if(s[i]=='j')cout<<'u';
                    else if(s[i]=='k')cout<<'i';
                    else if(s[i]=='l')cout<<'g';
                    else if(s[i]=='m')cout<<'l';
                    else if(s[i]=='n')cout<<'b';
                    else if(s[i]=='o')cout<<'k';
                    else if(s[i]=='p')cout<<'r';
                    else if(s[i]=='q')cout<<'z';
                    else if(s[i]=='r')cout<<'t';
                    else if(s[i]=='s')cout<<'n';
                    else if(s[i]=='t')cout<<'w';
                    else if(s[i]=='u')cout<<'j';
                    else if(s[i]=='v')cout<<'p';
                    else if(s[i]=='w')cout<<'f';
                    else if(s[i]=='x')cout<<'m';
                    else if(s[i]=='y')cout<<'a';
                    else if(s[i]=='z')cout<<'q';
                    else cout<<s[i];


            }
            cout<<endl;
}
    return 0;
}
