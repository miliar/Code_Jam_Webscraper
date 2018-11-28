/*
 * A.cpp
 *
 *  Created on: 2010/06/05
 *      Author: jun
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int t,T;
	int i,j;
	scanf("%d\n",&T);
	for (t=0;t<T;t++){
		int k;
		scanf("%d\n",&k);
		char tarr[k*k];
		char arr[k][k];
		char invA[k][k],invB[k][k];
		int s1=1,s2=0;
		int x,y,xysum;
		xysum=0;x=0;y=0;
		for (i=0;i<k*k;i++){
			char c;
			scanf("%c ",&c);
			arr[x][y]=c;
			if (y==0 || x==k-1){
				xysum++;
				if (xysum<k){
					y=xysum;x=0;
				}
				else{
					y=k-1;x=xysum-k+1;
				}
			}
			else{
				x++;y--;
			}
		}
		for (i=0;i<k;i++){
			for (j=0;j<k;j++){
				invA[j][i]=arr[i][j];
				invB[j][i]=arr[k-1-i][k-1-j];
			}
		}
		/*printf("A%d\n",k);
		for (i=0;i<k;i++){
			for (j=0;j<k;j++){
				printf("%c ",arr[j][i]);
			}
			printf("\n");
		}
		printf("B%d\n",k);
		for (i=0;i<k;i++){
			for (j=0;j<k;j++){
				printf("%c ",invA[j][i]);
			}
			printf("\n");
		}
		printf("C%d\n",k);
		for (i=0;i<k;i++){
			for (j=0;j<k;j++){
				printf("%c ",invB[j][i]);
			}
			printf("\n");
		}*/
		int offset;
		int distA=-1,distB=-1;
		for (offset=-k+1;offset<=k-1;offset++){
			int ok_flag=1;
			for (i=0;i<k;i++){
				for (j=0;j<k;j++){
					int nx,ny;
					nx=j-offset;
					ny=i+offset;
					if (0<=nx && nx<k && 0<=ny && ny<k){
						if (arr[j][i]!=invA[nx][ny]){
							ok_flag=0;
						}
					}
				}
			}
			if (ok_flag){
				int d=(offset>0)?offset:-offset;
				if (distA<0 || distA>d)distA=d;
			}
		}
		//printf("D%d\n",distA);
		for (offset=-k+1;offset<=k-1;offset++){
			int ok_flag=1;
			for (i=0;i<k;i++){
				for (j=0;j<k;j++){
					int nx,ny;
					nx=j-offset;
					ny=i-offset;
					if (0<=nx && nx<k && 0<=ny && ny<k){
						if (arr[j][i]!=invB[nx][ny]){
							ok_flag=0;
						}
					}
				}
			}
			if (ok_flag){
				int d=(offset>0)?offset:-offset;
				if (distB<0 || distB>d)distB=d;
			}
		}
		//printf("E%d\n",distB);
		int newk;
		newk=k+distA+distB;
		printf("Case #%d: %d\n",t+1,newk*newk-k*k);
	}
	return 0;
}
