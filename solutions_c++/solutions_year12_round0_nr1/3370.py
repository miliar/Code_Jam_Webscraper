#include<algorithm>
#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
#include<map>

using namespace std;

char func(char c)
{
	if(c=='a') return 'y';
	if(c=='b') return 'h';
	if(c=='c') return 'e';
	if(c=='d') return 's';
	if(c=='e') return 'o';
	if(c=='f') return 'c';
	if(c=='g') return 'v';
	if(c=='h') return 'x';
	if(c=='i') return 'd';
	if(c=='j') return 'u';
	if(c=='k') return 'i';
	if(c=='l') return 'g';
	if(c=='m') return 'l';
	if(c=='n') return 'b';
	if(c=='o') return 'k';
	if(c=='p') return 'r';
	if(c=='q') return 'z';
	if(c=='r') return 't';
	if(c=='s') return 'n';
	if(c=='t') return 'w';
	if(c=='u') return 'j';
	if(c=='v') return 'p';
	if(c=='w') return 'f';
	if(c=='x') return 'm';
	if(c=='y') return 'a';
	if(c=='z') return 'q';
	return ' ';
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	string s;int n;
	cin >> n;cin.ignore(100,'\n');
	for(int x=0;x<n;x++)
	{
		getline(cin,s);
		if(x)cout << endl;
		cout << "Case #" << x+1 << ": " ; 
		for(int i=0;i<s.length();i++)
			cout << func((char)(s[i]));
	}
	return 0;
}