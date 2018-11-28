#include<iostream>
#include<string>
#include<set>

using namespace std;

struct dicionario {
	string nome;
	bool flag;
};

int main()
{
	int numLetra, numPalavra, numTeste;
	string str;
	size_t found;
	
	scanf("%d%d%d", &numLetra, &numPalavra, &numTeste);
	
	string token[numLetra+1];
	dicionario palavra[numPalavra+1];
	
	for(int i = 0; i < numPalavra; i++) {
		cin >> palavra[i].nome;
	}

	for(int teste = 1; teste <= numTeste; teste++) {
		cin >> str;
		int i = 0;
		int index = 0;
		int pos_atual = 0;
		int pos_ant = 0;
		while(i < str.size()) {
			if(str[i] != '(' ) {
				token[index++] = str[i];
				i++;
			} else {
				pos_ant = i;
				pos_atual = str.find_first_of(")", pos_ant++);
				
				token[index++] = str.substr(pos_ant, pos_atual - pos_ant);
				i = pos_atual+1;
				
			}
		}
		
		for(int i = 0; i < numPalavra; i++)
		{
			palavra[i].flag = true;
		}
		
		
		int total = 0;
		char c;
		bool todo, parte;
		/* percorrer todas as palavras */
		for(int i = 0; i < numPalavra; i++)
		{
			if(palavra[i].flag) /* percorrer os tokens */
			{
				todo = true;
				for(int j = 0; j < numLetra; j++)
				{
					parte = false;
					char c = palavra[i].nome[j];
					for(int k = 0; k < token[j].size(); k++)
					{
						if(c == token[j][k]) {
							parte = true;
							break;
						}
					}
					if(!parte) {
						todo = false;
						break;
					}
				}
				if(todo) {
					palavra[i].flag = false;
					total++;
				}
			}
		}
		
		printf("Case #%d: %d\n", teste, total);	
		
	}
	
}

