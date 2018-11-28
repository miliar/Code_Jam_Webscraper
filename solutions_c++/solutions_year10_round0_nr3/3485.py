#include<iostream>
#include<conio.h>
using namespace std;

class Roller
{
private:
	FILE *fin,*fout;
public:
	Roller(char file[])
	{
		if((fin=fopen(file,"r"))==NULL) exit(0);
		if((fout=fopen("output.txt","w"))==NULL) exit(0);
	}
	void ride()
	{
		int n=0;
		fscanf(fin,"%d",&n);
		for(int i=1;i<=n;i++)
		{
			long run=0,k=0;
			int nog=0;
			fscanf(fin,"%d",&run);
			fscanf(fin,"%d",&k);
			fscanf(fin,"%d",&nog);
			long *a=new long[nog];
			for(int j=0;j<nog;j++) fscanf(fin,"%d",&a[j]);

			long amount=0;
			for(int r=0;r<run;r++)
			{
				int temp=0;
				long people=0;
				for(int m=0;m<nog;m++)
				{
					people+=a[m];
					if(people>k)
					{
						temp=m;
						people-=a[m];
						break;
					}
				}
				amount+=people;
				long *b=new long[temp];
				for(int m=0;m<temp;m++) b[m]=a[m];
				for(int m=temp;m<nog;m++) a[m-temp]=a[m];
				for(int m=0;m<temp;m++) a[nog-temp+m]=b[m];
			}
			fprintf(fout,"Case #%d: %d\n",i,amount);
		}
	}
};
void main()
{
	char file[10];
	cout<<"Enter the file name : ";
	cin>>file;
	Roller obj(file);
	obj.ride();
}