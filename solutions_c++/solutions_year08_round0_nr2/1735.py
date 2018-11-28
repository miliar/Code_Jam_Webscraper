#include <fstream.h>

void sort(int* a,int n)
{
	int i,j,temp,ing;
	ing=1;
	do
	{
		ing=0;
		for(i=0;i<n-1;i++)
		if (a[i]>a[i+1])
		{
			ing=1;
			temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;
			temp=a[200+i];
			a[i+200]=a[200+i+1];
			a[200+i+1]=temp;
			temp=a[400+i];
			a[400+i]=a[400+i+1];
			a[400+i+1]=temp;
		}
		for(i=0;i<n-1;i++)
		if (a[i]==a[i+1] && a[200+i]>a[201+i])
		{
			ing=1;
			temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;
			temp=a[200+i];
			a[i+200]=a[200+i+1];
			a[200+i+1]=temp;
			temp=a[400+i];
			a[400+i]=a[400+i+1];
			a[400+i+1]=temp;
		}
	}
	while (ing==1);

}


int main()
{
	fstream fin("in.txt",ios::in);
	fstream fout("out.txt",ios::out);
	int N, NA, NB, T;
	int a[3][200];
	char s[13];
        int n;
	fin>>N;
	for(n=0;n<N;n++)
	{
		fin>>T;
		fin>>NA>>NB;
		int i,j,k;
		for(i=0;i<NA;i++)
		{
			fin>>s;
			a[0][i]=60*((int(s[0])-48)*10+int(s[1])-48)+
			10*(int(s[3])-48)+int(s[4])-48;
			fin>>s;
			a[1][i]=60*((int(s[0])-48)*10+int(s[1])-48)+
			10*(int(s[3])-48)+int(s[4])-48;
			a[2][i]=1;

		}
		for(i=NA;i<NA+NB;i++)
		{
			fin>>s;
			a[0][i]=60*((int(s[0])-48)*10+int(s[1])-48)+
			10*(int(s[3])-48)+int(s[4])-48;
			fin>>s;
			a[1][i]=60*((int(s[0])-48)*10+int(s[1])-48)+
			10*(int(s[3])-48)+int(s[4])-48;
			a[2][i]=2;

		}
		sort(&a[0][0],NA+NB);
		int ing;
		int temp[2];
		int result=0;
		int res[2]={0};
		int p[2][200];
		for (i=0;i<NA+NB;i++)
		{
			ing=0;
			for(j=0;j<result;j++)
			{
				if (p[1][j]==a[2][i] && p[0][j]<=a[0][i])
				{
					ing=1;
					p[1][j]=3-p[1][j];
					p[0][j]=a[1][i]+T;
					for(k=j+1;k<result;k++)
					{
						if (p[0][k]<p[0][k-1])
						temp[0]=p[0][k-1];
						temp[1]=p[1][k-1];
						p[0][k-1]=p[0][k];
						p[1][k-1]=p[1][k];
						p[0][k]=temp[0];
						p[1][k]=temp[1];
					}
					ing=1;
					break;
				}
			}
			if (ing==0)
			{
				p[0][result]=a[1][i]+T;
				p[1][result]=3-a[2][i];
				res[2-p[1][result]]++;
				for(k=result;k>0;k--)
				{
					if (p[0][k]<p[0][k-1])
					{
						temp[0]=p[0][k-1];
						temp[1]=p[1][k-1];
						p[0][k-1]=p[0][k];
						p[1][k-1]=p[1][k];
						p[0][k]=temp[0];
						p[1][k]=temp[1];
					}
				}
				result++;
			}


		}
	fout<<"Case #"<<n+1<<": "<<res[0]<<" "<<res[1]<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}