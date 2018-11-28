#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<sstream>
#include<queue>
#include<cstdio>

using namespace std;

string magic[]={"ay","uj","zq","ikoecfwtrpvglmxhbnsd"};
const int NMAGIC=4;

char decode[27];

void parseMagic()
{
    int i,j,J,nj;

    for(i=0;i<NMAGIC;i++)
    {
        J=magic[i].length();
        for(j=0;j<J;j++)
        {
            nj=j+1; if(nj==J) nj=0;
            decode[magic[i][nj]-'a']=magic[i][j];
        }
    }
}

char buf[100000000];
void test()
{
    cin.getline(buf,100000);
    int N=strlen(buf),i;

    for(i=0;i<N;i++)
        {
            if(buf[i]==' ') cout<<' ';
            else cout<<decode[buf[i]-'a'];
        }
    //cout<<endl;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);



    int i,I;
    cin>>I;

    cin.getline(buf,100000);
    parseMagic();

    for(i=0;i<I;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        test();
        cout<<endl;
    }
    return 0;
}
