/*
 * main.cpp
 *
 *  Created on: 22/Mai/2010
 *      Author: Bisc8
 */

#include <vector>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

bool exist(vector<string> criados, string dir)
{
	bool resposta = false;

	for(int i = 0; i < criados.size(); i++)
	{
		if(criados[i] == dir)
			resposta = resposta || true;
	}

	return resposta;
}

int contar(vector<string> criados, vector<string> novos)
{
	int count = 0;

	for(int i = 0; i < novos.size(); i++)
	{

		string novo = novos[i];
		string temp = novo;

		int k;
		int indice = 0;

		while((k = novo.find("-")) != string::npos)
		{
			indice += k+1;
			if(!exist(criados,temp.substr(0,indice)))
			{
				criados.push_back(temp.substr(0,indice));
				//cout << "Adicionado: " << temp.substr(0,indice) << endl;
				count++;
			}
			novo.erase(0,k+1);

		}
	}

	return count;
}


int main()
{
	int T,N,M;

	string filename = "A-small-attempt0";
	freopen((filename+".in").c_str(), "r", stdin);
	freopen((filename+".out").c_str(), "w", stdout);

	cin >> T;

	for(int a = 0; a < T; a++)
	{
		cin >> N;
		cin >> M;

		vector<string> criados;
		vector<string> novos;

		for(int n = 0; n < N; n++)
		{
			string s;
			cin >> s;

			unsigned int i = 0;
			int j = 0;

			s.erase(0,1);

			string final = "";

			while(i != string::npos)
			{
				i = s.find('/',0);
				string str = s.substr(0,i);
				s.erase(0,i+1);
				final += str;

				std::stringstream ss;
				ss << j;

				final += ss.str();
				final += "-";

				j++;

			}
			criados.push_back(final);
			//cout << final << endl;

		}

		for(int m = 0; m < M; m++)
		{
			string s;
			cin >> s;

			unsigned int i = 0;
			int j = 0;

			s.erase(0,1);

			string final = "";

			while(i != string::npos)
			{
				i = s.find('/',0);
				string str = s.substr(0,i);
				s.erase(0,i+1);
				final += str;

				std::stringstream ss;
				ss << j;

				final += ss.str();
				final += "-";
				j++;

			}

			novos.push_back(final);
			//cout << final << endl;
		}

		cout << "Case #" << (a+1) << ": " << contar(criados,novos) << endl;

	}
}
