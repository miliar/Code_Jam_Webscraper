#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
	char a[1150]="zqejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	char b[1150]="qzourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	char c[1150];
	int hash[1150];
	int n,k=1,i,j;
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	for(i=0;i<strlen(a);i++)
	{
		hash[a[i]-'0']=b[i]-'0';
	}
	scanf("%d",&n);
	getchar();
	while(n--)
	{
		gets(c);
	
		//cout<<strlen(a)<<endl;
		printf("Case #%d: ",k++);
		
		for(i=0;i<strlen(c);i++)
		{
			printf("%c",hash[c[i]-'0']+'0');
		}
		cout<<endl;
	}
}