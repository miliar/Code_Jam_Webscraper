#include <Windows.h>
#include <fstream>
#include <string>
#include <list>
/******************************************************************/
/******************************************************************/

int main(int argc, char* argv[])
{
	std::ifstream infile;
	if(argc>1)
	{
		infile.open(argv[1]);
	}
	else { infile.open("input.in"); }

	int size = 0;
	infile >> size;

	if(size == 0)
	{
		printf("Keine Datei gefunden\n");
		return 0;
	}

	std::ofstream outfile;
	outfile.open("outfile.out",std::ios::out | std::ios::app );
	//std::ofstream log;
	//log.open("log.out",std::ios::out | std::ios::app );

	int a;
	int b;
	int winners;// = 0;

	for(int i=0; i < size; i++)
	{
		infile >> a;
		infile >> b;
		winners = 0;

		for(int num=a; num < b; num++)
		{
			std::string number = std::to_string((long long)num);
			std::list<int> perm;

			for(int pos=1; pos<=number.length();pos++)
			{
				std::string hinten = number.substr(pos, number.length()-pos);
				hinten += number.substr(0,pos);
				int zahl = atoi(hinten.c_str());

				if(zahl >= num+1 && zahl <= b)
				{
					std::list<int>::iterator iter = perm.begin();
					bool isInList = false;

					for(;iter!=perm.end();iter++)
					{
						if( (*iter) == zahl)
						{
							isInList = true;
							break;
						}
					}
					if(!isInList)
					{
						winners++;
						perm.push_back(zahl);
						//log << "NUM["<<i<<"] B: "<<number.c_str()<<" PER: "<<zahl<<" (*) \n";
					}
					//else { log << "NUM["<<i<<"] B: "<<number.c_str()<<" PER: "<<zahl<<" (**) \n"; }
				}
				//else { log << "NUM["<<i<<"] B: "<<number.c_str()<<" PER: "<<zahl<<"\n";}
			}
		}

		outfile << "Case #"<< i+1 <<": "<< winners << "\n";
	}

	outfile.close();
	//log.close();
	return 0;
}