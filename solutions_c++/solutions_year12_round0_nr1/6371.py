#include <iostream.h>
#include <conio.h>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

void scribe()
{
     freopen("0.in","r",stdin);
     freopen("0.out","w",stdout);
}

int main()
{
map<char,char> mapStr;

string str_in = "qzejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string str_out = "zqour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

//cout<<str_in.length();
for(int i = 0;i<str_in.length();i++)
mapStr[str_in[i]] = str_out[i];



scribe();

int nTests;
scanf("%d ",&nTests);

string in;
string out = "";

for(int i = 0 ; i < nTests ; i++)
{


getline(cin,in);


printf("Case #%d: ",i+1);
for(int i = 0;i<in.length();i++)
{
out[i] = mapStr[in[i]];
printf("%c",out[i]);

}
printf("\n");

}

return 0;

}
