// Problem Set: Qualifying
// Problem Number: 001

// The urban legend goes that if you go to the Google homepage and search for "Google", 
// the universe will implode. We have a secret to share... It is true! Please don't try 
// it, or tell anyone. All right, maybe not. We are just kidding.

// The same is not true for a universe far far away. In that universe, if you search on 
// any search engine for that search engine's name, the universe does implode!

// To combat this, people came up with an interesting solution. All queries are pooled 
// together. They are passed to a central system that decides which query goes to which 
// search engine. The central system sends a series of queries to one search engine, 
// and can switch to another at any time. Queries must be processed in the order they're 
// received. The central system must never send a query to a search engine whose name 
// matches the query. In order to reduce costs, the number of switches should be 
// minimized.

// Your task is to tell us how many times the central system will have to switch between 
// search engines, assuming that we program it optimally. 

#include <cstdlib>
#include <iostream>

int const sname_maxsize = 128;

int minchng(char** slist, int snum, char** qlist, int qnum, int chngs, char* found)
{
	if (!qnum) return chngs;
	int i;
	
	for (i = 0; strcmp(slist[i], *qlist); ++i);
	found[i] = 'y';
	
	if (strchr(found, 'n') == NULL)
	{ ++chngs; memset(found, 'n', snum); found[i] = 'y'; };
	
	return minchng(slist, snum, ++qlist, --qnum, chngs, found);
};

int main()
{
	int testcases, tcase, snum, qnum, i;
	scanf("%d\r\n", &testcases);
	
	char **search_engine, **query;
	char *found;
	
	tcase = 0;
	while (tcase++ < testcases)
	{
		scanf("%d\r\n", &snum);
		search_engine = (char**) malloc(snum * sizeof(char*));
		
		for (i = 0; i < snum; ++i)
		{ 
			search_engine[i] = (char*) malloc(sname_maxsize * sizeof(char));
			std::cin.getline(search_engine[i], sname_maxsize);
		};
		
		scanf("%d\r\n", &qnum);
		query = (char**) malloc(qnum * sizeof(char*));
		
		for (i = 0; i < qnum; ++i)
		{ 
			query[i] = (char*) malloc(sname_maxsize * sizeof(char));
			std::cin.getline(query[i], sname_maxsize);
		};
		
		found = (char*) malloc((snum + 1) * sizeof(char));
		memset(found, 'n', snum); found[snum] = (char)0;
		
		// here is where we do our recursion.
		printf("Case #%d: %d\n", tcase, minchng(search_engine, snum, query, qnum, 0, found));
		free(found);
		
		while (snum--) free(search_engine[snum]);
		free(search_engine);
		
		while (qnum--) free(query[qnum]);
		free(query);
	};
};
