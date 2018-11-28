#include<iostream>
#include<fstream>
using namespace std;

char check(char a){
	switch (a){
		
		case 'a':
			return 'y';
			break;
		case 'b':
			return 'h';
			break;
		case 'c':
			return 'e';
			break;
		case 'd':
			return 's';
			break;
		case 'e':
			return 'o';
			break;
		case 'f':
			return 'c';
			break;
		case 'g':
			return 'v';
			break;
		case 'h':
			return 'x';
			break;
		case 'i':
			return 'd';
			break;
		case 'j':
			return 'u';
			break;
		case 'k':
			return 'i';
			break;
		case 'l':
			return 'g';
			break;
		case 'm':
			return 'l';
			break;
		case 'n':
			return 'b';
			break;
		case 'o':
			return 'k';
			break;
		case 'p':
			return 'r';
			break;
		case 'q':
			return 'z';
			break;
		case 'r':
			return 't';
			break;
		case 's':
			return 'n';
			break;
		case 't':
			return 'w';
			break;
		case 'u':
			return 'j';
			break;
		case 'v':
			return 'p';
			break;
		case 'w':
			return 'f';
			break;
		case 'x':
			return 'm';
			break;
		case 'y':
			return 'a';
			break;
		case 'z':
			return 'q';
			break;
		
	}

}
int main(){

	ifstream infile;
	ofstream outfile("output.in");
	infile.open("A-small-attempt3.in");
	int cse;
	char b[1];
	infile>>cse;
	infile.getline(b,1,'\n');
	for(int z=0;z<cse;z++){
	char* a;
	
	a = new char[999999];
	
	int i=0;
	infile.getline(a,999999,'\n');
	
	outfile<<"Case #"<<z+1<<": ";
	while(a[i]!='\0'){
		
		outfile<<check(a[i]);
		cout<<check(a[i]);
		i++;
	}
	
			
	outfile<<'\n';
	cout<<'\n';}
	system("pause");
}
