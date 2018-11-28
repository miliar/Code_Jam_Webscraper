#include<stdio.h>
#include<string.h>
#include<string>
#include<map>
#include<vector>
#include<algorithm>

#define fu(i,n) for(int i = 0; (i) < (n); i++)
#define MSET(A, x) memset(A, x, sizeof(A))
#define MAX 1024

using namespace std;

int N;
map<char, vector<int> > mapa;
string mensagem = "welcome to code jam";
int possibilidades[MAX]; // indice -> posMapa

int QuatroDigitos(int valor)
{
	char resp[128];
	itoa(valor, resp, 10);
	string s = string(resp);
	for(int i = s.size(); i < 4; i++)
	{
		s = "0" + s;
	}
	int j = 0;
	for(int i = (int)s.size()-1; i >= (int)s.size()-4; i--)
	{
		resp[j++] = s[i];
	}
	reverse(resp,resp+j);
	resp[j] = '\0';
	return atoi(resp);
}

int CalcPossibilidade(int posMensagem, int posMapa)
{
		/*if(possibilidades[posMapa])
		{
		printf("retorno1\n");
			return possibilidades[posMapa];
		}*/
		int prox = posMensagem+1;
		if(prox >= (int)mensagem.size())
		{
		//printf("retorno2\n");
			return 1;
		}
		char c = mensagem[prox];
		int possibilidade = 0;
		fu(j,(int)mapa[c].size())
		{
			int pos = mapa[c][j];
		//printf("cMensagem : %c posMensagem: %d posMapa :%d letra: %c pos: %d\n",mensagem[posMensagem],posMensagem,posMapa,c,pos);
			if(pos > posMapa)
			{
		//printf("entrou\n");
				possibilidade += CalcPossibilidade(prox,pos);
				possibilidade = QuatroDigitos(possibilidade);
				possibilidades[pos] = possibilidade;
		//printf("possibilidade dentro do if: %d cMensagem : %c posMensagem: %d posMapa :%d\n",possibilidade,mensagem[posMensagem],posMensagem,posMapa);
			}
		}
	//printf("retornoFim possibilidade: %d\n",possibilidade);
		return possibilidade;
}

void limpa()
{
	mapa.clear();
	MSET(possibilidades,0);
}

int main()
{
	char str[MAX];
	gets(str);
	sscanf(str,"%d",&N);
//printf("N: %d\n",N);
	fu(k,N)
	{
		limpa();
		gets(str);
	//printf("%s\n",str);
		fu(i,(int)mensagem.size())
		{
			char c = mensagem[i];
			if(mapa[c].size() != 0)
			{
				continue;
			}
			fu(j,(int)strlen(str))
			{
				char c2 = str[j];
				if(c == c2)
				{
					mapa[c].push_back(j);
				}
			}
		}
		int possibilidade = 0;
		char c = mensagem[0];
		fu(j,(int)mapa[c].size())
		{
				int pos = mapa[c][j];
		//printf("pos mensagem: %d pos string: %d\n",i,pos);
				possibilidade += CalcPossibilidade(0,pos);
				possibilidade = QuatroDigitos(possibilidade);
		//printf("possibilidade: %d\n",possibilidade);
		}
		char resp[128];
		itoa(possibilidade, resp, 10);
		string s = string(resp);
		for(int i = s.size(); i < 4; i++)
		{
			s = "0" + s;
		}
		printf("Case #%d: %s\n",k+1,s.c_str());
		/*
		for(int i = s.size(); i < 4; i++)
		{
			s = "0" + s;
		}
		*/
		//printf("l: %d\n",l);
	}
	return 0;
}
