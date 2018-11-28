#include<iostream>
#include<string>
#include<map>
#include<cstring>
#include<cstdio>
#include<fstream>

using namespace std;

const char *in;

int main()
{
    string str;
    int T,c=1;
    string text;

  // freopen("A-small-attempt2.in","r",stdin);
  // freopen("A-small-attempt2.out","w",stdout);


    cin>>T;
    getchar();

    while(T--)
    {
        getline(cin,str);

        cout<<"Case #"<<c++<<": ";//<<endl;

        int len = str.size();

        for(int i=0;i<=len;i++)
        {
            switch(str[i])
            {
                case 'a': cout<<'y';break;
                case 'b': cout<<'h';break;
                case 'c': cout<<'e';break;
                case 'd': cout<<'s';break;
                case 'e': cout<<'o';break;
                case 'f': cout<<'c';break;
                case 'g': cout<<'v';break;
                case 'h': cout<<'x';break;
                case 'i': cout<<'d';break;
                case 'j': cout<<'u';break;
                case 'k': cout<<'i';break;
                case 'l': cout<<'g';break;
                case 'm': cout<<'l';break;
                case 'n': cout<<'b';break;
                case 'o': cout<<'k';break;
                case 'p': cout<<'r';break;
                case 'q': cout<<'z';break;//may create problem
                case 'r': cout<<'t';break;
                case 's': cout<<'n';break;
                case 't': cout<<'w';break;
                case 'u': cout<<'j';break;
                case 'v': cout<<'p';break;
                case 'w': cout<<'f';break;
                case 'x': cout<<'m';break;
                case 'y': cout<<'a';break;
                case 'z': cout<<'q';break;
                default : cout<<' ';break;
            }


        }
        cout<<endl;
    }

  //  cout.close();
return(0);
}
