/*
 * main.cpp
 *
 *  Created on: 2013.04.13.
 *      Author: Peti
 */

#include<iostream>
#include<fstream>
#include<sstream>

using namespace std;

char test(char a, char b, char c, char d){
	if(a=='X' && b=='X' && c=='X' && d=='X'){return 'x';}
	if(b=='X' && c=='X' && d=='X' && a=='T'){return 'x';}
	if(a=='X' && c=='X' && d=='X' && b=='T'){return 'x';}
	if(a=='X' && b=='X' && d=='X' && c=='T'){return 'x';}
	if(a=='X' && b=='X' && c=='X' && d=='T'){return 'x';}
	if(a=='O' && b=='O' && c=='O' && d=='O'){return 'o';}
	if(b=='O' && c=='O' && d=='O' && a=='T'){return 'o';}
	if(a=='O' && c=='O' && d=='O' && b=='T'){return 'o';}
	if(a=='O' && b=='O' && d=='O' && c=='T'){return 'o';}
	if(a=='O' && b=='O' && c=='O' && d=='T'){return 'o';}
	if(a=='.' || b=='.' || c=='.' || d=='.'){return 'n';};
	return 't';
}


int main(){
	int t; //test cases
	int i,j;
	fstream in("A-large.in");
	fstream out("output.txt");
	in>>t;
	char tomb[t*4*4];
	char eredmeny[t];
	char ret;
	bool x,o,draw;

	for(i=0;i<t*4;i++){
		in>>tomb[(i*4)+0];
		in>>tomb[(i*4)+1];
		in>>tomb[(i*4)+2];
		in>>tomb[(i*4)+3];
	}

	for(j=0;j<t;j++){
		x=o=false;
		draw=true;
		for(i=0;i<4;i++){
			ret=test(tomb[(j*4*4)+i],tomb[(j*4*4)+i+4],tomb[(j*4*4)+i+8],tomb[(j*4*4)+i+12]);
			if(ret=='x'){x=true;}
			if(ret=='o'){o=true;}
			if(ret=='n'){draw=false;}
		}
		for(i=0;i<4;i++){
			ret=test(tomb[(j*4*4)+(i*4)+0],tomb[(j*4*4)+(i*4)+1],tomb[(j*4*4)+(i*4)+2],tomb[(j*4*4)+(i*4)+3]);
			if(ret=='x'){x=true;}
			if(ret=='o'){o=true;}
			if(ret=='n'){draw=false;}
		}
		ret=test(tomb[(j*4*4)+0],tomb[(j*4*4)+5],tomb[(j*4*4)+10],tomb[(j*4*4)+15]);
		if(ret=='x'){x=true;}
		if(ret=='o'){o=true;}
		if(ret=='n'){draw=false;}
		ret=test(tomb[(j*4*4)+3],tomb[(j*4*4)+6],tomb[(j*4*4)+9],tomb[(j*4*4)+12]);
		if(ret=='x'){x=true;}
		if(ret=='o'){o=true;}
		if(ret=='n'){draw=false;}
		if(x){
			eredmeny[j]='x';
		}else if(o){
			eredmeny[j]='o';
		}else if(draw){
			eredmeny[j]='d';
		}else{
			eredmeny[j]='n';
		}

	}

	for(j=0;j<t;j++){
		out<<"Case #"<<j+1<<": ";
		cout<<"Case #"<<j+1<<": ";
		switch(eredmeny[j]){
			case 'x':
				out<<"X won\n";
				cout<<"X won\n";
				break;
			case 'o':
				out<<"O won\n";
				cout<<"O won\n";
				break;
			case 'd':
				out<<"Draw\n";
				cout<<"Draw\n";
				break;
			case 'n':
				out<<"Game has not completed\n";
				cout<<"Game has not completed\n";
				break;
			default:
				break;
		}
	}
	return 0;
}




