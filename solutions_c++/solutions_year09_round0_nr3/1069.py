#include <fstream>

using namespace std;
char s[500]={};
string sent;
int main()
{
	ifstream fin("inputlarge.in");
	ofstream fout("output.txt");
	sent="welcome to code jam";
	char un[10];
	int n;
	fin >> n;
	fin.getline(un,10);
	for(int cases=0;cases<n;cases++)
	{
		fin.getline(s,510);
		int a[20][510]={0};
		int i=0;
		int prec=0;
		while(s[i]!=0)
		{
			if (s[i]=='m')
			{
				a[0][i]=1;
				prec++;
			}
			i++;
		}
		int k=1;
		int j=sent.length()-2;
		for(;j>=0;j--)
		{
			char now=sent[j];
			int temp=0;
			for(int l=0;l<i;l++)
			{
				prec=prec-a[k-1][l];
			if (prec<0)
					prec=prec+10000;
				if (s[l]==now)
				{
					a[k][l]=prec;
					temp=temp+a[k][l];
					temp%=10000;
				}
			}
			prec=temp;
			k++;
		}
		fout <<	"Case #" << cases+1 <<": ";
			if (prec<1000)
				fout << "0";
			if (prec<100)
				fout << "0";
			if (prec<10)
				fout << "0";
		fout << prec <<"\n";

	}
	return 0;
}