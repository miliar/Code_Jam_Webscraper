#include <fstream.h>
#include <conio.h>
void sort (long* a,int n)
{
int i,ing=1;
long temp;
do
	{
	ing =1;
	for(i=0;i<n-1;i++)
	if (a[i]<a[i+1])
	{
		ing=0;
		temp=a[i];
		a[i]=a[i+1];
		a[i+1]=temp;
	}
	}
while (ing==0);


}
int main()

{
	clrscr();
	fstream fin("in.txt",ios::in);
	fstream fout("out.txt",ios::out);
	int N,P,K,L;
	fin>>N;
	int i,j,k;
	long t;
	long a[1000];
	unsigned long result;
	for (k=0;k<N;k++)
	{
		result=0;
		fin>>P>>K>>L;
		for(i=0;i<L;i++)
		fin>>a[i];
		sort (a,L);
		for(i=0;i<L;i++)
		result+=(i/K+1)*a[i];
		fout<<"Case #"<<k+1<<": "<<result<<endl;
	}

	fin.close();
	fout.close();
	cout<<"ended";
	getch();
	return 0;
}