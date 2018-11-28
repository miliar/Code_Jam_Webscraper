#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

int main()
{

	char arr[200];
	arr['a']='y';
	arr['b']='h';
	arr['c']='e';
	arr['d']='s';
	arr['e']='o';
	arr['f']='c';
	arr['g']='v';
	arr['h']='x';
	arr['i']='d';
	arr['j']='u';
	arr['k']='i';
	arr['l']='g';
	arr['m']='l';
	arr['n']='b';
	arr['o']='k';
	arr['p']='r';
	arr['q']='z';
	arr['r']='t';
	arr['s']='n';
	arr['t']='w';
	arr['u']='j';
	arr['v']='p';
	arr['w']='f';
	arr['x']='m';
	arr['y']='a';
	arr['z']='q';
	arr[' ']=' ';
	int n,i,j,l;
	char ch,str[1000],new_str[1000];
	cin>>n;
	scanf("%c",&ch);
	for(i=1;i<=n;i++)
	{
		scanf("%[^\n]",str);
		scanf("%c",&ch);
	//	cout<<str<<endl;
		int l=strlen(str);
		for(j=0;j<l;j++)
		{
			new_str[j]=arr[str[j]];
		}
		new_str[l]='\0';
		cout<<"Case #"<<i<<": "<<new_str<<endl;
	}
	return 0;
}

