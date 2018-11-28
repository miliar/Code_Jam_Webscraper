/* vi: set sw=4 ts=4: */
//
////  main.cpp
////  Codejam2013
////
////  Created by hams on 13. 4. 13..
////  Copyright (c) 2013년 hams. All rights reserved.
////
//
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <math.h>

#define MAX_BOUND (4)
#define MIN(a,b) (a > b ? b:a)
#define MAX(a,b) (a > b ? a:b)

void init(char lawn[4][4]){
	int ni,nj;
	for(ni=0; ni < MAX_BOUND;++ni){
		for(nj=0; nj < MAX_BOUND; ++nj){
			lawn[ni][nj] = '.';
		}
	}	
}

void draw(char lawn[4][4]){
	for(int ni=0; ni < 4; ++ni){
		for(int nj=0; nj < 4; ++nj){
				printf("%c ",(char)lawn[ni][nj]);
		}
		printf("\n");
	}
}

bool bingo(char map[4][4],char who){
	bool bwin = true;
	//printf("bingo:%c\n",who);
	for(int ni=0; ni < 4; ++ni){
		bwin = true;
		for(int nj=0; nj < 4;++nj){
			//printf("%c ",map[ni][nj]);
			if(map[ni][nj] != who && map[ni][nj] != 'T'){
				bwin = false;
				//printf("row:%d:false\n",ni);
				break;
			}
		}
		if(bwin == true) return true;
		bwin=true;
		for(int nj=0; nj < 4;++nj){
			//printf("%c ",map[nj][ni]);
			if(map[nj][ni] != who && map[nj][ni] != 'T'){
				bwin = false;
				//printf("col:%d:false\n",ni);
				break;
			}
		}
		if(bwin == true) return true;
	}

	bwin = true;
	for(int ni=0; ni < 4; ++ni){
		if(map[ni][ni] != who && map[ni][ni] != 'T'){
			bwin = false;
			break;
		}
	}
	if(bwin == true) return true;

	bwin = true;
	for(int ni=0; ni < 4; ++ni){
		if(map[ni][3-ni] != who && map[ni][3-ni] != 'T'){
			bwin = false;
			break;
		}
	}
	if(bwin == true) return true;
	return false;
}	


int main(){
	char  map[4][4] = {0,};
	int xcount,ocount,scount,tcount;
	int T=0; 
	scanf("%d",&T);
	for(int nloop=0; nloop < T; ++nloop){
		init(map);

		xcount=ocount=scount=tcount=0;
		for(int ni=0; ni < 4;++ni){
			scanf("%s",map[ni]);
		}
		for(int ni=0; ni < 4;++ni){
			for(int nj=0; nj < 4;++nj){
		//		scanf("%c",&map[ni][nj]);
				if(map[ni][nj] == 'X')
					xcount++;
				else if(map[ni][nj] == 'O')
					ocount++;
				else if(map[ni][nj] == 'T')
					tcount++;
				else if(map[ni][nj] == '.')
					scount++;
			}
		}
		//draw(map);
		if(bingo(map,'X') == true)
			printf("Case #%d: X won\n",nloop+1);
		else if(bingo(map,'O') == true)
			printf("Case #%d: O won\n",nloop+1);
		else if(scount == 0)
			printf("Case #%d: Draw\n",nloop+1);
		else 
			printf("Case #%d: Game has not completed\n",nloop+1);
	}
}
