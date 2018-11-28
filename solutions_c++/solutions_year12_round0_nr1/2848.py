#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdio.h>
#include <conio.h>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <list>
#include <vector>
#include <deque>
#include <functional>

#define pii 2*acos(0)
#define max 150

using namespace std;

int main()
{
    //vector<double> v;
    //list<double> ilist;
    //deque<double> ideq;
    int i=0,j,t,c;
    char ch[100][max],a;
    //string str[max];
    //cout<<setprecision(10)<<pii;
    ifstream infile("A-small-attempt0.in");
    infile>>t;
    infile>>a;
    while(!infile.eof())
    {

     infile.getline(ch[i],max);
     c=strlen(ch[i]);
     //cout<<ch[i]<<endl;
     //cout<<ch[0][0];
     if (i==0)
     {
      for (j=strlen(ch[0])-1;j>=0;j--)
      {
          ch[0][j+1]=ch[0][j];
      }

     ch[0][0]=a;
     //cout<<ch[0][0];
     c+=1;
     }
     for (j=0;j<c;j++)
     {   //cout<<ch[i][j];
         if (ch[i][j]=='a')ch[i][j]='y';
         else if  (ch[i][j]=='b')ch[i][j]='h';
         else if  (ch[i][j]=='c')ch[i][j]='e';
         else if(ch[i][j]=='d')ch[i][j]='s';
         else if(ch[i][j]=='e')ch[i][j]='o';
         else if(ch[i][j]=='f')ch[i][j]='c';
         else if(ch[i][j]=='g')ch[i][j]='v';
         else if(ch[i][j]=='h')ch[i][j]='x';
         else if(ch[i][j]=='i')ch[i][j]='d';
         else if(ch[i][j]=='j')ch[i][j]='u';
         else if(ch[i][j]=='k')ch[i][j]='i';
         else if(ch[i][j]=='l')ch[i][j]='g';
         else if(ch[i][j]=='m')ch[i][j]='l';
         else if(ch[i][j]=='n')ch[i][j]='b';
         else if(ch[i][j]=='o')ch[i][j]='k';
         else if(ch[i][j]=='p')ch[i][j]='r';
         else if(ch[i][j]=='q')ch[i][j]='z';
         else if(ch[i][j]=='r')ch[i][j]='t';
         else if(ch[i][j]=='s')ch[i][j]='n';
         else if(ch[i][j]=='t')ch[i][j]='w';
         else if(ch[i][j]=='u')ch[i][j]='j';
         else if(ch[i][j]=='v')ch[i][j]='p';
         else if(ch[i][j]=='w')ch[i][j]='f';
         else if(ch[i][j]=='x')ch[i][j]='m';
         else if(ch[i][j]=='y')ch[i][j]='a';
         else if(ch[i][j]=='z')ch[i][j]='q';
         //else if(ch[i][j]=='\r')ch[i][j]=0;

         //cout<<ch[i][j];
     }
     //cout<<endl;
     //cout<<ch[i]<<endl;
     i++;
    }
    infile.close();
    ofstream outfile("o.out");
    for (i=0;i<t;i++)
    {
      outfile<<"Case #"<<i+1<<": "<<ch[i];
      if (i!=t-1)
      outfile<<endl;
    }
    return 0;
}
