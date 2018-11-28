#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>
#include <string.h>

void readline(char* buf, int buf_size, FILE* fin)
{
	fgets(buf, buf_size, fin);
	
	if(buf[strlen(buf) - 1] == '\n')
		buf[strlen(buf) - 1] = 0;
	
	if(buf[strlen(buf) - 1] == '\r')
		buf[strlen(buf) - 1] = 0;
}

int readint(FILE* fin)
{
	char buf[32];
	
	readline(&buf[0], 32, fin);
	
	return atoi(&buf[0]);
}

class SearchEngine
{
	public:
		
	char* name;
	int frequency;
	
	SearchEngine()
	{
		this->frequency = 0;
	}
	
	~SearchEngine()
	{
		free(this->name);
	}
};

class SearchQuery
{
	public:
		
	char* data;
	
	~SearchQuery()
	{
		free(this->data);
	}
};

class SearchEngineRouter
{
	public:
		int searchEngineCount;
		SearchEngine** searchEngines;
		
		int searchQueryCount;
		SearchQuery** searchQueries;
		
		int searchEngineSwitches;
		SearchEngine* currentSearchEngine;
		
		SearchEngineRouter()
		{
			
		}
		
		void readSearchEngineCount(FILE* fin)
		{
			//fscanf(fin, "%i", &this->searchEngineCount);
			
			this->searchEngineCount = readint(fin);
			
			printf("\n%i search engines", this->searchEngineCount);
		}
		
		void readSearchEngines(FILE* fin)
		{
			this->searchEngines = (SearchEngine**)malloc(this->searchEngineCount * sizeof(SearchEngine*));
			
			char* tmp = (char*)malloc(0xFF);
			
			//fgets(tmp, 0xFF, fin);	//read until the end of the line containing search engine count
			
			for(int i = 0; i < this->searchEngineCount; i++)
			{
				readline(tmp, 0xFF, fin);
						
				//fscanf(fin, "%s", tmp);
				printf("\n%s", tmp);
				this->searchEngines[i] = new SearchEngine();
				
				this->searchEngines[i]->name = (char*)malloc(strlen(tmp) + 1);
				strcpy(this->searchEngines[i]->name, tmp);
			}
			
			free(tmp);
		}
		
		void readSearchQueryCount(FILE* fin)
		{
			//fscanf(fin, "%i", &this->searchQueryCount);
			
			this->searchQueryCount = readint(fin);
			
			printf("\n%i search queries", this->searchQueryCount);
		}
		
		void readSearchQueries(FILE* fin)
		{
			this->searchQueries = (SearchQuery**)malloc(this->searchQueryCount * sizeof(SearchQuery*));
			
			char* tmp = (char*)malloc(0xFF);
			
			for(int i = 0; i < this->searchQueryCount; i++)
			{
				readline(tmp, 0xFF, fin);
				
				printf("\n%s", tmp);
				
				this->searchQueries[i] = new SearchQuery();
				
				this->searchQueries[i]->data = (char*)malloc(strlen(tmp) + 1);
				strcpy(this->searchQueries[i]->data, tmp);
			}
			
			free(tmp);
		}
		
		void computeSearchEngineNameFrequencies(int searchQueriesStart)
		{
			for(int j = 0; j < this->searchEngineCount; j++)
			{
				this->searchEngines[j]->frequency = 0;
			}
			
			for(int i = searchQueriesStart; i < this->searchQueryCount; i++)
				for(int j = 0; j < this->searchEngineCount; j++)
				{
					if(i != searchQueriesStart)
						if(!strcmp(this->searchQueries[i]->data, this->searchQueries[i - 1]->data))
							continue;
					
					if(!strcmp(this->searchQueries[i]->data, this->searchEngines[j]->name))
						this->searchEngines[j]->frequency++;
				}
		}
		
		int distance(SearchEngine* searchEngine, int searchQueriesStart)
		{
			int result = 0;
			
			for(int i = searchQueriesStart; i < this->searchQueryCount; i++, result++)
				if(!strcmp(this->searchQueries[i]->data, searchEngine->name))
					return result;
					
			return result;
		}
		
		//omit search engines having the same name as query
		//also we must choose the engine that is the most distant from our query
		SearchEngine* getLowestFrequencySearchEngine(SearchQuery* searchQuery, int searchQueriesStart)
		{
			int j = 0;
			
			SearchEngine* result = this->searchEngines[j];
			
			while(!strcmp(result->name, searchQuery->data))
				result = this->searchEngines[++j];

			
			for(int i = 0; i < this->searchEngineCount; i++)
			{
				if(
					strcmp(searchQuery->data, this->searchEngines[i]->name) &&
					this->distance(this->searchEngines[i], searchQueriesStart) > this->distance(result, searchQueriesStart)
					)
					result = searchEngines[i];
					
				/*
				if(
					this->searchEngines[i]->frequency < result->frequency &&
					strcmp(searchQuery->data, this->searchEngines[i]->name)
					)
					result = searchEngines[i];
				
				//between two with same frequency choose the most distant one	
				if(
					this->searchEngines[i]->frequency == result->frequency &&
					strcmp(searchQuery->data, this->searchEngines[i]->name) &&
					this->distance(this->searchEngines[i], searchQueriesStart) > this->distance(result, searchQueriesStart)
					)
					result = searchEngines[i];*/
			}
					
			return result;
		}
		
		void routeSearchQueries()
		{
			this->searchEngineSwitches = 0;
			this->currentSearchEngine = NULL;
			
			for(int i = 0; i < this->searchQueryCount; i++)
			{			
				this->computeSearchEngineNameFrequencies(i);
				
				//for(int k = 0; k < this->searchEngineCount; k++)
				//	printf("\n%i %s", this->searchEngines[k]->frequency, this->searchEngines[k]->name);
				
				SearchEngine* searchEngine = this->getLowestFrequencySearchEngine(this->searchQueries[i], i);
				
				if(this->currentSearchEngine == NULL)
				{
					printf("\n#initial: %s -> %i", searchEngine->name, searchEngine->frequency);
					this->currentSearchEngine = searchEngine;
				}
				
				//if the current engine has a different name than query keep running queries on it
				if(strcmp(this->searchQueries[i]->data, this->currentSearchEngine->name))
					continue;
					
				if(strcmp(this->currentSearchEngine->name, searchEngine->name))
				{
					printf("\n#chose: %s -> %i", searchEngine->name, searchEngine->frequency);
					
					this->currentSearchEngine = searchEngine;
					this->searchEngineSwitches++;
				}
			}
		}
		
		~SearchEngineRouter()
		{
			for(int i = 0; i < this->searchEngineCount; i++)
				delete this->searchEngines[i];
				
			free(this->searchEngines);
				
			for(int i = 0; i < this->searchQueryCount; i++)
				delete this->searchQueries[i];
				
			free(this->searchQueries);
		}
};

int main()
{
	FILE* fin = fopen("a.in.txt", "rb");
	FILE* fout = fopen("a.out.txt", "wb");//stdout;
	
	int testCases = readint(fin);
	//fscanf(fin, "%i", &testCases); 
	
	for(int i = 0; i < testCases; i++)
	{
		SearchEngineRouter* searchEngineRouter = new SearchEngineRouter(); 
	
		searchEngineRouter->readSearchEngineCount(fin);
		searchEngineRouter->readSearchEngines(fin);
		searchEngineRouter->readSearchQueryCount(fin);
		searchEngineRouter->readSearchQueries(fin);
	
		searchEngineRouter->routeSearchQueries();
	
		fprintf(fout, "Case #%i: %i\n", i + 1, searchEngineRouter->searchEngineSwitches);
		//printf("Result = %i", searchEngineRouter->searchEngineSwitches);
		printf("\nCase #%i: %i\n", i + 1, searchEngineRouter->searchEngineSwitches);
		delete searchEngineRouter;
		//printf("\nPress any key !");getch();
	}
	
	fclose(fin);
	fclose(fout);
//	getch();
	return 0;
}
