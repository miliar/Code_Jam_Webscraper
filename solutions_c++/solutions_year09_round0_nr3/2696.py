#include<iostream>
using namespace std;

char p[20]="welcome to code jam";
char q[505];
int s,len;

void search(int num,int pos)
{
	int i;
	if(num==19){s=s+1;s=s%10000;return ;}
	for(i=pos+1;i<len;i++)
	{
		if(q[i]==p[num])
		{
			search(num+1,i);
		}
	}
	return ;
}
int main()
{
	int t,i,k=1;
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d",&t);
	getchar();
	while(t--)
	{
		cin.getline(q,505);
		s=0;
		len=strlen(q);
		for(i=0;i<len;i++)
		{
			if(q[i]=='w'){search(1,i);}
			
		}
		printf("Case #%d: ",k++);
		if(s<10)printf("000%d\n",s);
		else if(s<100)printf("00%d\n",s);
		else if(s<1000)printf("0%d\n",s);
		else if(s<10000)printf("%d\n",s);
	}
	return 0;
}