#include <stdio.h>

int main (int argc, const char * argv[])
{
	FILE *inputFile, *outputFile;
	int numberOfCases,caseCounter=0,numberOfSearchEngines,searchEngineCounter=0,numberOfQueries,queryCounter=0;
	
	int searchEngineSwitches;
	int queriesCycled;
	int furthestQuery;
	char filepath[1000]={0};
	
	printf("Enter the filepath of the input file starting with /Users:");
	scanf("%s", filepath);
	
    inputFile=fopen(filepath,"r");
	fscanf(inputFile,"%d\n",&numberOfCases); //Find out how many cases there are
	
	outputFile=fopen("/Users/matthewhubble/Desktop/outputfile.in","w");
	
	for(caseCounter=0;caseCounter<numberOfCases;caseCounter++) //Loop for every case
	{
		char searchEngineNames[100][100]={0};
		char queryNames[1000][100]={0};
		int querySuccess[100]={0};
		numberOfSearchEngines=0;
		searchEngineCounter=0;
		numberOfQueries=0;
		queryCounter=0;
		searchEngineSwitches=0;
		queriesCycled=0;
		furthestQuery=0;
		int bubbleCounter=0;
		
		fscanf(inputFile,"%d\n",&numberOfSearchEngines); //Find out how many search engine names there are
		for(searchEngineCounter=0;searchEngineCounter<numberOfSearchEngines;searchEngineCounter++) //Loop for every search engine name
		{
			fscanf(inputFile,"%[^\n]%*c",&searchEngineNames[searchEngineCounter]); //Store search engine name
		}
		
		fscanf(inputFile,"%d\n",&numberOfQueries); //Find out how many queries there are
		for (queryCounter=0;queryCounter<numberOfQueries;queryCounter++) //Loop for every query
		{
			fscanf(inputFile,"%[^\n]%*c\n",&queryNames[queryCounter]); //Store query name
		}
		
		if (numberOfQueries==0) 
		{
			searchEngineSwitches=0;
		}
		
		else if (numberOfQueries!=0)
		{
			while(queriesCycled!=numberOfQueries)
			{
				for (searchEngineCounter=0;searchEngineCounter<numberOfSearchEngines;searchEngineCounter++)
				{
					for(queryCounter=furthestQuery;queryCounter<numberOfQueries;queryCounter++)
					{
						if (strcmp(searchEngineNames[searchEngineCounter],queryNames[queryCounter])==0)
							break;
					}
					
					querySuccess[searchEngineCounter]=queryCounter;			
				}
				
				for (bubbleCounter=0;bubbleCounter< 100;bubbleCounter++)
				{
					if (querySuccess[bubbleCounter] > furthestQuery)
					{
						furthestQuery = querySuccess[bubbleCounter];
					}	
				}
				queriesCycled=furthestQuery;
				
				if(furthestQuery!=numberOfQueries)
					searchEngineSwitches++;
		    }
	    }
		printf("Case #%d: %d\n",caseCounter + 1,searchEngineSwitches);
		fprintf(outputFile,"Case #%d: %d\n",caseCounter + 1,searchEngineSwitches);
	}
	
    return 0;
}