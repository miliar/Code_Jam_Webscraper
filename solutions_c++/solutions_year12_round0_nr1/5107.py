#include<iostream>
#include<stdio.h>
#include<fstream>
#include<cstdlib>
#include<string.h>
using namespace std;

int t,l;
char g[30][101];
int main()
{
ifstream myfile("A-small-attempt1.in");
while(myfile.peek() != EOF)
{myfile>>t;
	int x=0;

while(x<=t)
{
 myfile.getline(g[x],101);

x++;
}
}
myfile.close();
for(int z=0;z<=t;z++)
{for(int y=0;y<=strlen(g[z]);y++)
{
l =(char)g[z][y]-96;

switch(l)
{case 25:
l=1;
break;
case 14:
l=2;
break;
case 6:
l=3;
break;
case 9:
l=4;
break;
case 3:
l=5;
break;
case 23:
l=6;
break;
case 12:
l=7;
break;
case 2:
l=8;
break;
case 11:
l=9;
break;
case 21:
l=10;
break;
case 15:
l=11;
break;
case 13:
l=12;
break;
case 24:
l=13;
break;
case 19:
l=14;
break;
case 5:
l=15;
break;
case 22:
l=16;
break;
case 26:
l=17;
break;
case 16:
l=18;
break;
case 4:
l=19;
break;
case 18:
l=20;
break;
case 10:
l=21;
break;
case 7:
l=22;
break;
case 20:
l=23;
break;
case 8:
l=24;
break;
case 1:
l=25;
break;
case 17:
l=26;
break;}
g[z][y]=96+l;
}if(z>0)
cout<<"Case #"<<z<<": "<<g[z]<<endl;
}

return 0;
}
