#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<deque>
#include<cstring>
#include<string>
#include<cmath>
#include<ctime>
#include<cstdlib>
using namespace std;
#define X first
#define Y second
typedef long long LL;
typedef __int128_t VL;

char mapa[15][15];
bool mozna_dojsc[15][15];
int R, C;
int cave;
//kierunek: 0 - nie wiadomo, 1 - w prawo, 2 - w prawo, a potem w lewo, -1 - w lewo, -2 - w lewo, a potem w prawo, 9 - w dol

bool jest_OK(int poziom_zaglebienia, vector<pair<int, int> > pozycje, int kierunek){
	if(poziom_zaglebienia > 16*8)
		return false;
	
	bool juz_ok = true;
	for(int i = 0; i < pozycje.size(); i++)
		if(mapa[pozycje[i].X][pozycje[i].Y] != cave){
			juz_ok = false;
			break;
		}
	if(juz_ok)
		return true;
	
	if(kierunek == 0){
		return (jest_OK(poziom_zaglebienia+1, pozycje, 2) || jest_OK(poziom_zaglebienia+1, pozycje, -2));
	}
	else if(kierunek == 2){
		if(jest_OK(poziom_zaglebienia+1, pozycje, -1))
			return true;
		bool zmiana = false;
		for(int i = 0; i < pozycje.size(); i++)
			if(mapa[pozycje[i].X][pozycje[i].Y+1] != '#'){
				pozycje[i].Y++;
				zmiana = true;
				if(!mozna_dojsc[pozycje[i].X][pozycje[i].Y])
					return false;
			}
		if(zmiana)
			return jest_OK(poziom_zaglebienia+1, pozycje, 2);
		else
			return false;
	}
	else if(kierunek == -2){
		if(jest_OK(poziom_zaglebienia+1, pozycje, 1))
			return true;
		bool zmiana = false;
		for(int i = 0; i < pozycje.size(); i++)
			if(mapa[pozycje[i].X][pozycje[i].Y-1] != '#'){
				pozycje[i].Y--;
				zmiana = true;
				if(!mozna_dojsc[pozycje[i].X][pozycje[i].Y])
					return false;
			}
		if(zmiana)
			return jest_OK(poziom_zaglebienia+1, pozycje, -2);
		else
			return false;
	}
	else if(kierunek == 9){
		bool zmiana = false;
		for(int i = 0; i < pozycje.size(); i++)
			if(mapa[pozycje[i].X+1][pozycje[i].Y] != '#'){
				pozycje[i].X++;
				zmiana = true;
				if(!mozna_dojsc[pozycje[i].X][pozycje[i].Y])
					return false;
			}
		if(zmiana)
			return jest_OK(poziom_zaglebienia+1, pozycje, 0);
		else
			return false;
	}
	else if(kierunek == 1){
		if(jest_OK(poziom_zaglebienia+1, pozycje, 9))
			return true;
		bool zmiana = false;
		for(int i = 0; i < pozycje.size(); i++)
			if(mapa[pozycje[i].X][pozycje[i].Y+1] != '#'){
				pozycje[i].Y++;
				zmiana = true;
				if(!mozna_dojsc[pozycje[i].X][pozycje[i].Y])
					return false;
			}
		if(zmiana)
			return jest_OK(poziom_zaglebienia+1, pozycje, 1);
		else
			return false;
	}
	else if(kierunek == -1){
		if(jest_OK(poziom_zaglebienia+1, pozycje, 9))
			return true;
		bool zmiana = false;
		for(int i = 0; i < pozycje.size(); i++)
			if(mapa[pozycje[i].X][pozycje[i].Y-1] != '#'){
				pozycje[i].Y--;
				zmiana = true;
				if(!mozna_dojsc[pozycje[i].X][pozycje[i].Y])
					return false;
			}
		if(zmiana)
			return jest_OK(poziom_zaglebienia+1, pozycje, -1);
		else
			return false;
	}
	
while(true);
return false;	
}


int main(){
	int testy;
	scanf("%d", &testy);
	for(int t = 1; t <= testy; t++){
		scanf("%d %d", &R, &C);
		for(int i = 0; i < R; i++){
			scanf("%s", mapa[i]);
		}
		
		printf("Case #%d:\n", t);
	
	
		for(cave = int('0'); ; cave++){
			for(int i = 0; i < 10; i++)
				fill(mozna_dojsc[i], mozna_dojsc[i]+10, false);
			int liczba_sposobow = 0;
			for(int i = R-2; i >= 1; i--){
				for(int j = 1; j < C-1; j++)
					if(mapa[i][j]==cave)
						mozna_dojsc[i][j] = true;
				for(int j = 1; j < C-1; j++)
					if(mozna_dojsc[i+1][j] && mapa[i][j]!='#')
						mozna_dojsc[i][j] = true;
				for(int j = 1; j < C-1; j++)
					if(mozna_dojsc[i][j-1] && mapa[i][j]!='#')
						mozna_dojsc[i][j] = true;
				for(int j = C-2; j >= 1; j--)
					if(mozna_dojsc[i][j+1] && mapa[i][j]!='#')
						mozna_dojsc[i][j] = true;
				for(int j = 1; j < C-1; j++)
					if(mozna_dojsc[i][j])
						liczba_sposobow++;
			}
			if(liczba_sposobow == 0)
				break;
			
			vector<pair<int, int> > poczatkowe;
			for(int i = 1; i < R-1; i++)
				for(int j = 1; j < C-1; j++)
					if(mozna_dojsc[i][j]){
						poczatkowe.push_back(make_pair(i, j));
						break;
					}
					
			if(jest_OK(0, poczatkowe, 0))
				printf("%c: %d Lucky\n", char(cave), liczba_sposobow);
			else
				printf("%c: %d Unlucky\n", char(cave), liczba_sposobow);
		}

	}
	return 0;
}
