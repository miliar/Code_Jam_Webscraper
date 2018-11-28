#include<iostream>
#include<cstdio>
#include<string>
#include<cctype>
using namespace std;

char change (char a)
{
    switch(a)
    {
        case 'a': return 'y';
        case 'b': return 'h';
        case 'c': return 'e';
        case 'd': return 's';
        case 'e': return 'o';
        case 'f': return 'c';
        case 'g': return 'v';
        case 'h': return 'x';
        case 'i': return 'd';
        case 'j': return 'u';
        case 'k': return 'i';
        case 'l': return 'g';
        case 'm': return 'l';
        case 'n': return 'b';
        case 'o': return 'k';
        case 'p': return 'r';
        case 'q': return 'z';
        case 'r': return 't';
        case 's': return 'n';
        case 't': return 'w';
        case 'u': return 'j';
        case 'v': return 'p';
        case 'w': return 'f';
        case 'x': return 'm';
        case 'y': return 'a';
        case 'z': return 'q';
    }

}
int main()
{
 // freopen("A-small-attempt1.in","r",stdin);
   //freopen("A-small-attempt1.out","w",stdout);

    int t,i;
    char c;
    string s;
    cin>>t;
    cin.ignore();
    for(int j=0;j<t;j++)
    {
        getline(cin,s);
        printf("Case #%d: ",j+1);
        for(i=0;i<s.size();i++)
        {
            c=s.at(i);
            if(isalpha(c))
            c=change(c);
            printf("%c",c);
        }
        cout<<endl;
    }

}
