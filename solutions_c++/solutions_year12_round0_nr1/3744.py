#include<iostream>
#include<cmath>
#include<fstream>
#include<cstring>
using namespace std;
int main()
{

char trans[27];
strcpy(trans,"yhesocvxduiglbkrztnwjpfmaq");
int tests,n;
cin>>tests;
ofstream f;
f.open("output.txt");
char input[301];
char output[301];
for(n=0;n<tests;n++)
{
int i;
i=0;
char c;

cin.getline(input,300);
if(n==0)
cin.getline(input,300);
int length;
length=strlen(input);
for(i=0;i<length;i++)
{
output[i]=input[i];
if(output[i]>='a' && output[i]<='z')
output[i]=trans[input[i]-'a'];
}
output[i]=0;
f<<"Case #"<<n+1<<": "<<output<<endl;
cout<<"Case #"<<n+1<<": "<<output<<endl;

}
f<<flush;
f.close();

return 0;
}
