#include<fstream>
using namespace std;

int t,h,w,i,j;
int fang[100][100];
int zuo[10000];
char zhong[10000];
void main()
{
		ifstream inf;
    inf.open("B-small-attempt4.in");

    ofstream outf;
    outf.open("out.txt");
	inf>>t;
	for(int z=0;z<t;z++)
	{
		inf>>h>>w;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				inf>>fang[i][j];
			}
		}
		for(i=0;i<h*w;i++)zuo[i]=i;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				int low=fang[i][j],tent=i*w+j;
				if((i-1)>=0)
				{
					if(fang[i-1][j]<fang[i][j]){low=fang[i-1][j];tent=(i-1)*w+j;}
				}
				if((j-1)>=0)
				{
					if(fang[i][j-1]<fang[i][j]&&fang[i][j-1]<low){low=fang[i][j-1];tent=i*w+j-1;}
				}
				if((j+1)<w)
				{
					if(fang[i][j+1]<fang[i][j]&&fang[i][j+1]<low){low=fang[i][j+1];tent=i*w+j+1;}
				}
				if((i+1)<h)
				{
					if(fang[i+1][j]<fang[i][j]&&fang[i+1][j]<low){low=fang[i+1][j];tent=(i+1)*w+j;}
				}
				zuo[i*w+j]=tent;
			}
		}
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				zhong[i*w+j]='\0';
			}
		}
		char mu='a'-1;
		for(i=0;i<h*w;i++)
		{
			if(zhong[i]!='\0')continue;
			int guo=i;
			while(zuo[guo]!=guo&&zhong[guo]=='\0')
			{
				guo=zuo[guo];	
			}
			int temp=i;
			if(zhong[guo]!='\0')
			{
				while(temp!=guo)
				{
					zhong[temp]=zhong[guo];temp=zuo[temp];
				}
			}
			else
			{
				mu++;
				while(temp!=guo)
				{
					zhong[temp]=mu;temp=zuo[temp];
				}
				zhong[guo]=mu;
			}
		}
		outf<<"Case #"<<z+1<<':'<<endl;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				outf<<zhong[i*w+j]<<' ';
			}
			outf<<endl;
		}
	}
}