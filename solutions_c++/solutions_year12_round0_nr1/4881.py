#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int main(int argc, char *argv[]) {
	int casos;
	map<char,char> maping;
	maping['y']='a';
	maping['q']='z';
	maping['e']='o';
	maping['j']='u';
	maping['p']='r';
	maping['m']='l';
	maping['s']='n';
	maping['l']='g';  //    q 
	maping['c']='e';
	maping['k']='i';
	maping['x']='m';
	maping['v']='p';
	maping['n']='b';
	maping['r']='t';
	maping['i']='d';
	maping['b']='h';
	maping['t']='w';
	maping['h']='x';
	maping['w']='f';
	maping['d']='s';
	maping['g']='v';
	maping['u']='j';
	maping['o']='k';
	maping['f']='c';
	maping['a']='y';
	maping['z']='q';
	maping[' ']=' ';
	freopen( "googlerese.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	cin>>casos;
	cin.ignore();
	
	for(int i=0;i<casos;i++){
		cout<<"Case #"<<i+1<<": ";
		char aux;
		aux=getchar();
		while(aux!='\n' ){
			
		maping.find(aux);
		cout<<(*(maping.find(aux))).second;
		aux=getchar();
		}
		cout<<"\n";
	}
	
	return 0;
}
