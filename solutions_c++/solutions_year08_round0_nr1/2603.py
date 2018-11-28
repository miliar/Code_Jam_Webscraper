#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

class CSearchEngine 
{
public:
	char *m_name;
	int  m_counter; 
	int	 m_StartIndex;
	int  m_LastIndex;

	CSearchEngine()
	{
		m_name = 0;
		m_counter = 0;
		m_StartIndex = 10000;
		m_LastIndex = -1;
	};
	~CSearchEngine()
	{
		if(m_name!=0) delete [] m_name;
	};
};

vector<class CSearchEngine*>  SearchEngine;
vector<char*> Queries;

bool compareCounter (CSearchEngine *se1, CSearchEngine *se2)
{
	return se1->m_counter<se2->m_counter;
}

bool compareStartIndex(CSearchEngine *se1, CSearchEngine *se2)
{
	return se1->m_StartIndex>se2->m_StartIndex;
}

bool compareLastIndex(CSearchEngine *se1, CSearchEngine *se2)
{
	return se1->m_LastIndex<se2->m_LastIndex;
}

void PrintSE(vector<CSearchEngine*> &se)
{
	int size = se.size();
	int j;
	for(j=0; j<size; j++)
	{
		printf("SE: %s (%d), start: %d, last: %d\n", 
			se[j]->m_name,
			se[j]->m_counter,
			se[j]->m_StartIndex,
			se[j]->m_LastIndex);
	}
}

void UpdateEngineElement(int j, char *name, vector<CSearchEngine *>&ses)
{
	int size = ses.size();
	int k;
	for(k=0; k<size; k++)
	{
		if(strcmp(ses[k]->m_name, name)==0)
		{
			ses[k]->m_counter++;
			if(j<ses[k]->m_StartIndex)
			{
				ses[k]->m_StartIndex = j;
			}
			if(j>ses[k]->m_LastIndex)
			{
				ses[k]->m_LastIndex = j;
			}
			break;
		}
	}
}

void CopySE(vector<CSearchEngine*> &from, vector<CSearchEngine*> &to)
{
	
	int size = from.size();
	int j;
	CSearchEngine *se;
	for(j=0; j<size; j++)
	{
			se = new CSearchEngine();	
			se->m_name = new char [strlen(from[j]->m_name)+1];
			se->m_counter = 0;
			strcpy(se->m_name, from[j]->m_name);

			to.push_back(se);
	}
}

void PrintQuery(vector<char *> &q)
{
	int size = q.size();
	int j;
	for(j=0; j<size; j++)
	{
		printf("Q[%d]:%s\n", j, q[j]);
	}
}

void ResetSEcounter(vector<CSearchEngine*> &se)
{
	int size = se.size();
	int j;
	for(j=0; j<size; j++) se[j]->m_counter = 0;
}

void usage(char *exename)
{
	printf("Usage:\n");
	printf("%s <input file>\n", exename);
}


int solve(vector<CSearchEngine*> &ses, vector<char *> &query)
{
	//printf("call solve..\n");
	int i;
	if(ses[0]->m_counter==0)
	{
		//printf("0 found..\n");	
		return 0;
	}

	vector<char *> front_query;
	vector<char *> back_query;
	vector<CSearchEngine *> front_se;
	vector<CSearchEngine *> back_se;
	char *name;
	int counter = 0;
	//printf("sort start index.\n");
	sort(ses.begin(), ses.end(), compareStartIndex);	// find which query last 
	//PrintSE(ses);	
	CopySE(ses, front_se);
	for(i=ses[0]->m_StartIndex; i<query.size(); i++)
	{
		front_query.push_back(query[i]);
		UpdateEngineElement(counter, query[i], front_se);
		counter++;
	}
//	printf("front query\n");
//	PrintQuery(front_query);
	//printf("front SE\n");
	//PrintSE(front_se);
	sort(front_se.begin(), front_se.end(), compareCounter);
	int n1 = solve(front_se, front_query);
	return n1+1;
	//printf("n1: %d\n", n1);


	//printf("sort last index.\n");
	sort(ses.begin(), ses.end(), compareLastIndex);	// find which query early 
	//PrintSE(ses);	
	CopySE(ses, back_se);

	counter = 0;
	for(i=0; i<=ses[0]->m_LastIndex; i++)
	{
		back_query.push_back(query[i]);
		UpdateEngineElement(counter, query[i], back_se);
		counter++;
	}
//	printf("back query\n");
//	PrintQuery(back_query);
	//PrintSE(back_se);
	sort(back_se.begin(), back_se.end(), compareCounter);
	int n2 = solve(back_se, back_query);
	//printf("n2: %d\n", n2);

	front_query.clear();
	back_query.clear();
	front_se.clear();
	back_se.clear();

	return n2+1;
	//printf("n1: %d, n2: %d\n", n1, n2);
	if(n1<n2) return n1+1;
	else return n2+1;
}

int main(int argc, char *argv[])
{
	if(argc!=2)
	{
		usage(argv[0]);
		return 1;
	}

	FILE *inf;
	int i, j;
	int iNSearchEngines;
	int iNcases, iNQueries;
	FILE *outf;

	inf = fopen(argv[1], "r");
	if(inf==NULL) return 1;
	outf = fopen("output.txt", "w");

	char line[128];
	CSearchEngine *se;
	fgets(line, 128, inf);
	sscanf(line, "%d", &iNcases);
	int k;

	for(i=0; i<iNcases; i++)
	{
		SearchEngine.clear();
		Queries.clear();
		fgets(line, 128, inf);
		sscanf(line, "%d", &iNSearchEngines);
		for(j=0; j<iNSearchEngines; j++)
		{
			fgets(line, 128, inf);
			line[strlen(line)-1]='\0';
			se = new CSearchEngine();	
			se->m_name = new char [strlen(line)+1];
			se->m_counter = 0;
			strcpy(se->m_name, line);
			SearchEngine.push_back(se);
		}


		fgets(line, 128, inf);
		sscanf(line, "%d", &iNQueries);
		char *name;
		for(j=0; j<iNQueries; j++)
		{
			fgets(line, 128, inf);
			line[strlen(line)-1]='\0';
			name = new char [strlen(line)+1];
			strcpy(name, line);
			Queries.push_back(name);
			UpdateEngineElement(j, name, SearchEngine);
		}
		sort(SearchEngine.begin(), SearchEngine.end(), compareCounter);

		int n = solve(SearchEngine, Queries);
		fprintf(outf, "Case #%d: %d\n", i+1, n);
		printf("Case #%d: %d\n", i+1, n);
	}

	fclose(inf);
	fclose(outf);
}
