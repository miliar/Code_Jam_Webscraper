#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main()
{

	// Read from file
#if 1
	ifstream readStream;
	ofstream writeStream;

	readStream.open("B-large.in", ios::in);
	writeStream.open("B-large.out", ios::out);
#endif

	const int size = 2000;
	char temp[size];
	readStream.getline(temp, size, '\n');
	int nCase = atoi(temp);

	char *splitted;
	int i, b, o, c;

	vector<char*> baseElements;
	vector<char*> opposeElements;

	for(i=0; i<nCase; i++)
	{
		baseElements.clear();
		opposeElements.clear();
		readStream.getline(temp, size, '\n');

		splitted = strtok(temp," ");
		int nBase = atoi(splitted);

		for(b=0; b<nBase; b++)
		{
			splitted = strtok(NULL," ");
			baseElements.push_back(splitted);
		}

		splitted = strtok(NULL," ");
		int nOpposed = atoi(splitted);
		for(o=0; o<nOpposed; o++)
		{
			splitted = strtok(NULL," ");
			opposeElements.push_back(splitted);
		}

		splitted = strtok(NULL," ");
		int nInput = atoi(splitted);
		char* input = strtok(NULL," ");

		vector<char> invoke;
		invoke.clear();

		for(int c=0; c<nInput; c++)
		{
			if(invoke.size() == 0)
			{
				invoke.push_back(input[c]);
			} else {

				//Check combine
				bool isCombine =false;
				for(b=0; b<nBase; b++)
				{
					bool comb1 = ((invoke.back() == baseElements[b][0])&&(input[c] == baseElements[b][1]));
					bool comb2 = ((invoke.back() == baseElements[b][1])&&(input[c] == baseElements[b][0]));
					if(comb1 || comb2)
					{
						invoke.pop_back();
						invoke.push_back(baseElements[b][2]);
						isCombine =true;
						break;
					}	
				}
				if(isCombine) continue;

				//Check Opposed
				bool isOppose = false;
				for(o=0; o<nOpposed; o++)
				{
					if(input[c] == opposeElements[o][0])
					{
						for(int l = 0; l < invoke.size(); l++)
						{
							if(invoke[l] == opposeElements[o][1])
							{
								invoke.clear();
								isOppose =true;
								break;
							}
						}
					} else if(input[c] == opposeElements[o][1]) {
						for(int l=0;l< invoke.size(); l++)
						{
							if(invoke[l] == opposeElements[o][0])
							{
								invoke.clear();
								isOppose=true;
								break;
							}
						}
					}
					if(isOppose) break;
				}
				if(isOppose) continue;
				invoke.push_back(input[c]);
			}
		}


		writeStream<<"Case #"<<i+1<<": "<<"[";
		for(c = 0; c < invoke.size(); c++)
		{
			if(c == invoke.size()-1) writeStream<<invoke[c];
			else writeStream<<invoke[c]<<", ";
		}
		writeStream<<"]"<<endl;
	}

	readStream.clear();
	readStream.close();

	writeStream.clear();
	writeStream.close();

	return 0;
}