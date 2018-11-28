#include<iostream>
#include<map>
#include<string>
#include<fstream>
using namespace std;


int H,W;

int mmp[110][110];
int number[110][110];

int node[11010];

void init(int s){
	for(int i=1;i<=s;i++)
		node[i]=i;
}
int get_parent(int u){
	if(u!=node[u])
		node[u]=get_parent(node[u]);
	return node[u];
}
void union_set(int u,int v){
	if(get_parent(u) != get_parent(v) )
		node[node[u]] = node[v];
}

int main()
{
	
	ifstream fcin("B-small.in");
	ofstream fcout("B-small");

	int num,cases = 1;
	fcin>>num;
	int i,j,k;

	for(cases = 1; cases <=num; cases++)
	{
		fcin>>H>>W;
		for(i=0;i<H;i++)
		{
			for(j=0;j<W;j++)
			{
				fcin>>mmp[i][j];
				number[i][j]=i*W+j+1;
			}
		}

		for(i=1;i<=number[H-1][W-1];i++)
		{
			node[i]=i;
		}

		int min = 999999999; int posi = -1;
		for(i=0;i<H;i++)
		{
			for(j=0;j<W;j++)
			{
				min = mmp[i][j];  posi = -1;
				if(i>0 && mmp[i-1][j] < min) {min=mmp[i-1][j];posi=1;}
				if(j>0 && mmp[i][j-1] < min) {min=mmp[i][j-1];posi=3;}
				if(j<W-1 && mmp[i][j+1] < min) {min=mmp[i][j+1];posi=4;}
				if(i<H-1 && mmp[i+1][j] < min) {min=mmp[i+1][j];posi=2;}


				if(posi==1)
				{
					union_set(number[i-1][j],number[i][j]);
				}
				else if(posi==2)
				{
					union_set(number[i+1][j],number[i][j]);
				}
				else if(posi ==3)
				{				
					union_set(number[i][j-1],number[i][j]);
				}
				else if(posi==4)
				{				
					union_set(number[i][j+1],number[i][j]);
				}
			}

			
		}

		for(i=1;i<10;i++)
			cout<<get_parent(node[i])<<endl;

		char ch[11000];
		memset(ch,0,sizeof(ch));
		char start = 'a';

		char res[110][110];
		memset(res,0,sizeof(res));
		for(i=0;i<H;i++)
		{
			for(j=0;j<W;j++)
			{
				if( ch[ get_parent(node[i*W+j+1]) ] >0 )
				{
					res[i][j]=ch[ get_parent(node[i*W+j+1]) ];
				}
				else
				{
					ch[ get_parent(node[i*W+j+1]) ] = start;
					start++;
				}
			}
		}

		fcout<<"Case #"<<cases<<":"<<endl;
		for(i=0;i<H;i++)
		{
			for(j=0;j<W-1;j++)
			{
				fcout<<ch[ get_parent(node[i*W+j+1]) ]<<' ';
			}
			fcout<<ch[ get_parent(node[i*W+j+1]) ]<<endl;
		}
	}


	return 0;
}