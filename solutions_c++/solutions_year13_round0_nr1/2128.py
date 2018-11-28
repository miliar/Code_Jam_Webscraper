#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<iterator>
using namespace std;

inline int scan()
{
    int po=0;
    char ch;
    ch=getchar_unlocked();
    while(ch<'0' || ch>'9')
        ch=getchar_unlocked();
    while(ch>='0' && ch<='9')
    {
        po=(po<<3)+(po<<1)+ch-'0';
        ch=getchar_unlocked();
    }
    return po;
}


int xcnt, ocnt;


bool Win(char c, char **a) {
	int count = 0;
	int diagflag= 1;
	
	if(a[0][0] == c || a[0][0] == 'T') {
		for(int i=0; i<3; i++) {
			if(a[i+1][i+1] != c && a[i+1][i+1] != 'T') {
				diagflag = 0;
				break;
			}
		}
 	}
 	else diagflag = 0;
	if(diagflag) 
 		return true;	
 	if(a[0][3] == c || a[0][3] == 'T') {
 		diagflag = 1;
 		for(int i=2; i>=0; i--) {
 			if(a[3-i][i] != c && a[3-i][i] != 'T') {
 				diagflag = 0;
 				break;
 			}
 		}
 	}
 	else diagflag = 0;
 	if(diagflag) 
 		return true;
	
	for(int i=0; i<4; i++) {
		count = 0;
		if(a[i][0] == c || a[i][0] == 'T') {
			for(int j=1; j<4; j++) {
				if(a[i][j] == c || a[i][j] == 'T')
					++count;		
				else break;
			}
			if(count == 3) 
				return true;
		}		
	}
	
	for(int i=0; i<4; i++) {
		count = 0;
		if(a[0][i] == c || a[0][i] == 'T') {
			for(int j=1; j<4; j++) {
				if(a[j][i] == c || a[j][i] == 'T')
					++count;
				else break;
			
			}
			if(count == 3) 
				return true;
		}		
	}
	return false;
}

bool Draw(char **a) {
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if(a[i][j] == '.')
				return false;
	
	return true;
	
}

int main() {
	int test;
	test = scan();
	for(int t=0; t<test; t++) {	
		bool wonx, wono, draw, incomplete;
		wonx = wono = draw = incomplete = false;
		char **a = (char **)malloc(4*sizeof(char*));
		for(int i=0; i<4; i++)
			a[i] = (char*)malloc(4*sizeof(char));
		xcnt = ocnt = 0;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				cin>>a[i][j];
				if(a[i][j] == 'X')
					++xcnt;
				else if(a[i][j] == 'O')
					++ocnt;				
			}
		}
		if(xcnt>ocnt)
			wonx = Win('X', a);
		else if(xcnt==ocnt)
			wono = Win('O', a);
		
		if(!wonx && !wono)
			draw = Draw(a);
		
		if(!draw && !wonx && !wono)
			incomplete = true;
		
		if(wonx)
			cout<<"Case #"<<t+1<<": "<<"X won"<<endl;	
		else if(wono)
			cout<<"Case #"<<t+1<<": "<<"O won"<<endl;
		else if(incomplete)
			cout<<"Case #"<<t+1<<": "<<"Game has not completed"<<endl;
		else if(draw)
			cout<<"Case #"<<t+1<<": "<<"Draw"<<endl;
	}
	return 0;
}
