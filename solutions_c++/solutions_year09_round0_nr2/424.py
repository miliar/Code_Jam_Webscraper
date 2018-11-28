#include<iostream>
#include<map>
using namespace std;

int alt[100][100];
int group[100][100];

int N, W, H;

void getrowcol(int i, int j, int &i1, int &j1)
{
	int newalt = alt[i][j];
	i1=i;
	j1=j;
	if(i-1 >= 0 && alt[i-1][j]<newalt)
	{
		newalt=alt[i-1][j];
		i1=i-1;
		j1=j;
	}
	if(j-1 >= 0 && alt[i][j-1]<newalt)
	{
		newalt=alt[i][j-1];
		i1=i;
		j1=j-1;
	}
	if(j+1 < W && alt[i][j+1]<newalt)
	{
		newalt=alt[i][j+1];
		i1=i;
		j1=j+1;
	}
	if(i+1 < H && alt[i+1][j]<newalt)
	{
		newalt=alt[i+1][j];
		i1=i+1;
		j1=j;
	}
}
	
int main()
{
	int i,j;
	
	cin>>N;

	for(int c=1; c<=N; c++)
	{
		cin>>H>>W;

		for(i=0; i<H; i++)
			for(j=0; j<W; j++)
			{
				cin>>alt[i][j];
				group[i][j]=i*W + j;
			}

		bool changed = true;
		while(changed)
		{

			changed=false;
			for(i=0; i<H; i++)
				for(j=0; j<W; j++)
				{
					int i1,j1;
					getrowcol(i, j, i1, j1);

					if(group[i][j]!=group[i1][j1])
					{
						group[i][j]=group[i1][j1];
						changed=true;
					}
				}
		}

		char minchar = 'a';
		map<int, char> conv;
		cout<<"Case #"<<c<<":\n";

		for(i=0; i<H; i++)
			for(j=0; j<W; j++)
			{

				map<int,char>::iterator iter = conv.find(group[i][j]);
				if(iter==conv.end())
				{
					conv[group[i][j]]=minchar;
					cout<<minchar;
					minchar++;
				}

				else
				{
					cout<<iter->second;
				}
				if(j != W-1 )
					cout<<' ';
				else
					cout<<endl;
			}
	}
}







