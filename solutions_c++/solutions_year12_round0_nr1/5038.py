
#include<iostream>
#include<string>
#include<cstring>

using namespace std;

int main() {
	char arr[150];
	arr['e']='o';arr['j']='u';arr['p']='r';arr['m']='l';arr['y']='a';arr['s']='n';arr['l']='g';arr['c']='e';arr['k']='i';arr['d']='s';arr['x']='m';arr['v']='p';arr['n']='b';arr['r']='t';arr['i']='d';arr['b']='h';arr['t']='w';arr['a']='y';arr['h']='x';arr['w']='f';arr['o']='k';arr['u']='j';arr['g']='v';arr['f']='c';arr['q']='z';arr['z']='q';
	int T;
	cin>>T;
	int x=T;
	string line;
	while(T) {
		
		getline(cin, line);
		int n = line.length();
		if(x==T) {x++; continue;}
		cout<<"Case #"<<x-T<<": ";
		for(int j=0; j<n; j++) {
			if(line[j]==' ') cout<<" ";
			else cout<<arr[line[j]];
		}
		cout<<endl;
		T--;
	}
	return 0;
}
