#include<iostream>
#include<fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

int main()
{
    int a[26]={0};
    a[0]=24;
    a[1]=7;
    a[2]=4;
    a[3]=18;
    a[4]=14;
    a[5]=2;
    a[6]=21;
    a[7]=23;
    a[8]=3;
    a[9]=20;
    a[10]=8;
    a[11]=6;
    a[12]=11;
    a[13]=1;
    a[14]=10;
    a[15]=17;
    a[16]=25;
    a[17]=19;
    a[18]=13;
    a[19]=22;
    a[20]=9;
    a[21]=15;
    a[22]=5;
    a[23]=12;
    a[24]=0;
    a[25]=16;
    
    freopen ("A-sample.in","r",stdin);
    freopen ("A-output.out","w",stdout);
    
    
    int i=0;
    int k;
    
    int t=0;
    
        char ch[3];
        cin.getline( ch, 3, '\n' );
        k=atoi(ch);
        
    while(t<k)
    {
         char x[101];
         char z[101];
        cin.getline( x, 101, '\n' );
        int end=(unsigned)strlen(x);
        i=0;
        while(x[i]!='\0')
        {
                           if(x[i]>='a' && x[i]<='z')
                                        z[i]='a'+ a[x[i]-'a'];
                           else
                               z[i]=x[i];             
                         i++;
        }
        z[i]='\0';
        i=0;
        cout<<"Case #"<<t+1<<": ";
        while(z[i]!='\0')
        {
                         cout<<z[i++];
        }   
        cout<<endl;             
        t++;
    }
    
}
