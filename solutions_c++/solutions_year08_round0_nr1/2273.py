#include <iostream>
#include <fstream>
#include <conio.h>

#define SERVER_NAME 100

using std::ifstream;
using std::ofstream;
using std::ios;

class ServerInfo
{
public:
	void initial(char* name)
	{
		memset(_name, 0, SERVER_NAME);
		strcpy(_name,name);
		open();
	}
	void  open() {_open = true;}
	void  close() {_open = false;}
	bool  isName(char* name)
	{
		return (strcmp(name, _name)!=0) ? false : true;
	}

	char* name()  {return _name;}
	bool  isOpen()  {return _open;}

private:
	char _name[SERVER_NAME];
	bool _open;
};

int main()
{
	ifstream inputFile("Input.txt");
	ofstream outputFile("Output.txt", ios::app);

	char inbuf[SERVER_NAME];
	if(inputFile.good())
	{
		if(inputFile.getline(inbuf,SERVER_NAME)) 
		{
			int nCase = atoi(inbuf);
			for(int iCase = 1; iCase <= nCase; iCase++)
			{
				inputFile.getline(inbuf,SERVER_NAME);
				int nServer = atoi(inbuf);
				ServerInfo* serverInfoBuffer = (ServerInfo*)malloc(sizeof(ServerInfo)*nServer);
				for(int iServer = 1; iServer <= nServer; iServer++)
				{
					inputFile.getline(inbuf,SERVER_NAME);
					serverInfoBuffer[iServer-1].initial(inbuf);
				}

				inputFile.getline(inbuf,SERVER_NAME);
				int nQuery = atoi(inbuf);
				int swap = 0;
				for(int iQuery = 1; iQuery <= nQuery; iQuery++)
				{
					inputFile.getline(inbuf,SERVER_NAME);
					bool found = false;
					for(int j = 0; j < nServer; j++)
					{
						if( serverInfoBuffer[j].isName(inbuf) &&
							serverInfoBuffer[j].isOpen())
						{
							serverInfoBuffer[j].close();
						}

						if(!found && serverInfoBuffer[j].isOpen())
							found = true;
					}

					if(!found)
					{
						swap++;
						for(int k = 0; k < nServer; k++)
						{
							serverInfoBuffer[k].open();
							if(serverInfoBuffer[k].isName(inbuf))
								serverInfoBuffer[k].close();
						}
					}
				}
				outputFile << "Case #" << iCase << ": " << swap << "\n";
				delete serverInfoBuffer;
			}
		}
		inputFile.close();
		outputFile.close();
	}
	else
	{
		printf("Error : Can not open input file.\n");
	}

	printf("Press any key to continue...");
	getch();
	return 0;
}