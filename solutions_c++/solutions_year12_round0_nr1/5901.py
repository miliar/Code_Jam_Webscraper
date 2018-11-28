#include<stdio.h>
#include<fstream>
#include<string.h>
#include<iostream>
using namespace std;
string a[31];
char func(char s)
{
    switch(s-'a')
    {
        case 0:return 'y';break;case 1:return 'h';break;case 2:return 'e';break;case 3:return 's';break;case 4:return 'o';break;case 5:return 'c';break;case 6:return 'v';break;case 7:return 'x';break;case 8:return 'd';break;case 9:return 'u';break;
        case 10:return 'i';break;case 11:return 'g';break;case 12:return 'l';break;case 13:return 'b';break;case 14:return 'k';break;case 15:return 'r';break;case 16:return 'z';break;case 17:return 't';break;case 18:return 'n';break;case 19:return 'w';break;
        case 20:return 'j';break;case 21:return 'p';break;case 22:return 'f';break;case 23:return 'm';break;case 24:return 'a';break;case 25:return 'q';
    }
}
int main ()
{

 ifstream inp("yoyyo.txt");
 for(int i=1;i<=30;i++)
 {

     //fgets(a[i-1],101,f);
     getline(inp,a[i-1]);
     int k=a[i-1].length();
     for(int j=0;j<k;j++)
     {
         if(a[i-1][j]!=' ')
         a[i-1][j]=func(a[i-1][j]);
     }
     //a[i-1][k-1]=' ';
     //for(int j=0;j<k;j++)a[j]=0;
 }
 ofstream out("output.txt");
 for(int i=1;i<=30;i++)
 {
     out<<"Case #"<<i<<": "<<a[i-1]<<"\n";
 }
return 0;
}
