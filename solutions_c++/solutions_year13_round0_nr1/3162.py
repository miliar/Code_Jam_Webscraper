#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<sstream>
#include<complex.h>
#include<fstream>
#include<stdlib.h>
#include<math.h>
using namespace std;
int main()
{
ifstream file;
ofstream file1;
file.open("inp.txt");
file1.open("out.txt");
int t;
string s;
file>>t;
getline(file,s);
for(int k=0;k<t;k++)
{
bool flag=0;
vector< vector<char> >input;
for(int i=0;i<4;i++)
{
string s;
getline(file,s);
const char *str=s.c_str();
vector<char>inp;
for(int j=0;j<4;j++)
{
if(str[j]=='O')
inp.push_back(19);
else if(str[j]=='X')
inp.push_back(23);
else if(str[j]=='T')
inp.push_back(29);
else
{flag=1;
inp.push_back(1);
}
}
input.push_back(inp);
}
getline(file,s);
int prod2=1;
int prod3=1;
for(int j=0;j<4;j++)
{
prod2*=input[j][j];
prod3*=input[j][3-j];
}
if(prod2==pow(19,4)||prod2==29*pow(19,3))
{
file1<<"Case #"<<k+1<<": O won"<<"\n";
goto label;
}
else if(prod2==pow(23,4)||prod2==29*pow(23,3))
{
file1<<"Case #"<<k+1<<": X won"<<"\n";
goto label;
}
if(prod3==pow(19,4)||prod3==29*pow(19,3))
{
file1<<"Case #"<<k+1<<": O won"<<"\n";
goto label;
}
else if(prod3==pow(23,4)||prod3==29*pow(23,3))
{
file1<<"Case #"<<k+1<<": X won"<<"\n";
goto label;
}

for(int i=0;i<4;i++)
{
int prod=1;
int prod1=1;
for(int j=0;j<4;j++)
{
prod*=input[i][j];
prod1*=input[j][i];
}
if(prod==pow(19,4)||prod==29*pow(19,3))
{
file1<<"Case #"<<k+1<<": O won"<<"\n";
goto label;
}
else if(prod==pow(23,4)||prod==29*pow(23,3))
{
file1<<"Case #"<<k+1<<": X won"<<"\n";
goto label;
}
else if(prod1==pow(19,4)||prod1==29*pow(19,3))
{
file1<<"Case #"<<k+1<<": O won"<<"\n";
goto label;
}
else if(prod1==pow(23,4)||prod1==29*pow(23,3))
{
file1<<"Case #"<<k+1<<": X won"<<"\n";
goto label;
}

}
if(flag==1)
file1<<"Case #"<<k+1<<": Game has not completed"<<"\n";
else
file1<<"Case #"<<k+1<<": Draw"<<"\n";
label:;
}
return 0;
}
