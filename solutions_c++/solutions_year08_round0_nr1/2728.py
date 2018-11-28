#include <fstream>
#include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
int i,j,n,m,k;
string Q[120],S[20];
int F[120][20];

int f(int x,int y)
{
	int i,t;
	if (x==k) return 0;

	if (F[x][y]!=-1) return F[x][y];

	if (Q[x]==S[y]) 
	{
		t=200;
		for (i=0;i<m;i++) 
			if (f(x+1,i)+1<t)
				if (Q[x]!=S[i])
					t = f(x+1,i)+1;
	}
	else t = f(x+1,y);

	F[x][y]=t;
	return t;
}

int main()
{
	char temp[1024];
	fin>>n;
	for (i=1;i<=n;i++)
	{
		int t=200;
		fin>>m;
		fin.getline(temp,1024,0x0a);
		for (j=0;j<m;j++) 
		{
			fin.getline(temp,1024,0x0a);
			S[j]=temp;
		}
		fin>>k;		
		fin.getline(temp,1024,0x0a);
		for (j=0;j<k;j++) 
		{
			fin.getline(temp,1024,0x0a);
			Q[j]=temp;
		}
		memset(F,0xFF,sizeof(F));
		for (j=0;j<m;j++) 
			if (t>f(0,j))
				t = f(0,j);
		fout<<"Case #"<<i<<": "<<t;
		if (i!=n) fout<<endl;
	}

	return 0;
}