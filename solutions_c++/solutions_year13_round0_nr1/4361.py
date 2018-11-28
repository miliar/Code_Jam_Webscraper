#include<iostream>
#include<fstream>

using namespace std;

char a[5][4],c;
bool s,count;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.txt");
	
	int t,tt;
	int i,j,k;
	
	fin>>t;
	for(tt=1;tt<=t;++tt){
		for(i=0;i<4;i++){
			fin>>a[i]; 
		}

		//X winning
		for(i=0;i<4;i++){
			j=0;
			while(a[i][j]=='X'||a[i][j]=='T'){
				j++;
				if(j==4) goto Xwin;
			}
		}
		for(j=0;j<4;j++){
			i=0;
			while(a[i][j]=='X'||a[i][j]=='T'){
				i++;
				if(i==4) goto Xwin;
			}
		}
		
		i=j=0;
		while(a[i][j]=='X'||a[i][j]=='T'){
			i++;j++;
			if(i==4) goto Xwin;
		}
		i=3;j=0;
		while(a[i][j]=='X'||a[i][j]=='T'){
			i--;j++;
			if(j==4) goto Xwin;
		}

		//O winning
		for(i=0;i<4;i++){
			j=0;
			while(a[i][j]=='O'||a[i][j]=='T'){
				j++;
				if(j==4) goto Owin;
			}
		}
		for(j=0;j<4;j++){
			i=0;
			while(a[i][j]=='O'||a[i][j]=='T'){
				i++;
				if(i==4) goto Owin;
			}
		}
		
		i=j=0;
		while(a[i][j]=='O'||a[i][j]=='T'){
			i++;j++;
			if(i==4) goto Owin;
		}
		i=3;j=0;
		while(a[i][j]=='O'||a[i][j]=='T'){
			i--;j++;
			if(j==4) goto Owin;
		}


		//NC game
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(a[i][j]=='.') goto NC;
			}
		}

		fout<<"Case #"<<tt<<": Draw\n";continue;
		Xwin:fout<<"Case #"<<tt<<": X won\n";continue;
		Owin:fout<<"Case #"<<tt<<": O won\n";continue;
		NC:fout<<"Case #"<<tt<<": Game has not completed\n";continue;
	}
	
	return 0;
}