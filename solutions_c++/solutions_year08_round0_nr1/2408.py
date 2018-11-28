#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>


int main() {
	

	int testCases;

	scanf("%d\n", &testCases);

	for (int t = 0; t < testCases; t++) {
		
		map <string, int> dp [1099];

		int numberOfSearchEngines;

		scanf("%d\n", &numberOfSearchEngines);

		vector<string> searchEngines;
		
		for (int i = 0; i < numberOfSearchEngines; i++) {
		
			char c[999];	
			
			gets(c);

			string s(c);

			searchEngines.push_back( s );

		}
		int numberOfQueries;

		scanf("%d\n", &numberOfQueries);

		vector<string> queries;
		
		for (int i = 0; i < numberOfQueries; i++) {
			
			char c[999];	
			
			gets(c);

			string s(c);
			
			queries.push_back(s);

		}

		for (int i = 0; i < numberOfSearchEngines; i++) {
			if ( numberOfQueries > 0 && searchEngines [i] != queries [0] )	
				dp [0][searchEngines[i]] = 0;
			else 
				dp [0][searchEngines[i]] = 99999999;
			
		}
		
		for (int i = 1; i < numberOfQueries; i++) {
			
			for (int j = 0; j < numberOfSearchEngines; j++) {

				dp [i][searchEngines[j]] = 99999999;

			}

		}

		for (int i = 1; i < numberOfQueries; i++) {
			
			for (int j = 0; j < numberOfSearchEngines; j++) {
					
				if ( searchEngines [j] == queries [i] ) 
					continue;	

				for (int k = 0; k < numberOfSearchEngines; k++) {
					
					dp [i][searchEngines[j]] = min( 
						dp [i][searchEngines[j]], 
						dp [i - 1][searchEngines[k]] 
							+ (int) ( (searchEngines [j] != searchEngines[k]) )
						);

				}
			
			}

		}

		
		int result = 99999999;


		for (int i = 0; i < numberOfSearchEngines; i++) {
			
			if ( numberOfQueries != 0 ) {

				result = min(result, dp [numberOfQueries - 1][searchEngines[i]]);
			} else {
				result = 0;
			}

		}
		cout <<"Case #" << t + 1 << ": " << result << endl;
		

	}

	return 0;

}
	
			
	
		
