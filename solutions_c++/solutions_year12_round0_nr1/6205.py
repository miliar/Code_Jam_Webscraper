#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int n,i,j;
	char str[30][101];
	char output[30][101];
	
	cin >> n;
	for(i=0;i<n;i++){
		gets(str[i]);
	}	

	for(i=0;i<n;i++){
		j = 0;
		do{
			if(str[i][j] == ' ' || str[i][j] == '\0') output[i][j] = str[i][j];
			if(str[i][j] == 'y') output[i][j] = 'a';
			if(str[i][j] == 'n') output[i][j] = 'b';
			if(str[i][j] == 'f') output[i][j] = 'c';
			if(str[i][j] == 'i') output[i][j] = 'd';
			if(str[i][j] == 'c') output[i][j] = 'e';
			if(str[i][j] == 'w') output[i][j] = 'f';
			if(str[i][j] == 'l') output[i][j] = 'g';
			if(str[i][j] == 'b') output[i][j] = 'h';
			if(str[i][j] == 'k') output[i][j] = 'i';
			if(str[i][j] == 'u') output[i][j] = 'j';
			if(str[i][j] == 'o') output[i][j] = 'k';
			if(str[i][j] == 'm') output[i][j] = 'l';
			if(str[i][j] == 'x') output[i][j] = 'm';
			if(str[i][j] == 's') output[i][j] = 'n';
			if(str[i][j] == 'e') output[i][j] = 'o';
			if(str[i][j] == 'v') output[i][j] = 'p';
			if(str[i][j] == 'z') output[i][j] = 'q';
			if(str[i][j] == 'p') output[i][j] = 'r';
			if(str[i][j] == 'd') output[i][j] = 's';
			if(str[i][j] == 'r') output[i][j] = 't';
			if(str[i][j] == 'j') output[i][j] = 'u';
			if(str[i][j] == 'g') output[i][j] = 'v';
			if(str[i][j] == 't') output[i][j] = 'w';
			if(str[i][j] == 'h') output[i][j] = 'x';
			if(str[i][j] == 'a') output[i][j] = 'y';
			if(str[i][j] == 'q') output[i][j] = 'z';
			j++;

		}while(str[i][j] != '\0');
	}
	for(i=0;i<n;i++){
		cout<<"Case #"<<i<<": "<<output[i]<<endl;
	}
}
