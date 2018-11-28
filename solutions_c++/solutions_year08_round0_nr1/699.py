#include <cstdio>
#include <cstdlib>
#include <cstring>

#define	INPUT_BUFFER_LEN	(128)
#define	INPUT_SE_LEN		(128)

#undef	DEBUG

using namespace std;

int main() {
	int n;
	char in_buf[INPUT_BUFFER_LEN];
	
	gets(in_buf);
	n = atoi(in_buf);
	
#ifdef DEBUG
	printf("N = %d\n", n);
#endif
	
	char se[INPUT_SE_LEN][INPUT_BUFFER_LEN];
	int query[INPUT_SE_LEN];
	
	// each case
	for (int i = 0; i < n; i++) {
		gets(in_buf);
		int se_size = atoi(in_buf);
		int switches = 0;
		
		// each search engine
		for (int j = 0; j < se_size; j++) {
			query[j] = 0; // clear query count
			gets(se[j]);

#ifdef DEBUG
			printf("search engine #%d, %s\n", j, se[j]);
#endif

		}
		
		gets(in_buf);
		int query_size = atoi(in_buf);

#ifdef DEBUG
		printf("%d queries\n", query_size);
#endif
		
		// each query
		for (int j = 0; j < query_size; j++) {
			gets(in_buf);

#ifdef DEBUG
			int found = -1;
#endif
			int current_se = -1;
			
			for (int k = 0; k < se_size; k++) {
				if (strcmp(in_buf, se[k]) == 0) {
					current_se = k;
					query[current_se]++;

#ifdef DEBUG
					found = current_se;
					printf("search query #%d: (%d) %s\n", j, k, se[current_se]);
#endif

					break;
				}
			}
			
#ifdef DEBUG
			if (found == -1) {
				printf("wtf???????\n");
			}
#endif
			
			// see if the whole list of SEs has been queried
			int all_queried = 1;
			for (int k = 0; k < se_size; k++) {
				if (query[k] == 0) {
					all_queried = 0;
					break;
				}
			}
			
			// reset if all queried & switches++
			if (all_queried == 1) {
#ifdef DEBUG
					printf("found all at query %d\n", j);
#endif

				for (int k = 0; k < se_size; k++) {
					query[k] = 0; // clear query count
				}
				
				query[current_se] = 1;
				switches++;
			}
		} // query
		
		printf("Case #%d: %d\n", i + 1, switches);
	} // case
	
	return 0;
}
