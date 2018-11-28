
#include <assert.h>
#include <stdio.h>
#include <string>

const char * deststring="welcome to code jam";
const unsigned int destlength = 19;

std::string * ptexts = NULL;


unsigned int casenum = 0;

std::string * pwords = NULL;
std::string * ptokens = NULL;

void getVariables(const char * fname)
{
	FILE* pInput;
	pInput = fopen(fname, "r");
	assert(pInput);
	char line[1024];
	memset(line,0,1024);

	char * presult = fgets(line, 1024, pInput);
	assert(presult);
	
	sscanf(line, "%d%", &casenum);

	
	assert((casenum>=1)&&(casenum<=100));
	assert(ptexts = new std::string[casenum]);

	for (int i = 1; i<=casenum; i++)
	{
		memset(line,0, 1024);
		presult = fgets(line, 1024, pInput);
		assert(presult);

		if (line[strlen(line)-1] == '\n')
				line[strlen(line)-1] = '\0';
		
		ptexts[i-1] = line;		
	}

	fclose(pInput);
}

unsigned int getwelcometimes(const std::string& content, unsigned int refindex, unsigned int contentindex)
{
	unsigned int times = 0;
	
	int pos = 0;
	
	unsigned int newref = refindex + 1;
	while( (pos = content.find_first_of(deststring[refindex],contentindex)) != -1)
	{
		
			if (refindex == (destlength-1)) 
			{
				times++;
				contentindex = pos + 1;
				continue;
			}
			
			if (pos == (content.length()-1)) return times;
									
			contentindex = pos + 1;

			times += getwelcometimes(content, newref,  contentindex);
			
			
	}
	

	return times;
		
				
}

	

int main(int argc, char* argv[])
{
	assert(argc == 3); //usage: welcodejam inputfile outputfile
	getVariables(argv[1]);
	
	
	FILE* pOutput = fopen(argv[2],"w");
	assert(pOutput);
	
	char resoutput[100];
	memset(resoutput, 0, 100);
	
	unsigned int resultnum = 0;
	for (int i =1; i<=casenum; i++)
	{
		resultnum = getwelcometimes(ptexts[i-1], 0, 0);
		sprintf(resoutput,"Case #%d: %04d\n", i, resultnum);
		fwrite(resoutput, sizeof(char), strlen(resoutput),pOutput);
	}
	
	fclose(pOutput);
	
	delete[] ptexts;
	return 0;
}
