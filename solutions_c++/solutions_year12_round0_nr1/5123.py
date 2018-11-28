#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int t;
	cin>>t;
	char temp[10];
	cin.getline(temp,10,'\n');
	for(int i=0;i<t;i++){
		char in[200];
		cin.getline(in,200,'\n');
		for(int j=0;j<strlen(in);j++){
			switch(in[j]){
				case 'a': in[j]='y';
					  break;
				case 'b': in[j]='h';
					  break;
				case 'c': in[j]='e';
					  break;
				case 'd': in[j]='s';
					  break;
				case 'e': in[j]='o';
					  break;
				case 'f': in[j]='c';
					  break;
				case 'g': in[j]='v';
					  break;
				case 'h': in[j]='x';
					  break;
				case 'i': in[j]='d';
					  break;
				case 'j': in[j]='u';
					  break;
				case 'k': in[j]='i';
					  break;
				case 'l': in[j]='g';
					  break;
				case 'm': in[j]='l';
					  break;
				case 'n': in[j]='b';
					  break;
				case 'o': in[j]='k';
					  break;
				case 'p': in[j]='r';
					  break;
				case 'q': in[j]='z';
					  break;
				case 'r': in[j]='t';
					  break;
				case 's': in[j]='n';
					  break;
				case 't': in[j]='w';
					  break;
				case 'u': in[j]='j';
					  break;
				case 'v': in[j]='p';
					  break;
				case 'w': in[j]='f';
					  break;
				case 'x': in[j]='m';
					  break;
				case 'y': in[j]='a';
					  break;
				case 'z': in[j]='q';
					  break;
			}
		}
		cout<<"Case #"<<i+1<<": "<<in<<endl;
	}
	return 0;
}	
