#include <stdio.h>
#include <memory.h>

//using namespace std;

bool fn(char a[50][50],int n,int k,char c)
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n-k+1;j++)
		{
			for(int l=0;l<k;l++)
			{
				if(a[i][j+l]!=c)
					goto j1;
			}
			return true;
j1:
			for(int l=0;l<k;l++)
			{
				if(a[j+l][i]!=c)
					goto j2;
			}
				return true;
j2:;
		}
	}

	for(int i=0;i<n-k+1;i++)
		for(int j=0;j<n-k+1;j++)
		{
			for(int l=0;l<k;l++)
			{
				if(a[i+l][j+l]!=c)
					goto j3;
			}
				return true;
j3:;
		}

	for(int i=k-1;i<n;i++)
		for(int j=0;j<n-k+1;j++)
		{
			for(int l=0;l<k;l++)
			{
				if(a[i-l][j+l]!=c)
					goto j4;
			}
				return true;
j4:;
		}

	return false;
}

int main(int argc, char **argv)
{
	if(argc!=2)
	{
		printf("Usage: <prog> <input_file>\n");
		return 1;
	}

	FILE *fin = fopen("a.in","r");
	FILE *fout = fopen("a.out","w");
		
	int cnt;
	fscanf(fin,"%d",&cnt);
	for(int i=0;i<cnt;i++)
	{
		int n,k;
		fscanf(fin,"%d %d",&n,&k);
		char a[50][50];
		char b[50][50];
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));

		for(int j=0;j<n;j++)
		{
			char tmp[51]="";
			fscanf(fin,"%s",tmp);
			for(int k=0;k<n;k++)
			{
				a[j][k]=tmp[k];
			}
		}

		for(int j=0;j<n;j++)
		{
			int l=n-1;
			for(int k=n-1;k>=0;k--)
			{
				if(a[j][k]!='.')
					b[l--][n-1-j]=a[j][k];
			}
		}

		bool r=fn(b,n,k,'R');
		bool bl=fn(b,n,k,'B');

		if(r && bl)		
			fprintf(fout,"Case #%d: Both\n",i+1);
		else if(r)
			fprintf(fout,"Case #%d: Red\n",i+1);
		else if(bl)
			fprintf(fout,"Case #%d: Blue\n",i+1);
		else
			fprintf(fout,"Case #%d: Neither\n",i+1);
	}
	fclose(fin);
	fclose(fout);
}
