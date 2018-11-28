#include <cstdio>
using namespace std;

char tab[26];
int n,i,j,k;
char buffer[128];
char a;
bool czy;

int main()
{
	tab[0]='y';
	tab[1]='h';
	tab[2]='e';
	tab[3]='s';
	tab[4]='o';
	tab[5]='c';
	tab[6]='v';
	tab[7]='x';
	tab[8]='d';
	tab[9]='u';
	tab[10]='i';
	tab[11]='g';
	tab[12]='l';
	tab[13]='b';
	tab[14]='k';
	tab[15]='r';
	tab[16]='z';
	tab[17]='t';
	tab[18]='n';
	tab[19]='w';
	tab[20]='j';
	tab[21]='p';
	tab[22]='f';
	tab[23]='m';
	tab[24]='a';
	tab[25]='q';
	scanf("%d",&n);
	scanf("%c",&a);
	for(i=0;i<n;++i)
	{
		
		j=0;
		czy=1;
		while(czy)
		{
			scanf("%c",&a);
			if((a=='\n')||(a==EOF)) {czy=0;;}
			else {buffer[j]=a; ++j;}
		}
		printf("Case #%d: ",(i+1));
		for(k=0;k<j;++k)
		{
			if(buffer[k]==' ') {printf(" ");}
			else{printf("%c",tab[buffer[k]-97]);}
		}
		printf("\n");
	}
	
	return 0;
}
