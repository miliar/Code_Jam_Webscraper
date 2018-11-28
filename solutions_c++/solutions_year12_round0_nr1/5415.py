
#include<iostream>
#include<cstring>
using namespace std;

char d[26];
bool ar[26];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("1.txt","w",stdout);
	int i,l,j;
	d[25]='q';d['q'-'a']='z';
	char str[]="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	char temp[]="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	for(i=0;i<strlen(str);i++)
	d[str[i]-'a']=temp[i];
	int c;
	scanf("%d",&c);
	gets(str);
	int t=1;
	while(c--)
	{
		char sstr[11111];
		gets(sstr);
		for(i=0;i<strlen(sstr);i++)
		if(sstr[i]>='a'&&sstr[i]<='z')
		sstr[i]=d[sstr[i]-'a'];
		printf("Case #%d: ",t++);
		puts(sstr);
	}
}