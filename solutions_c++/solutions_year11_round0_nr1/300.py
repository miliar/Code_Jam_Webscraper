#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int N, tempo1,tempo2,pos1,pos2, tempo;

int main(){
	
	int casos;
	
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		char str[6];
		int val;
		
		scanf("%d", &N);
		
		tempo1 = tempo2 = tempo = 0;
		pos1 = pos2 = 1;
		
		for(int j = 1; j <= N; j++){
			scanf("%s %d", str, &val);
			
			if(str[0] == 'O'){
				
				tempo = max(tempo,tempo1+abs(pos1-val))+1;
				tempo1 = tempo;
				pos1 = val;
			}else{
				tempo = max(tempo,tempo2+abs(pos2-val))+1;
				tempo2 = tempo;
				pos2 = val;o
			}
		}
		
		printf("Case #%d: %d\n", i, tempo);
	}
	
	return 0;
}
