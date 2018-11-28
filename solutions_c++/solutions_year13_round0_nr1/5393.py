#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main(){
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.o", "w+", stdout);

	int t;
    cin >> t;
	char buffer[16];
	bool Xbuffer[16];
	bool Obuffer[16];
	bool gameComplete = 1;
	bool gameDraw = 1;
	for(int ti = 0; ti < t; ti++){
		 cout << "Case #" << (ti+1) << ": ";
		 gameComplete = 1;
		 gameDraw = 1;

		 for(int tj = 0; tj < 4; tj++){
			cin >> buffer;
			for(int tk = 0; tk < 4; tk++){
				Xbuffer[tk + tj*4] = (buffer[tk] == 'X') | (buffer[tk] == 'T');
				Obuffer[tk + tj*4] = (buffer[tk] == 'O') | (buffer[tk] == 'T');
				if(buffer[tk] == '.'){
					gameComplete = 0;
				}
			}
		 }
		 for(int tj = 0; tj < 4; tj++){
			 if(Xbuffer[tj]&Xbuffer[tj+4]&Xbuffer[tj+8]&Xbuffer[tj+12]){
				cout <<"X won\n";
				gameDraw = 0;
				break;
			 }
			 if(Obuffer[tj]&Obuffer[tj+4]&Obuffer[tj+8]&Obuffer[tj+12]){
				 cout <<"O won\n";
				 gameDraw = 0;
				 break;
			 }
			 if(Xbuffer[tj*4]&Xbuffer[tj*4+1]&Xbuffer[tj*4+2]&Xbuffer[tj*4+3]){
				cout <<"X won\n";
				gameDraw = 0;
				break;
			 }
			 if(Obuffer[tj*4]&Obuffer[tj*4+1]&Obuffer[tj*4+2]&Obuffer[tj*4+3]){
				 cout <<"O won\n";
				 gameDraw = 0;
				 break;
			 }
		 }
		 if(Xbuffer[0]&Xbuffer[5]&Xbuffer[10]&Xbuffer[15]){
			 cout <<"O won\n";
			 gameDraw = 0;
		 }
		 if(Xbuffer[3]&Xbuffer[6]&Xbuffer[9]&Xbuffer[12]){
			 cout <<"O won\n";
			 gameDraw = 0;
		 }
		 if(Obuffer[0]&Obuffer[5]&Obuffer[10]&Obuffer[15]){
			 cout <<"O won\n";
			 gameDraw = 0;
		 }
		 if(Obuffer[3]&Obuffer[6]&Obuffer[9]&Obuffer[12]){
			 cout <<"O won\n";
			 gameDraw = 0;
		 }
		 if(gameDraw){
			 if(gameComplete){
				 cout <<"Draw\n";
			 }
			 else{
				 cout <<"Game has not completed\n";
			 }
		 }
	}
}