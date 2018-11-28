#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char alien[5001][16];
char dis[16][27];
int  ndis[16];
int total,L,D,N;

void find()
{
	int i,j,k;
	for(i = 0;i < D;i++)
	{
		for(j = 0;j < L;j++)
		{
			for(k = 0;dis[j][k] != 0;k++)
			{
				if(alien[i][j] == dis[j][k])
					break;
			}
			//没有找到
			if(dis[j][k] == 0)
				break;
		}
		if(j == L)
			total++;
	}
}

int main()
{
	int i,j,k;
	int flag;
	char c;
	
	freopen("A-large.in","r",stdin);
	freopen("data.txt","w",stdout);
	
	
	scanf("%d %d %d",&L,&D,&N);
	getchar();
	for(i = 0;i < D;i++)
		scanf("%s",alien[i]);
	getchar();
	//输入待检测数据
	for(i = 0;i < N;i++)
	{
		memset(dis,0,sizeof(dis));
		memset(ndis,0,sizeof(ndis));
		total = 0;
		//flag为0表示待检测数据的一小组的开始
		flag = 0; 
		j = 0;
		k = 0;
		while((c = getchar()) != '\n' )
		{
			if(c == '(')
			{
				k = 0;
				flag = 1;
			}
			else if(c >= 'a' && c <= 'z')
			{
				//是括号中间部分
				if(flag == 1)
				{
					dis[j][k] = c;
					k++;
				}
				//是单独的一部分
				else
				{
					dis[j][0] = c;
					ndis[j++] = 1;
				}
			}
			else if(c == ')')
			{
				//括号部分结束
				flag = 0;
				ndis[j++] = k;
				k = 0;
			}
		}
		//输入结束
		
		//每一个待检测字符串 分成n_group组 每一组有ndis[]个字母
		total = 0;
		find();
		printf("Case #%d: %d\n",i+1,total);
	}
	return 0;
}
