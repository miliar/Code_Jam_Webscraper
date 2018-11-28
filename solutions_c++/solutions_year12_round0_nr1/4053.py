#include<iostream>
#include<fstream>
#include<string>
using namespace std;

char in1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
char in2[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char in3[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
char out1[] = "our language is impossible to understand";
char out2[] = "there are twenty six factorial possibilities";
char out3[] = "so it is okay if you want to just give up";

char a[300];

int main()
{
	memset(a, 0, sizeof(a));
	for(int j = 0; j < strlen(in1); j++)
	{
		a[in1[j]] = out1[j];
	}
	for(int j = 0; j < strlen(in2); j++)
	{
		a[in2[j]] = out2[j];
	}
	for(int j = 0; j < strlen(in3); j++)
	{
		a[in3[j]] = out3[j];
	}
	a['y'] = 'a';
	a['e'] = 'o';
	a['q'] = 'z';
	a['z'] = 'q';
	ifstream ifin("A-small-attempt0.in");
	ofstream ofout("out.txt");
	int T;
	ifin>>T;
	string s;
	getline(ifin, s);
	for(int j = 1; j <= T; j++)
	{
		ofout<<"Case #"<<j<<": ";
		getline(ifin, s);

		for(int i = 0; i < s.length(); i++) ofout<<a[s[i]];
		ofout<<endl;
	}
	//char p[300];
	//memset(p, 0, sizeof(p));
	//for(char i = 'a'; i <= 'z'; i++) p[a[i]] = 1;
	//for(char i = 'a'; i <= 'z'; i++)
		//if(p[i] == 0) ofout<<i;
		//if(a[i] == 0) ofout<<i<<"--"<<a[i];
	ofout.close();
	return 0;
}