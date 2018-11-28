//MaximZh
//Qualification_A.cpp

#include <stdio.h> //Standard C++ library

//Compare stings
bool cmpstr(const char *str1, const char *str2)
{
	while( (*str1 == *str2)&&(*str1) )
	{
		str1++;
		str2++;
	}
	return (*str1 == *str2);
}

int main()
{
	int N = 0; //Number of cases
	char *searchers[100]; //Search engines' names
	char stmp[101]; //Temporary string for input
	int query[1000]; //Query indices in the "searchers" array
	bool flag[100];

	FILE *pfin = fopen("data.in", "rt");
	FILE *pfout = fopen("data.out", "wt");
	fscanf(pfin, "%d\n", &N); //Input number of cases
	for( int i = 0; i < N; i++ )
	{
		int S = 0;
		int Q = 0;
		fscanf(pfin, "%d\n", &S); //Input number of search engines
		for( int j = 0; j < S; j++ ) //Input search engines' names
		{
			searchers[j] = new char[101];
			fscanf(pfin, "%[^\n]s", searchers[j]);
			fscanf(pfin, "\n");
		}
		fscanf(pfin, "%d\n", &Q); //Input number of queries
		for( int j = 0; j < Q; j++ ) //Input queries
		{
			fscanf(pfin, "%[^\n]s", stmp); //Input a query
			fscanf(pfin, "\n");
			//Get the query's index
			int k = 0; //The index
			while( !(cmpstr(stmp, searchers[k])) ) k++;
			query[j] = k;
		}
		int SwitchNum = 0; //The number of switches
		//Reset flags
		int Nflag = 0;
		for( int j = 0; j < 100; j++ )
			flag[j] = false;
		//Find the position in the query array by which
		//all the search engines' names have occured in the array
		//Then do it again from current position
		for( int q = 0; q < Q; q++ )
		{
			if( !flag[query[q]]	) //Set the falg if necessary
			{
				flag[query[q]] = true;
				Nflag++; //Increase the number of search engines' names occured
			}
			if( Nflag == S ) //The switch is inevitable
			{
				SwitchNum++;
				//Reset flags				
				for( int j = 0; j < 100; j++ )
					flag[j] = false;
				flag[query[q]] = true;
				Nflag = 1;
			}
		}
		//Output
		fprintf(pfout, "Case #%d: %d\n", i+1, SwitchNum);
	}
	fclose(pfout);
	fclose(pfin);
	return 0;
}