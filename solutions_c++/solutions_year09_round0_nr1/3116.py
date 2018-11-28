
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<char*> Words;
//Un vector de patrones
//Cada patron es un vector de string
//asi los token variables estan en este string
std::vector<std::vector<std::string>> Patterns;

//pregunta si algun elemento de posibilidades es igual a letra
bool match(char letra, std::string posibilidades)
	{
	for(int i=0 ;i < posibilidades.size();++i)
		{
		if( posibilidades[i] == letra )
			return true;
		}
	return false;
	}

int main()
	{
	std::ifstream In("Input.in", std::ios::in);
	if( !In.is_open() )
		{
		std::cerr<<"No se puedo abrir el archivo para lectura\n";
		system("pause");
		exit(1);
		}

	std::ofstream Out("Output.out", std::ios::out | std::ios::trunc);
	if( !Out.is_open() )
		{
		std::cerr<<"No se puedo abrir el archivo para escritura\n";
		system("pause");
		exit(1);
		}

	int L=0;
	int D=0;
	int N=0;
	In>> L;//numero de letras de las palabras
	In>> D;//numero de palabras
	In>> N;//numero de patrones
		
	Words.reserve(25);

	//Leo las palabras y las guardo en Words
	for(int j=0;j < D; ++j)
		{
		char* txt= new char[L+1];
		In>>txt;
		Words.push_back(txt);
		}

	In.ignore(1);

	//Proceso los patrones, por cada uno saco cuantas palabras encajan en este patron
	for(int j=0;j < N; ++j)
		{
			//Lectura del patron
		Patterns.push_back(std::vector<std::string>());
		std::string txt;
		std::getline(In,txt);
			
		std::vector<std::string>& OnePatern = Patterns.back();
		std::string::iterator it= txt.begin();
			while( it != txt.end() )//Por cada token
				{
				if( *it == '(' )
					{
					++it;
					std::string aux;
					while( it != txt.end() && *it != ')' )//se supone que por cada ( hay un )
						{
						aux.push_back(*it);
						it++;
						}
						OnePatern.push_back(aux);
					}else
					{
					std::string aux; aux.push_back(*it);
					OnePatern.push_back(aux);
					}
				++it;
				}

		int NumOfPosibiblesWords=0;
			//Proceso del patron
		for(int k=0;k < Words.size();++k)//por cada palabra
			{
			bool MatchedAll=true;//si hace match con todas las letras sale como entro y se incrementa el contador
			for(int y=0;y < std::strlen(Words[k]);++y)//puedo formar esta palabra, con esas letras?
				{
				if( match(Words[k][y],OnePatern[y] ) == false )
					{
					MatchedAll = false;
					break;//salgo a probar proxima palabra
					}
				}
			if( MatchedAll )
				++NumOfPosibiblesWords;
			}
		
		Out<<"Case #"<<j+1<<": "<<NumOfPosibiblesWords<<std::endl;
				
		}

	In.close();
	Out.close();

	system("pause");
	return 0;
	}


