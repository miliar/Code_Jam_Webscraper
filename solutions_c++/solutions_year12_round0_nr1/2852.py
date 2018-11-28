#include<cstdio>
#include<map>
using namespace std;
map<char,char> M;
void init()
{
	M['a']='y';
	M['b']='h';
	M['c']='e';
	M['d']='s';
	M['e']='o';
	M['f']='c';
	M['g']='v';
	M['h']='x';
	M['i']='d';
	M['j']='u';
	M['k']='i';
	M['l']='g';
	M['m']='l';
	M['n']='b';
	M['o']='k';
	M['p']='r';
	M['q']='z';
	M['r']='t';
	M['s']='n';
	M['t']='w';
	M['u']='j';
	M['v']='p';
	M['w']='f';
	M['y']='a';
	M['x']='m';
	M['z']='q';
	M[' ']=' ';
	M['\n']='\n';
}
int main()
{
	init();
	int ca;
	char c;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("ansA.out","w",stdout);
	scanf("%d",&ca);
	getchar();
	for(int ii=1;ii<=ca;ii++)
	{
		printf("Case #%d: ",ii);
		while(c=getchar())
		{
			putchar(M[c]);
			if(c=='\n')break;
		}
	}
	return 0;
}