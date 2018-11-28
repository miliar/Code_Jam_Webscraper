#include<cstdio>
#include<cstdlib>
#include<map>
#include<cstring>
using namespace std;



int main()
{
	map<char,char> trans;

	trans['a']='y';
	trans['b']='h';
	trans['c']='e';
	trans['d']='s';
	trans['e']='o';
	trans['f']='c';
	trans['g']='v';
	trans['h']='x';
	trans['i']='d';
	trans['j']='u';
	trans['k']='i';
	trans['l']='g';
	trans['m']='l';
	trans['n']='b';
	trans['o']='k';
	trans['p']='r';
	trans['q']='z';
	trans['r']='t';
	trans['s']='n';
	trans['t']='w';
	trans['u']='j';
	trans['v']='p';
	trans['w']='f';
	trans['x']='m';
	trans['y']='a';
	trans['z']='q';
	trans[' ']=' ';
	
	
	char s[110];
	int t;
	int count=1;
	scanf("%d",&t);
	char p=getchar();	
	while(t--)
	{	
		scanf("%[^\n]",s);
		int n=strlen(s);
		printf("Case #%d: ",count++);
		for(int i=0;i<n;i++)
			printf("%c",trans[s[i]]);
		printf("\n");		
		p=getchar();
			
	}	
	return 0;
}
