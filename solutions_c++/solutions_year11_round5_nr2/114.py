#include <cstdio>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

int N;
int a[1010];
int array[1010];

int main(){
	
	int casos;
	
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		
		scanf("%d", &N);
		for(int j = 0; j < N; j++){
			scanf("%d", &a[j]);
		}
		
		/*sort(a,a+N);
		
		int ini = 0, fim = N, med;
		
		while(ini != fim){
			map<int,int> mapa;
			med = (ini+fim+1)/2;
			for(int j = 0; j < N; j++)
				mapa[a[j]]++;
				
			bool off = false;
			for(int j = 0; j < N; j++){
				if(mapa[a[j]] > 0){
					int c= a[j];
					int r = 0;
					while(mapa[c] > 0){
						mapa[c]--;
						r++;
						c++;
					}
					printf("med = %d, inicio = %d, fui ate %d\n", med, a[j], c-1);
					if(r < med)
						off = true;
				}
			}
			if(off){
				fim = med-1;
			}else{
				ini = med;
			}
			
		}*/
		map<int,int> mapa;
		
		for(int j = 0; j < N; j++){
			mapa[a[j]]++;
		}
		int best = N;
		for(map<int,int>::iterator it = mapa.begin(), it2; it != mapa.end();){
			it2 = it;
			it2++;
			int next = it->first+1;
			int pos = 0;
			array[pos++] = it->second;
			while(it2 != mapa.end() && it2->first == next){
				array[pos++] = it2->second;
				it2++;
				next++;
			}
			
			for(int j = 0; j < pos; j++){
				if(j+1 == pos || array[j] > array[j+1]){
					int val = array[j];
					int k;
					for(k = j; k >= 0 && array[k] <= val && array[k] > 0;k--){
						array[k]--;
					}
					best = min(best,j-k);
					
					if(array[j] > 0)
						j--;
				}
			}
			
			
			it = it2;
		}
		
		printf("Case #%d: %d\n", i, best);
	}
	
	return 0;
}