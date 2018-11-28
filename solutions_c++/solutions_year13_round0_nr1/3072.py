// google jam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string.h>
#include <math.h>
#include <stdlib.h>

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,t=0;  //测试次数
	int i =0, j = 0, k = 0 , m = 0,n = 0,p = 0;
	int owon1 = 4 * 'O',owon2 = 3 *  'O' + 'T';
	int xwon1 = 4 * 'X',xwon2 = 3 *  'X' + 'T';
	int state = -1;//记录结果状态，-1初始状态,0未完成，1 Owin，2 Xwin，3 draw
	char tmp;
	char test[4][4];  //存储测试数据
	scanf("%d",&T);  //获取测试次数
	while(t++<T)
	{
		state = 3;
		while(1)
		{
			scanf("%c",&tmp);
			if( i == 16 )
			{
				for(j = 0;j<4;++j)
				{
					for(k = 0,i =0,m=0 ;k<4;k++)
					{
						i += test[j][k];
						m += test[k][j];
					}
					if(i == owon1 || i == owon2|| m == owon1 || m == owon2)
					{
						state = 1;
						break;
					}
					else if(i == xwon1 || i == xwon2|| m == xwon1 || m == xwon2)
					{
						state = 2;
						break;
					}
				}
				for(k=0,n=0,p=0;k<4;++k)
				{
					n +=test[k][k];
					p +=test[k][3-k];
				}
				if(n == owon1 || n == owon2|| p == owon1 || p == owon2)
				{
					state = 1;
				}
				else if(n == xwon1 || n == xwon2|| p == xwon1 || p == xwon2)
				{
					state = 2;
				}
				switch(state)
				{
				case 0:
					printf("Case #%d: Game has not completed\n",t);
					break;
				case 1:
					printf("Case #%d: O won\n",t);
					break;
				case 2:
					printf("Case #%d: X won\n",t);
					break;
				case 3:
					printf("Case #%d: Draw\n",t);
					break;
				default:
					printf("erro\n");
					break;
				}
				i = 0;
				break;
			}
			if( tmp == '.' || tmp == 'O' || tmp == 'T' || tmp == 'X')
			{
				if(tmp == '.')
				{
					state = 0;
				}
				test[i/4][i%4] = tmp;
				i ++ ;
			}
		}
	}
	return 0;
}

