/*
 TASK: B. Magicka
 LANG: C++
 by pasin30055
 */
#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX_T 105
#define MAX_N 105
#define MAX_C 40
#define MAX_D 35
#define MAX_L 10
#define MAX_CHAR 26

using namespace std;

int t,iii;
int n,i,j,k;
int c,d;
int en;
char com[MAX_CHAR][MAX_CHAR];
bool inv[MAX_CHAR][MAX_CHAR];
bool isv[MAX_CHAR][MAX_CHAR];
bool chk;
char in1[MAX_C][MAX_L],in2[MAX_D][MAX_L];
char in[MAX_N];
char st[MAX_N];

int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large-out.txt","w",stdout);
	scanf("%d",&t);
	for(iii=0;iii<t;iii++)
	{
		scanf("%d",&c);
		for(i=0;i<MAX_CHAR;i++)
		{
			for(j=0;j<MAX_CHAR;j++)
			{
				isv[i][j]=0;
				inv[i][j]=0;
			}
		}
		for(i=0;i<c;i++)
		{
			scanf("%s",in1[i]);
			com[in1[i][0]-'A'][in1[i][1]-'A']=in1[i][2];
			com[in1[i][1]-'A'][in1[i][0]-'A']=in1[i][2];
			isv[in1[i][0]-'A'][in1[i][1]-'A']=1;
			isv[in1[i][1]-'A'][in1[i][0]-'A']=1;
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",in2[i]);
			inv[in2[i][0]-'A'][in2[i][1]-'A']=1;
			inv[in2[i][1]-'A'][in2[i][0]-'A']=1;
		}
		scanf("%d",&n);
		scanf("%s",in);
		en=0;
		for(i=0;i<n;i++)
		{
			st[en]=in[i];
			en++;
			chk=1;
			while(chk)
			{
				chk=0;
				if(en>=2&&isv[st[en-1]-'A'][st[en-2]-'A'])
				{
					st[en-2]=com[st[en-1]-'A'][st[en-2]-'A'];
					en--;
					chk=1;
				}
			}
			for(j=0;j<en;j++)
			{
				for(k=0;k<en;k++)
				{
					if(inv[st[j]-'A'][st[k]-'A'])
					{
						en=0;
					}
				}
			}
		}
		printf("Case #%d: ",iii+1);
		printf("[");
		for(i=0;i<en;i++)
		{
			if(i!=0)
			{
				printf(", ");
			}
			printf("%c",st[i]);
		}
		printf("]\n");
	}
	return 0;
}
