#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
int T;
int i;
char G[30][101];
cin>>T;
cin.clear();
cin.ignore(1000,'\n');

//cin.getline(G[0],256,'\n');
for (i = 0 ; i < T; ++i)
	cin.getline(G[i],101,'\n');
	

for (int j = 0; j < T; ++j)
{
i=0;
while(G[j][i])
{	switch(G[j][i])
	{
		case 'y' : G[j][i] = 'a'; break;
		case 'n' : G[j][i] = 'b'; break;
		case 'f' : G[j][i] = 'c'; break;
		case 'i' : G[j][i] = 'd'; break;
		case 'c' : G[j][i] = 'e'; break;
		case 'w' : G[j][i] = 'f'; break;
		case 'l' : G[j][i] = 'g'; break;
		case 'b' : G[j][i] = 'h'; break;
		case 'k' : G[j][i] = 'i'; break;
		case 'u' : G[j][i] = 'j'; break;
		case 'o' : G[j][i] = 'k'; break;
		case 'm' : G[j][i] = 'l'; break;
		case 'x' : G[j][i] = 'm'; break;
		case 's' : G[j][i] = 'n'; break;
		case 'e' : G[j][i] = 'o'; break;
		case 'v' : G[j][i] = 'p'; break;
		case 'z' : G[j][i] = 'q'; break;
		case 'p' : G[j][i] = 'r'; break;
		case 'd' : G[j][i] = 's'; break;
		case 'r' : G[j][i] = 't'; break;
		case 'j' : G[j][i] = 'u'; break;
		case 'g' : G[j][i] = 'v'; break;
		case 't' : G[j][i] = 'w'; break;
		case 'h' : G[j][i] = 'x'; break;
		case 'a' : G[j][i] = 'y'; break;
		case 'q' : G[j][i] = 'z'; break;
		case ' ' : G[j][i] = ' '; break;
	}// end of switch
	++i;
}//end of while
}//end of for

//print the output
for (i=0; i<T ;++i)
	cout<<"Case #"<<i+1<<':'<<' '<<G[i]<<'\n';

}//end of main
