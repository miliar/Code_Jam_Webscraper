#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
int T;
string frase;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>T;
    for(int j=0;j<=T;j++)
    {
        getline(cin,frase);
        int tam=frase.size();
        for(int i=0;i<tam;i++)
        {
            switch (frase[i])
            {
                case 'a':
                frase[i]+=24;
                break;
                case 'b':
                frase[i]+=6;
                break;
                case 'c':
                frase[i]+=2;
                break;
                case 'd':
                frase[i]+=15;
                break;
                case 'e':
                frase[i]+=10;
                break;
                case 'f':
                frase[i]-=3;
                break;
                case 'g':
                frase[i]+=15;
                break;
                case 'h':
                frase[i]+=16;
                break;
                case 'i':
                frase[i]-=5;
                break;
                case 'j':
                frase[i]+=11;
                break;
                case 'k':
                frase[i]-=2;
                break;
                case 'l':
                frase[i]-=5;
                break;
                case 'm':
                frase[i]-=1;
                break;
                case 'n':
                frase[i]-=12;
                break;
                case 'o':
                frase[i]-=4;
                break;
                case 'p':
                frase[i]+=2;
                break;
                case 'q':
                frase[i]+=9;
                break;
                case 'r':
                frase[i]+=2;
                break;
                case 's':
                frase[i]-=5;
                break;
                case 't':
                frase[i]+=3;
                break;
                case 'u':
                frase[i]-=11;
                break;
                case 'v':
                frase[i]-=6;
                break;
                case 'w':
                frase[i]-=17;
                break;
                case 'x':
                frase[i]-=11;
                break;
                case 'y':
                frase[i]-=24;
                break;
                case 'z':
                frase[i]-=9;
                break;
                case ' ':
                break;
            }
        }
        if(j>0)
            cout<<"Case #"<<j<<": "<<frase<<endl;
    }
}
