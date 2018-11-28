#include<iostream>
#include<fstream>

using namespace std;

int check(char a, char b, char c, char d)
{
	if(a=='T') a=b;
	if(b=='T') b=a;
	if(c=='T') c=a;
	if(d=='T') d=a;
	if((a==b)&&(b==c)&&(c==d)) return 1;
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");
	int t, game_over, found_winner;
	char b[4][4], winner;
	fin>>t;
	for(int count=0;count<t;count++) {
	
		game_over=1;
		found_winner=0;
		
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				fin>>b[i][j];
				if(b[i][j]=='.') game_over=0;
			}
		}
		//Horizontal
		for(int i=0;i<4;i++) {
			if((b[i][0]=='.') || (b[i][1]=='.') || (b[i][2]=='.') || (b[i][3]=='.'))
				continue;
			if((check(b[i][0],b[i][1],b[i][2],b[i][3])==1)) {
				found_winner=1;
				winner=(b[i][0]=='T')?b[i][1]:b[i][0];
				break;
			}
		}
		//Vertical
		if(!found_winner) {
			for(int j=0;j<4;j++) {
				if((b[0][j]=='.') || (b[1][j]=='.') || (b[2][j]=='.') || (b[3][j]=='.'))
					continue;
				if((check(b[0][j],b[1][j],b[2][j],b[3][j])==1)) {
					found_winner=1;
					winner=(b[0][j]=='T')?b[1][j]:b[0][j];
					break;
				}
			}
		}
		//Diagonal1
		if(!found_winner) {
			if((b[0][0]!='.') && (b[1][1]!='.') && (b[2][2]!='.') && (b[3][3]!='.')) {
				if((check(b[0][0],b[1][1],b[2][2],b[3][3])==1)) {
					found_winner=1;
					winner=(b[0][0]=='T')?b[1][1]:b[0][0];
				}
			}
		}
		//Diagonal2
		if(!found_winner) {
			if((b[0][3]!='.') && (b[1][2]!='.') && (b[2][1]!='.') && (b[3][0]!='.')) {
				if((check(b[0][3],b[1][2],b[2][1],b[3][0])==1)) {
					found_winner=1;
					winner=(b[0][3]=='T')?b[1][2]:b[0][3];
				}
			}
		}
		
		if(found_winner) {
			fout<<"Case #"<<(count+1)<<": "<<winner<<" won\n";
		} else {
			if(game_over)
				fout<<"Case #"<<(count+1)<<": "<<"Draw\n";
			else
				fout<<"Case #"<<(count+1)<<": "<<"Game has not completed\n";
		}
		
		
	}
	
	return 0;
}
