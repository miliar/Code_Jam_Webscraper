#include<iostream.h>
#include<fstream.h>
#include<conio.h>


int main()

{

fstream in, ou;
int binarr[1000][20],chkarr[20];;
long t,i,j,n,k;
long arr[1000];
clrscr();

in.open("large.in",ios::in);

if(!in)
{
cout<<"input error";
}
ou.open("C-large.out",ios::out);
if(!ou)
{
cout<<"ouput error";
}
in>>t;
for(int s=0;s<t;s++)
{
	long output=0,min=1000000;
	int b;
	in>>n;
	b=1;
		for(j=0;j<20;j++)
		chkarr[j]=0;

		for(i=0;i<n;i++)
		for(j=0;j<20;j++)
		binarr[i][j]=0;
		ou<<"Case #"<<s+1<<": ";
		for(j=0;j<n;j++)
		{
		in>>arr[j];
		}

		for(j=0;j<n;j++)
		{
		k= arr[j];
		int l=0;
			while(k>0)
			{
			binarr[j][l]=k%2;
			k=k/2;
			l++;
			}
		}

		for(i=0;i<20;i++)
		{
			for(j=0;j<n;j++)
			chkarr[i]=chkarr[i]+binarr[j][i];
		}

		for(j=0;j<20;j++)
		{

		chkarr[j]=chkarr[j]%2;
		if(chkarr[j]!=0)
		{	ou<<"NO";
			ou<<endl;
			b=0;
		break;
		}

		}


		if(b==1)
		{
		for(j=0;j<n;j++)
		{
			if(arr[j]<min)
			{
			min=arr[j];
			i=j;
			}
		}


		for(j=0;j<n;j++)
		{
		if(j!=i)
		{
		output=output+arr[j];

		}
		}
		ou<<output<<endl;
		}
}

ou.close();
in.close();
return 0;




}