#include<iostream>
#include<string>
using namespace std;

char principle[26];


string trans(string str)
{
	string outstr;
	for (int i=0; i<str.length();++i)
	{
		if(str[i]!=' ')
		    outstr.push_back( principle[str[i]-97]);
		else 
			outstr.push_back(' ');
	}
	return outstr;
}
int main(){
	freopen("A-small-attempt7.in", "r", stdin);    freopen("A-small-attempt1.out", "w", stdout);
	principle[0]='y';
	principle[1]='h';
	principle[2]='e';
	principle[3]='s';
	principle[4]='o';
	principle[5]='c';
	principle[6]='v';
	principle[7]='x';
	principle[8]='d';
	principle[9]='u';
	principle[10]='i';
	principle[11]='g';
	principle[12]='l';
	principle[13]='b';
	principle[14]='k';
	principle[15]='r';
	principle[16]='z';
	principle[17]='t';
	principle[18]='n';
	principle[19]='w';
	principle[20]='j';
	principle[21]='p';
	principle[22]='f';
	principle[23]='m';
	principle[24]='a';
	principle[25]='q';

	int count=0;
	
	string str;
	cin>>count;
	string mystr[100];
	for(int i=0; i<=count;++i)
	{
		
		getline(cin,str);
		mystr[i]= trans(str);
		
	}

	for(int i=1; i<=count;++i)
	{
		cout<<"Case #"<<i<<": "<<mystr[i]<<endl;
	}
	return 0;
}