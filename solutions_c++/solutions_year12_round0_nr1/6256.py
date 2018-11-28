#include<iostream>
#include<stdio.h>
#include<map>
using namespace std;
main()
{
       int t,i=0;
       char c[100];
       cin>>t;
       getchar();
       FILE *fp;
       fp=fopen("output.txt","w");
       map<char,char>arr;
       arr['a']='y'; arr['b']='h';arr['c']='e'; arr['d']='s';arr['e']='o';arr['f']='c';arr['g']='v';arr['h']='x';arr['i']='d';arr['j']='u';arr['k']='i';arr['l']='g';arr['m']='l';arr['n']='b';arr['o']='k';arr['p']='r';arr['q']='z';arr['r']='t';arr['s']='n';arr['t']='w';arr['u']='j';arr['v']='p';arr['w']='f';arr['x']='m';arr['y']='a';arr['z']='q';arr[' ']=' ';
     while(t--)
    {        
        gets(c);
        fprintf(fp,"Case #%d: ",i+=1);
        for(int k=0;k<strlen(c);k++){
                  fprintf(fp,"%c",arr[c[k]]);}
                  fprintf(fp,"\n");
                  }
                  }      
