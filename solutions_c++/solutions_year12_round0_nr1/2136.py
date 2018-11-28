#include <iostream>
using namespace std;
int main()
{
	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	char map[300];
	map['a']='y';
	map['b']='h';
	map['c']='e';
	map['d']='s';
	map['e']='o';
	map['f']='c';
	map['g']='v';
	map['h']='x';
	map['i']='d';
	map['j']='u';
	map['k']='i';
	map['l']='g';
	map['m']='l';
	map['n']='b';
	map['o']='k';
	map['p']='r';
	map['q']='z';
	map['r']='t';
	map['s']='n';
	map['t']='w';
	map['u']='j';
	map['v']='p';
	map['w']='f';
	map['x']='m';
	map['y']='a';
	map['z']='q';
	char str[200];
	int T;
	scanf("%d",&T);
	cin.getline(str,200);
	for(int i=0;i<T;i++)
	{
		cin.getline(str,200);
		int j=0;
		while(str[j]!='\n'&&str[j]!='\0')
		{
			if(str[j]>='a'&&str[j]<='z') str[j]=map[str[j]];
			j++;
		}
		printf("Case #%d: %s\n",i+1,str);
	}
		
}