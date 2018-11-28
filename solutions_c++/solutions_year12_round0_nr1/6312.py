#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
int main()
{
int arr[27];
arr[1]=25;
arr[2]=8;
arr[3]=5;
arr[4]=19;
arr[5]=15;
arr[6]=3;
arr[7]=22;
arr[8]=24;
arr[9]=4;
arr[10]=21;
arr[11]=9;
arr[12]=7;
arr[13]=12;
arr[14]=2;
arr[15]=11;
arr[16]=18;
arr[17]=26;
arr[18]=20;
arr[19]=14;
arr[20]=23;
arr[21]=10;
arr[22]=16;
arr[23]=6;
arr[24]=13;
arr[25]=1;
arr[26]=17;
for(int k=1;k<=26;k++)
cout<<arr[k]<<endl;

char c;
string line;
int t;
int i=0,j;
ifstream dh("A-small-attempt0.in");
ofstream dhee;
dhee.open("output.txt");
dh>>t;
while(!dh.eof())
{
getline(dh,line);
cout<<line<<endl;
if(i!=0 && i<=t)
{
dhee<<"Case #"<<i<<": ";
for(j=0;j<line.size();j++)
{
if(97<=(int)line[j] && (int)line[j]<=123)
{
dhee<<(char)(arr[(int)line[j]-96]+96);
}
else
dhee<<" ";
}
dhee<<endl;
}
i++;
}
dh.close();
dhee.close();
return 0;
}
