#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

const int N=110;
char c[N][5], d[N][5], s[N];
int cn, dn, n, cas, cas1;

int main()
{
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int i, j, k, l, flag, tmp;
	scanf("%d", &cas);
	for(cas1=1; cas1<=cas; cas1++)
	{
		scanf("%d", &cn);
		for(i=0; i<cn; i++)
			scanf("%s", c[i]);
		scanf("%d", &dn);
		for(i=0; i<dn; i++)
			scanf("%s", d[i]);
		scanf("%d %s", &n, s);

		printf("Case #%d: [", cas1); //���ͷ����
		if(n==1)
		{
			printf("%s]\n", s);
			continue;
		}
		if(cn==0 && dn==0)
		{
			printf("%c", s[0]);
			for(i=1; i<n; i++)
				printf(", %c", s[i]);
			printf("]\n");
			continue;
		}

		// ����
		i = 1;
		while(i<n)
		{
			flag = 0;
			for(j=0; j<cn; j++) //��ĩβ������
			{
				if( (s[i]==c[j][0] && s[i-1]==c[j][1]) || (s[i-1]==c[j][0] && s[i]==c[j][1]) )
				{
					s[i-1] = c[j][2];
					for(k=i+1; k<n; k++)
						s[k-1] = s[k];
					n -= 1;
					//i;
					flag = 1;
					break;
				}
			}
			if(flag)
				continue;
			
			flag = 0;
			for(j=0; j<i; j++) //ö��ǰ������λ�á�����
			{
				for(k=0; k<dn; k++)
				{
					if( (s[i]==d[k][0] && s[j]==d[k][1]) || (s[j]==d[k][0] && s[i]==d[k][1]) )
					{
                        j = 0;
						tmp = i-j+1;
						for(l=i+1; l<n; l++)
							s[l-tmp] = s[l];
						n -= tmp;
						i = j;
						flag = 1;
						break;
					}
				}
				if(flag)
					break;
			}
			if(flag)
				continue;
			else
				i++;
		}

		//�������
		if(n==0)
		{
			printf("]\n");
			continue;
		}
		printf("%c", s[0]);
		for(i=1; i<n; i++) //ע��ı�nֵ����
			printf(", %c", s[i]);
		printf("]\n"); //���β������
	}


    //system("pause");
	return 0;
}
