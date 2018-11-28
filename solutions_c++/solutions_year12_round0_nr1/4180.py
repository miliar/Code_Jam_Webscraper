#include<iostream>

#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
    char a[26];
    a[0]='y';
    a[1]='h';
    a[2]='e';
    a[3]='s';
    a[4]='o';
    a[5]='c';
    a[6]='v';
    a[7]='x';
    a[8]='d';
    a[9]='u';
    a[10]='i';
    a[11]='g';
    a[12]='l';
    a[13]='b';
  // here4
    a[14]='k';
    a[15]='r';
  //here2
    a[16]='z';
    a[17]='t';
    a[18]='n';
    a[19]='w';
    a[20]='j';
    a[21]='p';
    a[22]='f';
    a[23]='m';
    a[24]='a';
// here
    a[25]='q';
   // ifstream infile("input.txt");
   // ofstream outfile("output.txt");
    char c[100];
 int n=31;
 char tt;
cin>>n;
int count=0;   
 while(count!=n+1)
    {
//cout<<"Case #"<<count<<": "; 
           gets(c);
if(count!=0)
{
cout<<"Case #"<<count<<": ";   
 int y=strlen(c);
    for(int i=0;i<y;i++)
    {
 here:	          
 tt=c[i];
if(isdigit(tt))
{
i++;
goto here;
}
            if(!isdigit(tt))
           { 
            if(c[i]==' ')
            {
            cout<<" ";
            }
            else
            {
                cout<<a[c[i]-97];
                }
                }
     //       cout<<endl;
            }
            cout<<endl;
}
count++;
}

 //   infile.close();
   // outfile.close();
   
    return(0);
    }
