#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <string.h>
#include <stdlib.h>
#include <queue>

#define writeFile(name) freopen(name,"w",stdout)

using namespace std;

int main(){
	int T;
	writeFile("out.out");
	scanf("%d",&T);
	for (int Z = 0; Z < T; Z++)
	{
		vector<string>game;
		cin.ignore();
		for (int i = 0; i < 4; i++)
		{
			string line;
			getline(cin,line);
			game.push_back(line);
		}
		bool hasEmpty = false,Xwon = false,Owon = false;
		for (int i = 0; i < 4; i++)
		{
			bool O,X;
			O = X = false;
			for (int j = 0; j < 4; j++)
			{
				if(game[i][j] == 'O'){
					if(X){
						X = O = false;
						break;
					}
					O = true;
				}
				if(game[i][j] == 'X'){
					if(O){
						X = O = false;
						break;
					}
					X = true;
				}
				if(game[i][j] == '.'){
					X = O = false;
					hasEmpty = true;
					break;
				}
			}
			if(X && !O){
				Xwon = true;
				Owon = false;
				break;
			}
			if(O && !X){
				Xwon = false;
				Owon = true;
				break;
			}
		}
		if(Xwon){
			printf("Case #%d: X won\n",Z+1);
			continue;
		}
		if(Owon){
			printf("Case #%d: O won\n",Z+1);
			continue;
		}
		bool LRO,LRX,RLO,RLX;
		LRO = RLO = LRX = RLX = false;
		bool LRF = false,RLF = false;
		for (int i = 0; i < 4; i++)
		{
			if(game[i][i] == 'O'){
				if(LRX){
					LRX = LRO = false;
					LRF = true;
				}
				LRO = true;
			}
			if(game[i][i] == 'X'){
				if(LRO){
					LRX = LRO = false;
					LRF = true;
				}
				LRX = true;
			}
			if(game[i][i] == '.'){
				LRX = LRO = false;
				LRF = true;
			}
			if(game[i][3-i] == 'O'){
				if(RLX){
					RLX = RLO = false;
					RLF = true;
				}
				RLO = true;
			}
			if(game[i][3-i] == 'X'){
				if(RLO){
					RLX = RLO = false;
					RLF = true;
				}
				RLX = true;
			}
			if(game[i][3-i] == '.'){
				RLX = RLO = false;
				RLF = true;
			}
		}
		if(!RLF){
			if(RLO){
				printf("Case #%d: O won\n",Z+1);
				continue;
			}
			if(RLX){
				printf("Case #%d: X won\n",Z+1);
				continue;
			}
		}
		if(!LRF){
			if(LRO){
				printf("Case #%d: O won\n",Z+1);
				continue;
			}
			if(LRX){
				printf("Case #%d: X won\n",Z+1);
				continue;
			}
		}
		Xwon = Owon = false;
		for (int i = 0; i < 4; i++)
		{
			bool O,X;
			O = X = false;
			for (int j = 0; j < 4; j++)
			{
				if(game[j][i] == 'O'){
					if(X){
						X = O = false;
						break;
					}
					O = true;
				}
				if(game[j][i] == 'X'){
					if(O){
						X = O = false;
						break;
					}
					X = true;
				}
				if(game[j][i] == '.'){
					X = O = false;
					hasEmpty = true;
					break;
				}
			}
			if(X && !O){
				Xwon = true;
				Owon = false;
				break;
			}
			if(O && !X){
				Xwon = false;
				Owon = true;
				break;
			}
		}
		if(Xwon){
			printf("Case #%d: X won\n",Z+1);
			continue;
		}
		if(Owon){
			printf("Case #%d: O won\n",Z+1);
			continue;
		}
		if(hasEmpty){
			printf("Case #%d: Game has not completed\n",Z+1);
		}
		else{
			printf("Case #%d: Draw\n",Z+1);
		}
	}
}