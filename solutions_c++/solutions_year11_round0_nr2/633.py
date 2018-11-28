#include <iostream>
using namespace std;
int nc,nd,n;
int form[30][30];
int opp[30][30];
int appear[30];
char st[1000];
char res[1000];
void readin()
{
	scanf("%d",&nc);
	char buf[200];
	int i;
	memset(form,-1,sizeof(form));
	for(i = 0;i<nc;++i)
	{
		scanf("%s",buf);
		int a = buf[0] - 'A';
		int b= buf[1] - 'A';
		form[a][b] = form[b][a] = buf[2] -'A';
	}
	memset(opp,0,sizeof(opp));
	scanf("%d",&nd);
	for(i = 0;i<nd;++i)
	{
		scanf("%s",buf);
		int a = buf[0] -'A';
		int b = buf[1] -'A';
		opp[a][b] = opp[b][a] = true;
	}
	scanf("%d %s",&n,st);
	//getchar();
}
void work(int caseNum)
{
	int i,j;
	memset(appear,0,sizeof(appear));
	int ListNum = 0;
	for(i = 0;i<n;++i)
	{
		int  c = st[i] -'A';
		if(ListNum == 0)
		{
			++appear[c];
			res[ListNum++] = (char)(c+ 'A');
		}
		else
		{
			while(ListNum>0 && form[res[ListNum-1]-'A'][c]!=-1)
			{
				c = form[res[ListNum-1]-'A'][c];
				appear[res[ListNum-1]-'A']--;
				--ListNum;
			}
			for(j = 0;j<26;++j)
				if(appear[j]>0 && opp[c][j])
				{
					memset(appear,0,sizeof(appear));
					ListNum = 0;
					break;
				}
				if(j ==26)
				{
					res[ListNum++] =(char) (c + 'A');
					appear[c]++;
				}
		}
	}
	printf("Case #%d: ",caseNum);
	putchar('[');
	for(i = 0;i<ListNum;++i)
		if(i != ListNum-1)
			printf("%c, ",res[i]);
		else printf("%c",res[i]);
		printf("]\n");
}
int main()
{
	int tcase;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&tcase);
	int i;
	for(i = 1;i<=tcase;++i)
	{
		readin();
		work(i);
	}
	//fclose(stdin);

}