#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

int main()
{
FILE *file;
FILE *outfile;
file = fopen( "a-large.in", "r" );
outfile = fopen("f.out","w");
int testcases,count=0;
fscanf(file,"%d",&testcases);
while(count<testcases)
{ char c;
int o[150],sequencelength;
int b[150];
int sequence[150];
for(int i=0;i<100;i++)
{   o[i] = -1;
   b[i] = -1;
   sequence[i] = -1;
}
o[0]=1;
b[0]=1;
int count_o=1,count_b=1;
int i=0;
fscanf(file,"%d",&sequencelength);
for(i=0;i<sequencelength;i++)
{
fscanf(file,"%c",&c);
if( c == 'O' )
{
fscanf(file,"%d",&o[count_o]);
count_o++;
sequence[i]=1;
}
else if( c == 'B' )
{   fscanf(file,"%d",&b[count_b]);
count_b++;
sequence[i]=2;
}
else{i--;}
}
count_o=1;count_b=1;i=0;
int waito=0,waitb=0,totaltimeo=0,totaltimeb=0,addtime=0;

for(i=0;i<sequencelength;i++)
{ addtime=0;
if(sequence[i]==1)
{  if(o[count_o]>o[count_o-1])
addtime = o[count_o]-o[count_o-1];
  else if(o[count_o]<o[count_o-1])
addtime = o[count_o-1]-o[count_o];
  
  count_o++;
  addtime = addtime-waito;
  if(addtime<0)
  {addtime=0;}
  addtime++;
  waito=0;
  waitb=waitb+addtime;
  totaltimeo = totaltimeo+addtime;
             }
if(sequence[i]==2)
{  if(b[count_b]>b[count_b-1])
addtime = b[count_b]-b[count_b-1];
  else if(b[count_b]<b[count_b-1])
addtime = b[count_b-1]-b[count_b];
  
  count_b++;
  addtime = addtime-waitb;
  if(addtime<0)
  {addtime=0;}
  waitb=0;
  addtime++;
  waito=waito+addtime;
  totaltimeb = totaltimeb+addtime;

}
}
fprintf(outfile,"Case #%d: %d\n",count+1,totaltimeo+totaltimeb);

        count++;
}
return 0;
}
