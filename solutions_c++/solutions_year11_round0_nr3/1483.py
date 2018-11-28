#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

vector<int>wynik;
int t, n, temp;

int main(){
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		wynik.clear();
		scanf("%d", &n);
		for(int j = 0; j < n; j++){
			scanf("%d", &temp);
			wynik.push_back(temp);
		}
		sort(wynik.begin(), wynik.end());
		int x = 0;
		for(int k = 0; k < wynik.size(); k++){
			x^= wynik[k];
		}
		if(x==0){
			int result = 0;
			for(int k = 1; k < wynik.size(); k++){
				result += wynik[k];
			}
			printf("Case #%d: %d\n", i+1, result);
		}else{
			printf("Case #%d: NO\n", i+1);
		}
	}
	return 0;
}
