#include<stdio.h>
#include<string.h>
#include<string>
#include<map>
#include<vector>
#include<algorithm>

#define fu(i,n) for(int i = 0; (i) < (n); i++)
#define MSET(A, x) memset(A, x, sizeof(A))

using namespace std;

vector<string> linguagem;
vector<char> possibilidades[32];
vector<string> palavras;
int L,D,N;


void limpa()
{
	fu(i,L)
	{
		possibilidades[i].clear();
	}
	palavras.clear();
}

void GeraPalavra(int letraAtual)
{
	if(letraAtual >= L) return;
	int tamIni = (int)palavras.size();
	for(int index = 0; index < tamIni; index++)
	{
		string palavra = palavras[index];
		if(palavra == "") continue;
	//printf("palavra analizada: %s ",palavra.c_str());
		bool entra = false;
		fu(i,(int)possibilidades[letraAtual].size())
		{
			char c = possibilidades[letraAtual][i];
	//printf("Compara %c com %c\n",c,palavra[letraAtual]);
			if((char)palavra[letraAtual] == c)
			{
				entra = true;
				break;
			}
		}
		if(!entra) palavras[index] = "";
	//printf("tam dentro: %d\n",(int)palavras.size());
	}
	GeraPalavra(letraAtual+1);
}

int main()
{
	scanf("%d %d %d",&L,&D,&N);
	int f = 0;
	fu(i,D)
	{
		char str[32];
		scanf(" %s",str);
		string s = string(str);
		linguagem.push_back(s);
	//printf("Leitura: %s\n",linguagem[f].c_str());
		f++;
	}
	fu(k,N)
	{
		char str[1024];
		scanf(" %s",str);
		bool entreParenteses = false;
		int letraAtual = 0;
		limpa();
		fu(i,(int)strlen(str))
		{
			char c = str[i];
			if('a' <= c && c <= 'z')
			{
				if(entreParenteses)
				{
					possibilidades[letraAtual].push_back(c);
				}
				else
				{
					possibilidades[letraAtual++].push_back(c);
				}
			}
			else
			{
				if(c == '(')
				{
					entreParenteses = true;
				}
				else
				{
					entreParenteses = false;
					letraAtual++;
				}
			}
		}
		fu(i,(int)linguagem.size())
		{
			palavras.push_back(linguagem[i]);
		}
	//printf("tam fora: %d\n",(int)palavras.size());
		GeraPalavra(0);
		int numPalavras = 0;
		fu(i,(int)palavras.size())
		{
			if(palavras[i] != "")
			{
				numPalavras++;
			}
		}
		printf("Case #%d: %d\n",k+1,numPalavras);
	}
	
	return 0;
}
