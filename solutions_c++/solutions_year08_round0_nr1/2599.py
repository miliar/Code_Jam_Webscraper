#include <iostream>

using namespace std;

const int maxS = 100;
const int maxQ = 1000;
const int maxLen = 100;

int compare( const void *arg1, const void *arg2 );

int main()
{
	int N, S, Q, cnt, rescnt;
	char searchEngineNames[maxS][maxLen];
	char queries[maxQ][maxLen];
	int  flags[maxS];

	cin >> N;
	for(int i=1; i<=N; i++){
		/************************************
			Input Data
		*************************************/
		cin >> S;
		cin.ignore(maxLen,'\n'); // skipping end-of-line
		for(int j=0; j<S; j++)  {
			cin.getline(searchEngineNames[j], maxLen);
			flags[j] = 0;
		}
		cin >> Q;
		cin.ignore(maxLen,'\n'); // skipping end-of-line
		for(int j=0; j<Q; j++)
			cin.getline(queries[j], maxLen);
		/************************************
			Solve the Problem
		*************************************/
			qsort(searchEngineNames, S, maxLen, compare);
			cnt=0; rescnt=0;
			for(int j=0; j<Q; j++){
				char *p = (char*) bsearch(queries[j], searchEngineNames, S, maxLen, compare);
				int i = (p-(char*)searchEngineNames)/maxLen;
				if(!flags[i]){
					cnt++;
					if(cnt==S){
						cnt=1; rescnt++;
						memset(flags, '\0', sizeof(flags));
					}
					flags[i]=1;
				}
					
			}
		/************************************
			Output Results
		*************************************/
		cout << "Case #" << i << ": " << rescnt << endl;
		/* Debug
		cout << "----------------\n";
		for(int j=0; j<S; j++)
			cout << searchEngineNames[j] << endl;
		cout << "----------------\n";
		for(int j=0; j<Q; j++)
			cout << queries[j] << endl;
		*/
	}
	return 0;
}

int compare( const void *arg1, const void *arg2 )
{
   /* Compare all of both strings: */
   return strcmp( ( char* ) arg1, ( char* ) arg2 );
}