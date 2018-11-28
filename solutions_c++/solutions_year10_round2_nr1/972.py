#include <stdio.h>

#include <string>
#include <set>
using namespace std;

set<string> Set;

int main () {

	int cases, icases;
	
	int n,m;
	char buffer[1000];
	int i;
	char c;
	scanf("%d",&cases);
	string str;
	int res;
	
	for (icases = 1; icases <= cases; icases++) {
	
		Set.clear();
	
		scanf("%d %d",&n,&m);
//		printf("%d %d\n", n, m);
		getchar();
		
		for (i=0; i<n; i++) {
			scanf("%s\n", buffer);
	//		printf("li: %s\n",buffer);
			str = buffer;

			Set.insert(str);
		}

		res = 0;
		for (i=0; i<m; i++) {
			str = "";
			while (1) {
				c = getchar();
				if (c == '\n') {
					 break;
				}
				scanf("%[^/ \n]", buffer);
	//			printf("%s\n",buffer);

				
				str += "/";
				str += buffer;
				
		//		printf("procurando: %s\n",str.c_str());
				
				if (Set.find(str) == Set.end()) {
					Set.insert(str);
					res++;
				}
			}
		}
		
		printf("Case #%d: %d\n", icases, res);
	}

	return 0;
}
 
