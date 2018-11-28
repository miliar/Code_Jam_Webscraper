//Code Jam 2012 A 
#include<iostream>
#include<cstring>
using namespace std;
char str[1200];
char map[26];
void init()
{
	map[0]='y';
	map[1]='h';
	map[2]='e';
	map[3]='s';
	map[4]='o';
	map[5]='c';
	map[6]='v';
	map[7]='x';
	map[8]='d';
	map[9]='u';
	map[10]='i';
	map[11]='g';
	map[12]='l';
	map[13]='b';
	map[14]='k';
	map[15]='r';
	map[16]='z';
	map[17]='t';
	map[18]='n';
	map[19]='w';
	map[20]='j';
	map[21]='p';
	map[22]='f';
	map[23]='m';
	map[24]='a';
	map[25]='q';
}

int main(){
	int T,l,p,pnew;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin>>T;
	cin.getline(str,1200);
	init();
	for(int cnt=1;cnt<=T;cnt++)
	{
		cin.getline(str,1200);
		l=strlen(str);
		cout<<"Case #"<<cnt<<": ";
		for(int i=0;i<l;i++)
		{
			if(str[i]==' ')
				cout<<" ";
			else
				cout<<map[str[i]-'a'];
		}
		cout<<endl;
	}
	return 0;
}
 
