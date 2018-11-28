#include<iostream>
#include<string>

using namespace std;

int main(){
	
	char mapping[128];
	mapping['a']='y';
	mapping['b']='h';
	mapping['c']='e';
	mapping['d']='s';
	mapping['e']='o';
	mapping['f']='c';
	mapping['g']='v';
	mapping['h']='x';
	mapping['i']='d';
	mapping['j']='u';
	mapping['k']='i';
	mapping['l']='g';
	mapping['m']='l';
	mapping['n']='b';
	mapping['o']='k';
	mapping['p']='r';
	mapping['q']='z';
	mapping['r']='t';
	mapping['s']='n';
	mapping['t']='w';
	mapping['u']='j';
	mapping['v']='p';
	mapping['w']='f';
	mapping['x']='m';
	mapping['y']='a';
	mapping['z']='q';
	mapping[' ']=' ';
	mapping['\n']='\n';
	mapping['\0']='\0';
	
	int T;
	cin>>T;
	string s;
	getline(cin,s);
	for(int tc=1;tc<=T;tc++){
		string str;
		getline(cin,str);
		for(int i=0;i<str.size();i++)
			if(str[i]!='\0'||str[i]!='\n')
				str[i]=mapping[str[i]];
		
		cout<<"Case #"<<tc<<": "<<str<<endl;
		
	}
	
	return 0;
}
