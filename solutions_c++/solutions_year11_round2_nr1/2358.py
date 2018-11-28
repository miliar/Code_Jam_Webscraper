#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main(){

clrscr();
//int* N=new int[T];

ofstream output;
output.open("output.txt");
ifstream input;
input.open("input.txt");


int T;
input>>T;


for(int i=0;i<T;i++)
{
int N;
input>>N;

char **s=new char*[N];
long double *rpi=new long double[N];
long double *wp=new double[N];
double *owp=new double[N];
double *oowp=new double[N];

for(int j=0;j<N;j++)
{
s[j]= new char[N];
double w=0,t=0;
for(int k=0;k<N;k++){
input>>s[j][k];
//cout<<s[j][k]<<endl;
if(s[j][k]!='.')
{
t++;
if(s[j][k]=='1'){

w++;
   }
}

}
wp[j]=w/t;
cout<<wp[j]<<endl;
}

for(j=0;j<N;j++)
{
long double a=0;
long double total=0;
for(int k=0;k<N;k++)
{
long double wpp=0;
long double t=0,w=0;
for(int l=0;l<N;l++)
{
if(l!=j&&s[k][l]!='.')
{
t++;
if(s[k][l]=='1')
w++;
}


}
wpp=w/t;
if(s[j][k]!='.'&&j!=k)
{
total+=wpp;
a++;
}

}
owp[j]=total/a;
}


for(j=0;j<N;j++)
{
double a=0;
double total=0;
for(int k=0;k<N;k++)
{
if(s[j][k]!='.')
{
total+=owp[k];
a++;
}

}
oowp[j]=total/a;
}

output<<"Case #"<<i<<": "<<endl;

for(j=0;j<N;j++)
{
rpi[j]=0.25*wp[j]+0.50*owp[j]+0.25*oowp[j];
output<<rpi[j]<<endl;
}

}
output.close();
getch();

}