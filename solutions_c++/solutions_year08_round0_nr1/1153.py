#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int N;
    scanf("%d", &N);
    //fprintf(stderr, "-- N = %d\n", N);
    for(int n_case=0; n_case<N; n_case++) {
        //fprintf(stderr, "\n\n\n\n ---- test %d ---\n", n_case);
	int S,Q;
	vector<string> engines,queries;

	scanf("%d\n", &S);
	//fprintf(stderr,"-- S = %d\n", S);
	for(int n_engine=0; n_engine<S; n_engine++) {
	    char tmp[2000];
	    gets(tmp);
	    engines.push_back(tmp);
	    //fprintf(stderr,"-- S[%d] = %s\n", n_engine, tmp);
	}
	scanf("%d\n", &Q);
	//fprintf(stderr, "-- Q = %d\n", Q);
	for(int n_query=0; n_query<Q; n_query++) {
	    char tmp[2000];
	    gets(tmp);
	    queries.push_back(tmp);
	    //fprintf(stderr,"-- Q[%d] = %s\n", n_query, tmp);
	}

	vector<vector<int> > table(Q,vector<int>(S,0)); 
	for(int i=0;i<Q;i++) {
	    //fprintf(stderr,"-- ");
	    for(int j=0;j<S;j++) {
		if(queries[i]==engines[j])
		    table[i][j]=-1;
		else if(i==0)
		    table[i][j]=0;
		else if (table[i-1][j]!=-1)
		    table[i][j]=table[i-1][j];
		else {
		    int min_switches = Q+1;
		    for(int n_query=0; n_query<S; n_query++)
			if (table[i-1][n_query]!=-1)
			    min_switches = min(min_switches,table[i-1][n_query]);
		    table[i][j] = min_switches+1;
		}
		//fprintf(stderr,"%d ",table[i][j]);
	    }
	    //fprintf(stderr,"\n");
	}
		    
	int min_switches = Q+1;
        if (Q!=0)
	    for(int n_query=0; n_query<S; n_query++)
		if (table[Q-1][n_query]!=-1)
		    min_switches = min(min_switches,table[Q-1][n_query]);
		else;
	else
	    min_switches = 0;
	printf("Case #%d: %d\n", n_case+1, min_switches);
    }
    return 0;
}
