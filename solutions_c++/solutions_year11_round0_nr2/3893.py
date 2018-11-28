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
int C;
input>>C;
char **com=new char*[C];
for(int j=0;j<C;j++)
{
	com[j]=new char[3];
	for(int k=0;k<3;k++)
	{
		input>>com[j][k];
	}
}


int D;
input>>D;
char **clear=new char*[D];
for(j=0;j<D;j++)
{
	clear[j]=new char[D];
	for(int k=0;k<2;k++)
	{
		input>>clear[j][k];
	}
}


int N;
input>>N;
char *out=new char[N];
int k=-1;
for(j=0;j<N;j++)
{
   char ch;
   input>>ch;
   k++;
   if(k==0)
   {
   out[k]=ch;

   }
   else
   {
   out[k]=ch;
   for(int jj=0;jj<C;jj++)
   {
	if(out[k-1]==com[jj][0]&&out[k]==com[jj][1]||out[k-1]==com[jj][1]&&out[k]==com[jj][0])
	{
	out[k-1]=com[jj][2];
	k--;
	break;
	}
   }
   for(jj=0;jj<D;jj++)
   {
	for(int kk=0;kk<=k;kk++)
	{
		if(out[kk]==clear[jj][1])
		{
			for(int ll=0;ll<=k;ll++)
			{
			     if(out[ll]==clear[jj][0])
			     {
				k=-1;
				break;

			     }
			}

		}
	}
       //	break;
   }

   }


}
output<<"Case #"<<i+1<<": [";
for(int l=0;l<k;l++)
{
output<<out[l]<<", ";
}
if(k!=-1)
output<<out[k];
output<<"]"<<endl;
}






 }