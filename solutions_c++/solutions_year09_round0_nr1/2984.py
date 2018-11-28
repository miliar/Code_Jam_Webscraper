#include<iostream>
#include<string>
using namespace std;
int main()
{
char ws[5000][15];
string p;
int L,D,T;
cin>>L;
cin>>D;
cin>>T;
int words=D;
int i=0;
while(words--)
{
cin>>ws[i++];
}
int cnum=1;
while(T--)
{
int pos;
cin>>p;
string temp=p;
bool incomplete=true;
bool destructon=false;
int toti=0;
while(incomplete)
{
int itr=0;
while(itr<temp.length())
{
if(temp[itr]=='(') destructon=true;
if(temp[itr]==')') {destructon=false;toti++;}
if(temp[itr]!='('&&temp[itr]!=')'&&(!destructon)) toti++;
itr++;
}
if(toti==L) {incomplete=false;}
else{
cin>>temp;
p+=temp;
}
}
int possis=0;
for(int k=0;k<D;k++)
{bool t=true;
bool letter;
pos=0;
for(int z=0;z<L;z++)
{
letter=false;
if(p[pos]=='(')
{
pos++;
while(p[pos]!=')')
{
if(p[pos++]==ws[k][z]){letter=true;}
}
}else if(p[pos]!=ws[k][z]){letter=false;}else if(p[pos]==ws[k][z]){letter=true;}
pos++;
t=t&letter;
}
if(t) possis++;
}
cout<<"Case #"<<cnum<<": "<<possis<<endl;
cnum++;
}
return 0;
}
