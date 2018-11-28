#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;

int tab[100][100];
int h,w;

int minat(int j, int k)
{
	int minv=1000000;
	int minj=0;
	int mink=0;
	if(j>0 && tab[j-1][k]<minv)
	{
		minv=tab[j-1][k];
		minj=j-1;
		mink=k;
	}
	if(k>0 && tab[j][k-1]<minv)
	{
		minv=tab[j][k-1];
		minj=j;
		mink=k-1;
	}
	if(k<(w-1) && tab[j][k+1]<minv)
	{
		minv=tab[j][k+1];
		minj=j;
		mink=k+1;
	}
	if(j<(h-1) && tab[j+1][k]<minv)
	{
		minv=tab[j+1][k];
		minj=j+1;
		mink=k;
	}
	return (minv*10000+minj*100+mink);
}

int main(int argc, char *argv[])
{
	fstream fin;
	fstream fout;
	fin.open("b.in");
	fout.open("b.out", ios_base::app);
	//
    int t;
	fin >> t;

    for(int i=0; i<t; i++)
    {
		fin >> h;
		fin >> w;
		char res[100][100];
		//int vis[100][100];
		string names="abcdefghijklmnopqrstuvwxyz";
		int free=0;
		for(int j=0; j<h; j++)
		{
			for(int k=0; k<w; k++)
			{
				fin >> tab[j][k];
				//vis[j][k]=0;
				res[j][k]='#';
			}
		}
		for(int j=0; j<h; j++)
		{
			for(int k=0; k<w; k++)
			{
				if(res[j][k]=='#')
				{
					queue <int> q;
					res[j][k]=names[free];
					free++;
					q.push(100*j+k);
					while(!q.empty())
					{
						int x=q.front()%100;
						int y=q.front()/100;
						q.pop();
						int minv;
						int minj;
						int mink;
						int val=minat(y,x);
						mink=val%100;
						val/=100;
						minj=val%100;
						minv=val/100;
						//fout << x << " " << y << " " << minv << " " << minj << " " << mink << endl;
						if(minv<tab[y][x] && res[minj][mink]=='#')
						{
							res[minj][mink]=res[y][x];
							q.push(100*minj+mink);
						}
						//
						if(y>0)
						{
							val=minat(y-1,x);
							mink=val%100;
							val/=100;
							minj=val%100;
							minv=val/100;
							if(minv<tab[y-1][x] && minj==y && mink==x && res[y-1][x]=='#')
							{
								res[y-1][x]=res[y][x];
								q.push(100*(y-1)+x);
							}
						}
						if(x>0)
						{
							val=minat(y,x-1);
							mink=val%100;
							val/=100;
							minj=val%100;
							minv=val/100;
							if(minv<tab[y][x-1] && minj==y && mink==x && res[y][x-1]=='#')
							{
								res[y][x-1]=res[y][x];
								q.push(100*(y)+x-1);
							}
						}
						if(x<(w-1))
						{
							val=minat(y,x+1);
							mink=val%100;
							val/=100;
							minj=val%100;
							minv=val/100;
							if(minv<tab[y][x+1] && minj==y && mink==x && res[y][x+1]=='#')
							{
								res[y][x+1]=res[y][x];
								q.push(100*(y)+x+1);
							}
						}
						if(y<(h-1))
						{
							val=minat(y+1,x);
							mink=val%100;
							val/=100;
							minj=val%100;
							minv=val/100;
							if(minv<tab[y+1][x] && minj==y && mink==x && res[y+1][x]=='#')
							{
								res[y+1][x]=res[y][x];
								q.push(100*(y+1)+x);
							}
						}
					}
				}
			}
		}
		fout << "Case #" << i+1 << ":" << endl;
		for(int j=0; j<h; j++)
		{
			for(int k=0; k<w; k++)
			{
				fout << res[j][k];
				if(k!=(w-1)) fout << " ";
				else fout << endl;
			}
		}
    }
	//
    fin.close();
	fout.close();
    return 0;
}
