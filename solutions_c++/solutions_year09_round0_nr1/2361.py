#include <iostream.h>
#include <fstream.h>
#include <list.h>

#define MAXLEN 5000

int main(int argc, char* argv[])
{
	int D, L, K, N, X;
	int i;
	unsigned int j;
	
	bool bintoken;
	int  imatch;
	bool bmatchfound;
	
	char sLine[MAXLEN];

	list<string> sLang;
	list<string>::iterator iter; 
	
	ifstream inFile;
	
	if ( argc < 2 )
	{
		inFile.open("A-test.in");
	}
	else
	{
		inFile.open(argv[1]);
	}
	
	//inFile.open("A-test.in");
	
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> L;
	inFile >> D;
	inFile >> N;
	
	inFile.getline(sLine,MAXLEN);

	sLang.clear();
	for (X=0;X<D;X++)
	{
		inFile.getline(sLine,MAXLEN);
		sLang.push_back(sLine);
	}
	
	for (X=0;X<N;X++)
	{
		K = 0;
		inFile.getline(sLine,MAXLEN);

		for (iter=sLang.begin();iter!=sLang.end();iter++)
		{
			// loop
			j = 0;
			imatch = 0;
			for (i=0;i<L;i++)
			{

				if ( sLine[j] == '(' )
				{
					// in token
					bmatchfound = false;
					while ( sLine[j] != ')' )
					{
						// bmatchfound secures that if a character occurs multiple times in a token
						// it will not mess things up, for instance (aa)
						if ( (sLine[j] == (*iter)[i]) && ( bmatchfound == false ) )
						{
							imatch++;
							bmatchfound = true;
						}
						j++;
					}
					j++;
				}
				else
				{
					if ( sLine[j] == (*iter)[i] )
					{
						imatch++;
					}
					j++;
				}
			}
			if ( imatch == L )
				K++;
		}
		
		cout << "Case #" << X+1 << ": " << K << endl;
	}
	
	inFile.close();
	return 0;
}