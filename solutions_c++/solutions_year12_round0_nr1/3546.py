#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
using namespace std;
int main(){
	map<char,char> alpha;
	alpha['y']='a',alpha['n']='b',alpha['f']='c',alpha['i']='d',alpha['c']='e';
	alpha['w']='f',alpha['l']='g',alpha['b']='h',alpha['k']='i',alpha['u']='j';
	alpha['o']='k',alpha['m']='l',alpha['x']='m',alpha['s']='n',alpha['e']='o';
	alpha['v']='p',alpha['z']='q',alpha['p']='r',alpha['d']='s',alpha['r']='t';
	alpha['j']='u',alpha['g']='v',alpha['t']='w',alpha['h']='x',alpha['a']='y';
	alpha['q']='z';
	int test,l,k=1;
	char s[200],c;
	string output;
	scanf("%d",&test);
	getchar();
	while(test--){
		output="";
		while(true){
			c=getchar();
			if(c=='\n'||c==EOF)
				break;
			if(c==' ')
				output+=c;
			else
				output+=alpha[c];
		}
		printf("Case #%d: ",k++);
		cout<<output<<endl;
	}
	return 0;
}
