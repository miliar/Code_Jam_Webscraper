#include<iostream>
#include<string.h>
#include<math.h>
#include<fstream>
using namespace std;

int main()
{

ifstream in("ms1");
ofstream out("dd1.out");

if(!in)
{
cout<<"error";
}

char google_erse[3][100]={"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char target[30][100]={"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};

char googleerse[100],targ[100];

char a[26];
a[25]='q';
a[16]='z';

for(int i=0;i<3;i++)
 {  
  for(int j=0;j<strlen(google_erse[i]);j++)
    {
     if((int(google_erse[i][j])-97)>=0)
       {
        a[int(google_erse[i][j])-97]=int(target[i][j]);
        
       }
    }
 }
 
 for(int j=0;j<26;j++)
 {
  cout<<char(97+j)<<"-"<<a[j]<<endl;
 }

int z,sw,sn,l,k,flag,p[10],nug;

in>>l;
cout<<l<<endl;
in.getline(googleerse,100);
 for(k=1;k<=l;k++)
  {
    strcpy(googleerse,"");
    strcpy(targ,"");
    in.getline(googleerse,101);
    googleerse[strlen(googleerse)]='\0';
    cout<<googleerse<<endl;
    
    for(int j=0;j<strlen(googleerse);j++)
     {
       if((int(googleerse[j])-97)>=0)
        {
         targ[j]=a[int(googleerse[j])-97];
         //cout<<targ[j]<<endl;
        }
       else
        {
          targ[j]=googleerse[j];
          //cout<<targ[j]<<endl;
        }
     }
     targ[strlen(googleerse)]='\0';
     //cout<<targ<<endl;
     out<<"Case #"<<k<<": "<<targ<<"\n";
     strcpy(googleerse,"");
     strcpy(targ,"");
   }
     
return 0;
}

