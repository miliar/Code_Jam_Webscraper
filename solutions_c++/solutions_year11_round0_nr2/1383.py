#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int test;
int c,d,e;
char z1,z2,z3;

char com[200][3];
char opp[200][2];
char tab[10000];
vector<char> wynik;

bool opposite(char x){
	for(int i = 1; i <= 2*d; i++){
		if(x == opp[i][0]){
			for(int j = 0; j < wynik.size(); j++){
				if(wynik[j] == opp[i][1])return true;
			}
		}
	}
	return false;
}
	

int is_in_list(char x,char y){
	for(int i = 1; i <= 2*c; i++){
		if(x == com[i][0] && y == com[i][1])return i;
	}
	return 0;
}
	

int main(){
	scanf("%d", &test);
	for(int i = 0; i < test; i++){
		scanf("%d", &c);
		for(int j = 1; j <= c; j++){
			scanf(" %c%c%c",&com[j][0],&com[j][1],&com[j][2]);
			com[c+j][0] = com[j][1];
			com[c+j][1] = com[j][0];
			com[c+j][2] = com[j][2];
		}
		scanf("%d", &d);
		for(int j = 1; j <= d; j++){
			scanf(" %c%c", &opp[j][0], &opp[j][1]);
			opp[d+j][0] = opp[j][1];
			opp[d+j][1] = opp[j][0];
		}
		scanf("%d ", &e);
		for(int j = 0; j < e; j++){
			scanf("%c", &tab[j]);
		}
		for(int j = 0; j < e; j++){
			wynik.push_back(tab[j]);
			if(wynik.size()>=2){
				int temp = is_in_list(wynik[wynik.size()-1],wynik[wynik.size()-2]);
				while(temp && wynik.size() >= 2){
					wynik.pop_back();
					wynik.pop_back();
					wynik.push_back(com[temp][2]);
					temp = is_in_list(wynik[wynik.size()-1], wynik[wynik.size()-2]);
				}
				if(opposite(wynik[wynik.size()-1])){
					wynik.clear();
					continue;
				}
			}
		}
		printf("Case #%d: [", i+1);
		for(int k = 0; k < wynik.size(); k++){
			if(k == wynik.size()-1)printf("%c", wynik[k]);
			else printf("%c, ",wynik[k]);
		}
		printf("]\n");
		wynik.clear();
	}
	return 0;
}
