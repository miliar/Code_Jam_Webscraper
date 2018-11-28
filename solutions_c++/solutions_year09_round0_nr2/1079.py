#include <fstream>
#include <vector>

using namespace std;
typedef struct
{
	int x,y;
}point;

vector <point> v;
int a[100][100]={0};
int cases,nr,n,m;
void start(int x,int y)
{
	point p;
	int min=10000;
	p.x=x;
	p.y=y;
	v.push_back(p);
	if((x>0)&&(a[x-1][y]<min))
	{
		min=a[x-1][y];
		p.x=x-1;
		p.y=y;
	}
	if((y>0)&&(a[x][y-1]<min))
	{
		min=a[x][y-1];
		p.x=x;
		p.y=y-1;
	}
	if((y<n-1)&&(a[x][y+1]<min))
	{
		min=a[x][y+1];
		p.x=x;
		p.y=y+1;
	}
	if((x<m-1)&&(a[x+1][y]<min))
	{
		min=a[x+1][y];
		p.x=x+1;
		p.y=y;
	}
	if (min<a[x][y])
		start(p.x,p.y);
}
int main()
{
	ifstream fin("inputlarge.in");
	ofstream fout("output.txt");
	fin >> nr;
	for(cases=0;cases<nr;cases++)
	{
		char letter='a';
		letter--;
		fin >> m >> n;
		char c[100][100]={};
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
				fin >> a[i][j];
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
			{
				if (c[i][j]==0)
				{
					v.clear();
					start(i,j);
					int size=v.size()-1;
					char cur;
					if (c[v[size].x][v[size].y]==0)
						{
							letter++;
							cur=letter;
						}else cur=c[v[size].x][v[size].y];
					for(int k=0;k<=size;k++)
						c[v[k].x][v[k].y]=cur;
				}
			}
			fout << "Case #" << cases+1 << ":" <<"\n";
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n-1;j++)
				fout << c[i][j] << " ";
			fout << c[i][n-1];
			fout << '\n';
		}
	}
	return 0;
}