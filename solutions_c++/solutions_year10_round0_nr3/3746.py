#include<fstream.h>
#include<stdio.h>
#include<string.h>
#include<conio.h>

struct group
{
long lnomem;
int displacement;
long sum;
};


long evaluate(long R,long K,int N,group g[])
{
int iitrg;
long amount=0;
//PREPROCESSING OF GROUPS
for(iitrg=1;iitrg<=N;iitrg++)
{
g[iitrg].displacement=0;
g[iitrg].sum=g[iitrg].lnomem;
}

for(iitrg=1;iitrg<=N;iitrg++)
{
int index=iitrg+1;

if(index==N+1)
index=1;


while(g[iitrg].sum+g[index].lnomem <=K && index!=iitrg )
{
g[iitrg].sum+=g[index].lnomem ;
g[iitrg].displacement++;
index++;

if(index==N+1)
index=1;
}
//cout<<"\n"<<g[iitrg].sum<<" "<<g[iitrg].displacement;

}

//END OF PREPROCESSING
int pos=1;
for(long iitrR=1;iitrR<=R;iitrR++)
{

amount+=g[pos].sum;
pos+=g[pos].displacement+1;

if(pos>N)
pos=pos-N;
//else if(pos==N)
//{
//pos=1;
//}
//cout<<"\npos="<<pos;


}
//cout<<"amount"<<amount;
return amount;
}



void main()
{
int inocase=0;
long ioutput[51];
long R,K;
int N;
ifstream in;
in.open("input.in");
clrscr();
in>>inocase;
//cout<<"\n"<<inocase;
//getch();

//return;

for(int iitrnocase=1;iitrnocase<=inocase;iitrnocase++)
{
in>>R>>K>>N;
//cout<<"\n"<<R<<" "<<K<<" "<<N;
//getch();
group g[20];
for(int iitrnoN=1;iitrnoN<=N;iitrnoN++)
{
in>>g[iitrnoN].lnomem;
//cout<<"\n"<<g[iitrnoN].lnomem;
}

ioutput[iitrnocase]=evaluate(R,K,N,g);
cout<<"\n CASE "<<iitrnocase<<"#: "<<ioutput[iitrnocase];

//getch();
}
ofstream out;
out.open("output.txt");
for( iitrnocase=1;iitrnocase<=inocase;iitrnocase++)
out<<"Case #"<<iitrnocase<<": "<<ioutput[iitrnocase]<<"\n";
out.close();
in.close();
getch();
}

