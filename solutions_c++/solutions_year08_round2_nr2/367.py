#include <cstdio>
#include <vector>
using namespace std;

vector<int> primos;
vector<vector <int> > sets;

bool primo(int num){
	for(int i = 0;i < primos.size();i++)
		if(num % primos[i] == 0)
			return false;
	return true;
}

void init(){
	primos.clear();
	for(int i = 2;i < 501;i++)
		if(primo(i))
			primos.push_back(i);
}

void junta(int a, int b){
	for(int i = 0;i < sets[a].size();i++){
		for(int j = 0;j < sets[b].size();j++)
			if(sets[a][i] == sets[b][j])
				goto sai; 
		sets[b].push_back(sets[a][i]);
		sai:;
	}
	sets.erase(sets.begin() + a);
}

bool comum(int a, int b){
	if(sets[a].size() > sets[b].size()){
		int tmp = a;
		a = b; b = tmp;
	}
	for(int i = 0;i < sets[a].size();i++)
		for(int j = 0;j < sets[b].size();j++)
			if(sets[a][i] == sets[b][j])
				return true;
	return false;
}

int main(){
	init();
	int t = 0, nt;
	scanf("%d", &nt);
	while(nt--){
		int a, b, p, min, n_sets;
		scanf("%d %d %d", &a, &b, &p);
		n_sets = b - a + 1;
		for(min = 0;min < primos.size() && primos[min] < p;min++);
		//printf("--> %d %d\n", min, primos[min]);
		sets.clear();
		for(int i = 0;i < n_sets;i++){
			vector<int> v;
			for(int j = min;j < primos.size();j++)
				if((a + i) % primos[j] == 0)
					v.push_back(primos[j]);
			sets.push_back(v);
		}
		/*for(int i = 0;i < sets.size();i++){
			for(int j = 0;j < sets[i].size();j++)
				printf("%d ", sets[i][j]);
			puts("");
		}*/
		bool mudou = false;
		do{
			mudou = false;
			for(int i = 0;i < sets.size() - 1;i++)
				for(int j = i + 1;j < sets.size();j++)
					if(comum(i, j)){
						--n_sets;
						junta(i, j);
						mudou = true;
						j--;
					}
		}while(mudou);
		printf("Case #%d: %d\n", ++t, n_sets);
	}
	return 0;
}
