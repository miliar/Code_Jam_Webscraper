#include <stdio.h>
#include <string.h>

char dict[5010][20];
char word[100];

int main()
{
	int L,D,N;
	scanf("%d %d %d",&L,&D,&N);
	for(int i=0;i<D;++i)
		scanf(" %s",dict[i]);
	
	for(int t=0; t<N; ++t){
		scanf(" %s",word);
		
		int len = strlen(word);
		int matches = 0 ;

		for(int k=0; k<D; ++k){
			int start = 0;
			bool inside = false;
			bool ok = true;
			for(int i=0; i<L; ++i){
				bool found = false;
				if (inside){
					while (start < len && word[start] != ')') ++start;
					if (start == len) {
						ok = false;
						break;
					}
				}

				for(int j=start; j<len; ++j){
					if (word[j] == '('){
						inside = true;
						continue;
					}

					if (word[j] == ')'){
						inside = false;
						continue;
					}

					if (word[j] == dict[k][i]){
						start = j + 1;
						found = true;
						break;
					}
				}
				if (!found){
					ok = false;
					break;
				}
		 }

		 if (ok) ++matches;
	}
	 printf("Case #%d: %d\n",1+t,matches);	

	}
	return 0;
}
