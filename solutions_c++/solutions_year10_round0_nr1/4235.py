#include<iostream>
#include<conio.h>
using namespace std;

class Snapper
{
private:
	FILE *fin,*fout;
public:
	Snapper(char file[])
	{
		if((fin=fopen(file,"r"))==NULL) exit(0);
		if((fout=fopen("output.txt","w"))==NULL) exit(0);
	}
	void light()
	{
		int T=0;
		fscanf(fin,"%d",&T);
		for(int i=1;i<=T;i++)
		{
			long N=0,K=0;
			fscanf(fin,"%d",&N);
			fscanf(fin,"%d",&K);
			bool a[30];
			for(int j=0;j<N;j++) a[j]=false;
			for(int j=0;j<K;j++)
			{
				for(int h=0;h<N;h++)
				{
					if(a[h]) a[h]=false;
					else
					{
						a[h]=true;
						break;
					}
				}
			}
			bool flag=false;
			for(int j=0;j<N;j++)
			{
				if(a[j]) flag=true;
				else
				{
					flag=false;
					break;
				}
			}
			if(flag) fprintf(fout,"Case #%d: ON\n",i);
			else fprintf(fout,"Case #%d: OFF\n",i);
		}
	}
	~Snapper()
	{
		fclose(fin);
		fclose(fout);
	}
};
void main()
{
	char file[10];
	cout<<"Enter the file name : ";
	cin>>file;
	Snapper obj(file);
	obj.light();
}