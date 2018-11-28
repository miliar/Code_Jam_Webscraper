#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>
using namespace std;

int main()
{
freopen("aho.txt","w",stdout);

int goog,surp,t,p,total,final;
goog=surp=t=p=total=final=0;
string yo;
int counter,temp,a,b,c,d,e,f,g,h;
a=b=c=d=e=temp=f=g=h=0;
ifstream file("B-large.in");

getline(file,yo);
char *string=(char *)yo.c_str();
t=atoi(string);

for(a=0;a<t;a++)
{
goog=surp=p=0;
getline(file,yo,' ');
char *string1=(char *)yo.c_str();
goog=atoi(string1);

getline(file,yo,' ');
char *string2=(char *)yo.c_str();
surp=atoi(string2);

getline(file,yo,' ');
char *string3=(char *)yo.c_str();
p=atoi(string3);

int arr[goog];

for(b=0;b<goog-1;b++)
{
getline(file,yo,' ');
char *string4=(char *)yo.c_str();
arr[b]=atoi(string4);

}
getline(file,yo,'\n');
char *string5=(char *)yo.c_str();
arr[b]=atoi(string5);


total=p*3;

for(b=0;b<goog;b++)
{
if(arr[b]==0)
{

if((total-arr[b])==0)
{
final++;
}

}
else if((total-arr[b])<=0)
{
final++;

}
else if( (total-arr[b])<=2&&(total-arr[b])>=1 )
{
final++;

}

else if( (total-arr[b])<=4&& surp>0&&(total-arr[b])>=3 )
{
final++;
surp--;

}


}
cout<<"Case #"<<(a+1)<<":"<<" "<<final<<'\n';
final=0;
}




file.close();
return 0;
}
