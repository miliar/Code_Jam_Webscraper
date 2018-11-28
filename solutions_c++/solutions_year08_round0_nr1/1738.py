#include <fstream.h>
#include <string.h>

int main()
{
	fstream fin("in.txt",ios::in);
	int N,S,Q;
	fin>>N;
	long result=0;
	char name[100][100];
	char temp[100];
	int income[1000];
	int* a=0;
	int i,j,k;
	int pre=-1;
	int sum=0;
	fstream fout("out.txt",ios::out);
	for(i=0;i<N;i++)
	{
		fin>>S;
		fin.getline(temp,100);
		for(j=0;j<S;j++)
		fin.getline(name[j],100);
		fin>>Q;
		fin.getline(temp,100);
		for(j=0;j<Q;j++)
		{
		   fin.getline(temp,100);
		   for(k=0;k<S;k++)
		   {
			if (strcmp(temp,name[k])==0)
			{
				income[j]=k;
				break;
			}
		   }

		}
		pre = -1;
		sum=0;
		result=0;
		a=new(int[S]);
		for(j=0;j<S;j++) a[j]=0;
		for(j=0;j<Q;j++)
		{
			if (a[income[j]]==0)
			{
				a[income[j]]=1;
				sum++;
				if (sum==S)
					{
						result++;
						pre=income[j];
						for(k=0;k<S;k++)
						a[k]=0;
						a[pre]=1;
						sum=1;
					}
			}
		}
		delete [] a;
		a=0;
		fout<<"case#"<<i+1<<": "<<result<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}