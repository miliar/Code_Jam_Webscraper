#include <fstream>
#include <iostream>

using namespace std;

char ** t;

ifstream fin("A-small-attempt0.in");
ofstream fout("out.txt");
int * a, *b;
void solve()
{
	for (int i=0;i<4;i++)
		fin>>t[i];
	for (int i=0;i<10;i++)
		a[i]=b[i]=0;
	bool f=false,s=false,end=true;
	char p;
	bool z1,z2;
	for (int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			p = t[i][j];
			z1 = (p == 'X') || (p == 'T');
			z2 = (p == 'O') || (p == 'T');
			a[i] += z1;
			a[j+4] += z1;
			b[i] += z2;
			b[j+4] += z2;
			if ( p=='.' )
				end = false;
		}
	for (int i=0;i<4;i++)
	{
		p = t[i][i];
		z1 = (p == 'X') || (p == 'T');
		z2 = (p == 'O') || (p == 'T');
		a[8] += z1;
		b[8] += z2;
		p = t[3-i][i];
		z1 = (p == 'X') || (p == 'T');
		z2 = (p == 'O') || (p == 'T');
		a[9] += z1;
		b[9] += z2;
	}
	for (int i=0;i<10;i++)
	{
		cout<<a[i]<<" "<<b[i]<<"\n";
		if (a[i]>=4)
			f = true;
		if (b[i]>=4)
			s = true;
	}
	if (f||s)
		end = true;
	if (!end)
		fout<<"Game has not completed";
	else
		if (!f && !s)
			fout<<"Draw";
		else
			if (f)
				fout<<"X won";
			else
				fout<<"O won";
}

int main()
{
	t = new char * [4];
	for (int i=0;i<4;i++)
		t[i] = new char [4];
	a = new int[10];
	b = new int[10];
	int f;
	fin>>f;
	for (int i=0;i<f;i++)
	{
		fout<<"Case #"<<i+1<<": ";
		solve();			
		if (i!=f-1)
			fout<<"\n";
	}
	fout.close();
	return 0;	
}
