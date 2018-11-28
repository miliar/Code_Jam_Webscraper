#include <fstream>

using namespace std;

char ** t;

ifstream fin("A-small-attempt0.in");
ofstream fout("out.txt");
void solve()
{
	for (int i=0;i<4;i++)
		fin>>t[i];
	bool f=false,s=false,end=true;
	int xs,os;
	for (int i=0;i<4;i++)
	{
		xs=0;
		os=0;
		for (int j=0;j<4;j++)
		{
			char p = t[i][j];
			xs+=(p=='X') + (p=='T');
			os+=(p=='O') + (p=='T');
			if (p == '.')
				end = false;
		}
		if (xs == 4)
			f = true;
		if (os == 4)
			s = true;
	}
	
	for (int i=0;i<4;i++)
	{
		xs=0;
		os=0;
		for (int j=0;j<4;j++)
		{
			char p = t[j][i];
			xs+=(p=='X') + (p=='T');
			os+=(p=='O') + (p=='T');
		}
		if (xs == 4)
			f = true;
		if (os == 4)
			s = true;
	}
	
	char p;
	
	xs=0;
	os=0;
	for (int j=0;j<4;j++)
	{
		p = t[j][j];
		xs+=(p=='X') + (p=='T');
		os+=(p=='O') + (p=='T');
	}
	if (xs == 4)
		f = true;
	if (os == 4)
		s = true;
	
	xs=0;
	os=0;
	for (int j=0;j<4;j++)
	{
		p = t[3-j][j];
		xs+=(p=='X') + (p=='T');
		os+=(p=='O') + (p=='T');
	}
	if (xs == 4)
		f = true;
	if (os == 4)
		s = true;
	
	
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
	int f;
	fin>>f;
	for (int i=0;i<f;i++)
	{
		fout<<"Case #"<<i+1<<": ";
		solve();			
		if (i!=f-1)
			fout<<endl;
	}
}
