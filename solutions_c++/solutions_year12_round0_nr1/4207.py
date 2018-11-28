#include<iostream>
#include<string>
#include<cstdio>

using namespace std;


int main()
{
 //freopen("A-small-attempt3.in","r",stdin);
 //freopen("A-small-attempt3.out","w",stdout);
    string ch;
    int n,len,i,j,t;
     cin>>t;
     cin.ignore();

     for(j=1;j<=t;j++)
{
    getline(cin,ch);

for( i=0; i<ch.size();i++)
{

   switch(ch[i])
       {
            case 'a' :
            ch[i]='y';
            break;

            case 'b' :
            ch[i]='h';
break;
            case 'c' :
            ch[i]='e';
break;
            case 'd' :
            ch[i]='s';
break;
            case 'e' :
            ch[i]='o';
break;
            case 'f' :
            ch[i]='c';
break;
            case 'g' :
            ch[i]='v';
break;
            case 'h' :
            ch[i]='x';
break;
            case 'i' :
            ch[i]='d';
break;
            case 'j' :
            ch[i]='u';
break;
            case 'k' :
            ch[i]='i';
break;
            case 'l' :
            ch[i]='g';
break;
            case 'm' :
            ch[i]='l';
break;
            case 'n' :
            ch[i]='b';
break;
            case 'o' :
            ch[i]='k';
break;
            case 'p' :
            ch[i]='r';
break;
            case 'q' :
            ch[i]='z';
break;
            case 'r' :
            ch[i]='t';
break;
            case 's' :
            ch[i]='n';
break;
            case 't' :
            ch[i]='w';
break;
            case 'u' :
            ch[i]='j';
break;
            case 'v' :
            ch[i]='p';
break;
            case 'w' :
            ch[i]='f';
break;
            case 'x' :
            ch[i]='m';
break;
            case 'y' :
            ch[i]='a';
break;
            case 'z' :
            ch[i]='q';
break;
            case ' ':
            ch[i]=' ';
      break;  }

        }

        cout<<"Case #"<<j<<": "<<ch<<"\n";


}
return 0;
}
