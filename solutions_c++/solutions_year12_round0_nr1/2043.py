#include<stdio.h>

char change(char ch)
{
	if(ch == 97)
	{return 'y';}
	else if(ch == 'b'){return 'h';}
	else if(ch == 'c'){return 'e';}
	else if(ch == 'd'){return 's';}
	else if(ch == 'e'){return 'o';}
	else if(ch == 'f'){return 'c';}
	else if(ch == 'g'){return 'v';}
	else if(ch == 'h'){return 'x';}
	else if(ch == 'i'){return 'd';}
	else if(ch == 'j'){return 'u';}
	else if(ch == 'l'){return 'g';}
	else if(ch == 'k'){return 'i';}
	else if(ch == 'm'){return 'l';}
	else if(ch == 'n'){return 'b';}
	else if(ch == 'o'){return 'k';}
	else if(ch == 'p'){return 'r';}
	else if(ch == 'q'){return 'z';}
	else if(ch == 'r'){return 't';}
	else if(ch == 's'){return 'n';}
	else if(ch == 't'){return 'w';}
	else if(ch == 'u'){return 'j';}
	else if(ch == 'v'){return 'p';}
	else if(ch == 'w'){return 'f';}
	else if(ch == 'x'){return 'm';}
	else if(ch == 'y'){return 'a';}
	else
		return 'q';
}

int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("A.out","w",stdout);
	int n,j,i,k;
	char s[110];
	char ch;
	scanf("%d",&n);
	getchar();
	for(k=1;k<=n;k++)
	{
		j=1;
		while((ch=getchar())!='\n')
		{
			if(ch != ' ')
			    ch = change(ch);
			s[j]=ch;
			j++;
		}
		printf("Case #%d: ",k);
		for(i=1;i<j;i++)
			printf("%c",s[i]);
		printf("\n");
	}
	return 0;
}
/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
 
*/