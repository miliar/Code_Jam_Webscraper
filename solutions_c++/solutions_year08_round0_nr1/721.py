#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(){
	map<string, int> indice;
	int tab_min[110][1100];
	int nTests, test = 0;
	char aux[110];
	cin >> nTests;
	while(nTests--){
		indice.clear();
		int n_se, n_q;
		cin >> n_se; cin.getline(aux, 110);
		for(int i = 0;i < n_se;i++){
			char name[110];
			cin.getline(name, 110);
			//cout << name << '\n';
			indice[name] = i;
			tab_min[i][0] = 0;
		}
		int min_last = 0;
		//cout << "-------------------\n";
		cin >> n_q; cin.getline(aux, 110);
		for(int i = 1;i <= n_q;i++){
			//cout << "linha " << i << '\n';
			char query[110];
			cin.getline(query, 110);
			//cout << query << '\n';
			for(int j = 0;j < n_se;j++){
				if(indice[query] == j)
					tab_min[j][i] = -1;
				else
				if(tab_min[j][i - 1] == -1)
					tab_min[j][i] = min_last + 1;
				else
					tab_min[j][i] = tab_min[j][i - 1] < min_last + 1 ? tab_min[j][i - 1] : min_last + 1;
				//cout << tab_min[j][i] << '\n';
			}
			min_last = -1;
			for(int j = 0;j < n_se;j++)
				if(min_last == -1 || (tab_min[j][i] != -1 && min_last > tab_min[j][i]))
					min_last = tab_min[j][i];
			//cout << "MIN " << min_last << '\n';
		}
		cout << "Case #" << ++test << ": " << min_last << '\n';
	}
	return 0;
}
