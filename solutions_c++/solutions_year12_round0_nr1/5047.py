#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;

int main()
{
	int t;
	cin>>t;
	string s2;
	getline(cin,s2);
	map<char,char> m;
	char ch[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z']=  'q';
	
	for( int i=1; i<=t ; i++ ) {
		string s;
		string s2;
		getline(cin,s);
		
		//cout<<s<<endl;
		//cout<<"Case #"<<i<<": ";
		for(int j=0;j<s.size();j++) {
			if( s[j] == ' ' ) {
		//		cout<<" ";
				continue;
			//	s2 = s2 + s[j];
			}
			int num = (int)(char(s[j])-'a');
//			cout<<s[j]<<"  "<<ch[num];
//			cout<<"  "<<num<<" "<<endl;
			s[j] = ch[num];
		}
		s2=s;
		cout<<"Case #"<<i<<": "<<s2<<endl;	
//		cout<<endl;
	}
	
}
