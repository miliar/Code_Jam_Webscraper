#include<iostream>
#include<string>
#include<istream>
using namespace std;

int main(){
	int n;
	string ans="";
	string que;
	char anss[100];
	cin>>n;
	getline(cin,que);
	for(int j=0;j<n;){
		ans="";
		getline(cin,que);
		int k=0;
		while(k < que.length()){
			char c=que[k];
			if(c=='a')ans+='y';//
			if(c=='b')ans+='h';//
			if(c=='c')ans+='e';//
			if(c=='d')ans+='s';//
			if(c=='e')ans+='o';//
			if(c=='f')ans+='c';//
			if(c=='g')ans+='v';//
			if(c=='h')ans+='x';//
			if(c=='i')ans+='d';//
			if(c=='j')ans+='u';//
			if(c=='k')ans+='i';//
			if(c=='l')ans+='g';//
			if(c=='m')ans+='l';//
			if(c=='n')ans+='b';//
			if(c=='o')ans+='k';//
			if(c=='p')ans+='r';//
			if(c=='q')ans+='z';//
			if(c=='r')ans+='t';//
			if(c=='s')ans+='n';//
			if(c=='t')ans+='w';//
			if(c=='u')ans+='j';//
			if(c=='v')ans+='p';//
			if(c=='w')ans+='f';//
			if(c=='x')ans+='m';//
			if(c=='y')ans+='a';//
			if(c=='z')ans+='q';//
			if(c==' ')ans+=' ';
			k++;
		}
		
		j++;
		cout<<"Case #"<<j<<": "<<ans<<endl;
		
	}
	return 0;
}
