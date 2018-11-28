// B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <algorithm>
#include <windows.h>
#include <time.h>
using namespace std;
int T;
int R,C,D;
int W[500][500];
int sumRx[500][500];
int sumRy[500][500];
int _tmain(int argc, _TCHAR* argv[])
{
	SetCurrentDirectoryA("D:\\codejam\\2\\B\\B\\Debug");
	int T;
	FILE * fin = fopen("in.txt","r" );
	FILE * fout = fopen("out.txt" ,"w" );

	fscanf(fin,"%d",&T);
	for( int t = 1 ; t <= T ; t++ )
	{
		fscanf(fin,"%d%d%d",&R,&C,&D);
		for( int i = 0 ; i < R ; i++ )
		{
			char buff[500];
			fscanf(fin,"%s",buff);
			for( int j = 0 ; j < C ; j++ ) 
			{
				W[j][i] = buff[j]-'0';
			}
		}
		
		int ans = 2;
		for( int y = 0 ; y <= R-3 ; y++ )
		{
			if( y%20 == 0 ) printf("y:%d\n",y);
			for( int x = 0 ; x <= C-3 ; x++ )
			{
				int rx = 0 , ry = 0;
				int m = 0;
				for( int k = 1 ; k+x-1 < C && k+y-1 < R ; k++ )
				{
					for( int i = 0 ; i < k ; i++ )
					{
						rx += W[x+k-1][y+i]*(x+k-1);
						ry += W[x+k-1][y+i]*(y+i);
						m += W[x+k-1][y+i];
					}
					for( int i = 0 ; i < k-1 ; i++ )
					{
						rx += W[x+i][y+k-1]*(x+i);
						ry += W[x+i][y+k-1]*(y+k-1);
						m += W[x+i][y+k-1];
					}
					if( k > ans )
					{
						double checkrx = rx - W[x][y]*x - W[x][y+k-1]*x - W[x+k-1][y]*(x+k-1) - W[x+k-1][y+k-1]*(x+k-1);
						double checkry = ry - W[x][y]*y - W[x][y+k-1]*(y+k-1) - W[x+k-1][y]*y - W[x+k-1][y+k-1]*(y+k-1);
						double checkm = m - W[x][y] - W[x][y+k-1] - W[x+k-1][y] - W[x+k-1][y+k-1];
						if( checkm > 0 )
						{
							checkrx/=checkm;
							checkry/=checkm;
							if( abs( checkrx - ((double)(x+x+k-1))/2 ) < 0.000001 && abs( checkry - ((double)(y+y+k-1))/2 ) < 0.000001 )
							{
								ans = k;
							}
						}else
						{
							ans = k;
						}
					}
				}
			}
		}
		if( ans == 2 ) 
		{
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",t);
		}else{
			fprintf(fout,"Case #%d: %d\n" , t,ans );
		}
		
	printf("\n%d",clock());
	}
	return 0;
}

