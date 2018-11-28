#include <stdio.h>
#include <string>
using namespace std;

char combine[40][4];
char oppose[40][3];
int C, D, N;
char invoke[128];

void run(int fall){
	

	scanf("%d", &C);
	for(int i=0; i<C; i++){
		scanf("%s", combine[i]);
	}

	scanf("%d", &D);	
	for(int i=0; i<D; i++){
		scanf("%s", oppose[i]);
	}

	scanf("%d", &N);
	scanf("%s", invoke);
	string arr;

	for(int i=0; i<N; i++){
		char c = invoke[i];
		if(arr.size() > 0){
			char d = arr[arr.size()-1];
			int done=0;
			for(int i=0; i<C; i++){
				if((c == combine[i][0] && d == combine[i][1])
					|| (d == combine[i][0] && c == combine[i][1])){
					arr[arr.size()-1] = combine[i][2];
					done=1;
					break;
				}
			}
			if(done){
				continue;
			}
			for(int i=0; i<D; i++){
				for(int j=0; j<arr.size(); j++){
					if((c == oppose[i][0] && arr[j] == oppose[i][1])
						|| (arr[j] == oppose[i][0] && c == oppose[i][1])){
							arr.clear();
							done=1;
							break;
					}
				}
				if(done){
					break;
				}
			}
			if(done){
				continue;
			}
		}
		arr.push_back(c);
	}
	
	printf("Case #%d: [", fall+1);
	if(arr.size() > 0){
		printf("%c", arr[0]);
	}
	for(int i=1; i<arr.size(); i++){
		printf(", %c", arr[i]);
	}

	printf("]\n");
}

int main() {
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++){
		run(i);
	}
}
