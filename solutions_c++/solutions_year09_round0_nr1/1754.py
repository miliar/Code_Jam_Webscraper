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
			//û���ҵ�
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
	//������������
	for(i = 0;i < N;i++)
	{
		memset(dis,0,sizeof(dis));
		memset(ndis,0,sizeof(ndis));
		total = 0;
		//flagΪ0��ʾ��������ݵ�һС��Ŀ�ʼ
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
				//�������м䲿��
				if(flag == 1)
				{
					dis[j][k] = c;
					k++;
				}
				//�ǵ�����һ����
				else
				{
					dis[j][0] = c;
					ndis[j++] = 1;
				}
			}
			else if(c == ')')
			{
				//���Ų��ֽ���
				flag = 0;
				ndis[j++] = k;
				k = 0;
			}
		}
		//�������
		
		//ÿһ��������ַ��� �ֳ�n_group�� ÿһ����ndis[]����ĸ
		total = 0;
		find();
		printf("Case #%d: %d\n",i+1,total);
	}
	return 0;
}
