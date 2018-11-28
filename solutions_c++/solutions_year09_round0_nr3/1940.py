//2009Äê9ÔÂ3ÈÕ Google Code Jam
//Welcome to Code Jam
#include<iostream>
using namespace std;

struct CELL{
	char letter;
	int time;
	static int length;
};
int CELL::length = 0;

bool match(int p, char c);

int main()
{
	int N;
	char input[510];
	CELL cell[510];
	char no_use[2] ={};
	int pointer;
	int DP[20][500];//Dynamic Programming: the result is DP[0][0]%1000
	
	cin>>N;
	cin.getline(no_use, sizeof(no_use));
	for(int t=1; t<=N; t++){
		cin.getline(input, sizeof(input));
		
		cell[0].letter = input[0];
		cell[0].time = 1;
		CELL::length = 0;
		for(pointer = 1; input[pointer] != '\0'; pointer ++){
			if(input[pointer] == cell[CELL::length].letter)
				cell[CELL::length].time ++;
			else{
				cell[++ CELL::length].letter = input[pointer];
				cell[CELL::length].time = 1;
			}
		}
		
		memset(DP, 0, sizeof(DP));
		DP[18][CELL::length] = match(18, cell[CELL::length].letter) * cell[CELL::length].time;
		for(int c = CELL::length - 1; c>= 0; c--)
			DP[18][c] = (DP[18][c+1] + match(18, cell[c].letter) * cell[c].time)%1000;
		
		for(int p = 17; p>=0; p--){
			for(int c = CELL::length - (18 - p); c>=p; c--){
				DP[p][c] = (DP[p][c+1] + match(p, cell[c].letter) * cell[c].time * DP[p+1][c+1])%1000;
			}
		}
		
		cout<<"Case #"<<t<<": ";
		if(DP[0][0]<10) cout<<"000";
		else if(DP[0][0]<100) cout<<"00";
		else if(DP[0][0]<1000) cout<<"0";
		cout<<DP[0][0]<<endl;
	}
	return 0;
}

bool match(int p, char c)
{
	switch(p){
	case  0:return !(c-'w');
	case  1:return !(c-'e');
	case  2:return !(c-'l');
	case  3:return !(c-'c');
	case  4:return !(c-'o');
	case  5:return !(c-'m');
	case  6:return !(c-'e');
	case  7:return !(c-' ');
	case  8:return !(c-'t');
	case  9:return !(c-'o');
	case 10:return !(c-' ');
	case 11:return !(c-'c');
	case 12:return !(c-'o');
	case 13:return !(c-'d');
	case 14:return !(c-'e');
	case 15:return !(c-' ');
	case 16:return !(c-'j');
	case 17:return !(c-'a');
	case 18:return !(c-'m');
	}
	return false;
}
