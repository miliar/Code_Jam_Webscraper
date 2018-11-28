#include<stdio.h>
#include<string.h>
#include<string>
#include<map>
#include<vector>
#include<algorithm>

#define fu(i,n) for(int i = 0; (i) < (n); i++)
#define MSET(A, x) memset(A, x, sizeof(A))
#define MAX 128

using namespace std;

int T,H,W; //height and width
int mapa[MAX][MAX];
char labels[MAX][MAX];

char AchaLabel(int linha, int coluna, char c)
{
	vector< pair<int,int> > numerosAdj;
	if(labels[linha][coluna] != ' ')
	{
		return labels[linha][coluna];
	}
	//North, West, East, South
	int incrementos[] = {-1,0,0,-1,0,1,1,0};
	if(linha > 0)
	{
		numerosAdj.push_back(make_pair(mapa[linha-1][coluna],0));
	}
	if(coluna > 0)
	{
		numerosAdj.push_back(make_pair(mapa[linha][coluna-1],1));
	}
	if(coluna < W-1)
	{
		numerosAdj.push_back(make_pair(mapa[linha][coluna+1],2));
	}
	if(linha < H-1)
	{
		numerosAdj.push_back(make_pair(mapa[linha+1][coluna],3));
	}
	//sink
	if(numerosAdj.size() == 0)
	{
		labels[linha][coluna] = c;
		return c;
	}
	sort(numerosAdj.begin(),numerosAdj.end());
	//sink
	if(numerosAdj[0].first >= mapa[linha][coluna])
	{
		labels[linha][coluna] = c;
		return c;
	}
	int index = 2*numerosAdj[0].second;
	c = AchaLabel(linha + incrementos[index],coluna + incrementos[index+1],c);
	labels[linha][coluna] = c;
	return c;
}

void limpa()
{
	MSET(mapa,0);
	MSET(labels,0);
}

int main()
{
	scanf("%d",&T);
	fu(k,T)
	{
		scanf("%d %d",&H,&W);
		for(int linha = 0; linha < H; linha++)
		{
			for(int coluna = 0; coluna < W; coluna++)
			{
				int num;
				scanf(" %d",&num);
				mapa[linha][coluna] = num;
				labels[linha][coluna] = ' ';
			}
		}
		char c = 'a';
		for(int linha = 0; linha < H; linha++)
		{
			for(int coluna = 0; coluna < W; coluna++)
			{
				if(labels[linha][coluna] == ' ')
				{
					char c2 = AchaLabel(linha,coluna,c);
					if(c2 == c)
					{
						c++;
					}
				}
			}
		}
		printf("Case #%d:\n",k+1);
		for(int linha = 0; linha < H; linha++)
		{
			for(int coluna = 0; coluna < W; coluna++)
			{
				if(coluna == 0)
				{
					printf("%c",labels[linha][coluna]);
				}
				else
				{
					printf(" %c",labels[linha][coluna]);
				}
			}
			printf("\n");
		}
	}
	return 0;
}
