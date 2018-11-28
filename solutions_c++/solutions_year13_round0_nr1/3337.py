#include<iostream.h>
#include<string>
#include<fstream>
#include<list>
using namespace std;
char s[4][4];
string scan()
{string temp;int temp1=0;
for(int i=0;i<4;i++) {temp1=0;for(int i1=0;i1!=4;i1++) if((s[i][i1]=='T'||s[i][i1]=='O')) temp1++;
if(temp1==4) return "O won";}
for(int i=0;i<4;i++) {temp1=0;for(int i1=0;i1!=4;i1++) if((s[i][i1]=='T'||s[i][i1]=='X')) temp1++;
if(temp1==4) return "X won";}
for(int i=0;i<4;i++) {temp1=0;for(int i1=0;i1!=4;i1++) if((s[i1][i]=='T'||s[i1][i]=='O')) temp1++;
if(temp1==4) return "O won";}
for(int i=0;i<4;i++) {temp1=0;for(int i1=0;i1!=4;i1++) if((s[i1][i]=='T'||s[i1][i]=='X')) temp1++;
if(temp1==4) return "X won";}temp1=0;
for(int i=0;i<4;i++) {if((s[i][i]=='T'||s[i][i]=='O')) temp1++;
if(temp1==4) return "O won";}temp1=0;
for(int i=0;i<4;i++) {if((s[i][i]=='T'||s[i][i]=='X')) temp1++;
if(temp1==4) return "X won";}temp1=0;
for(int i=0;i<4;i++) {if((s[3-i][i]=='T'||s[3-i][i]=='O')) temp1++;
if(temp1==4) return "O won";}temp1=0;
for(int i=0;i<4;i++) {if((s[3-i][i]=='T'||s[3-i][i]=='X')) temp1++;
if(temp1==4) return "X won";}
for(int i=0;i<4;i++) for(int i1=0;i1!=4;i1++) if(s[i1][i]=='.') return "Game has not completed";
return "Draw";
}

int main()
{
    ifstream fin("in.IN");ofstream fo("out.txt");int T;
    fin>>T;
    for(int i=0;i<T;i++)
    {
        for(int i1=0;i1<4;i1++) fin>>s[i1];
       fo<<"Case #"<<i+1<<": "<< scan()<<endl;
    }
}
