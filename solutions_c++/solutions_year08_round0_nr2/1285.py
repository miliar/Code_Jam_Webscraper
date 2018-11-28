#include<stdio.h>
#include<string.h>

typedef struct
{
	int hr , mn;
}pack;

pack ana[105][2] , anb[105][2];
bool flag[105];

bool gt(int x1 , int y1 , int x2 , int y2)
{
	if(x1 > x2) return true;
	if(x1 == x2 && y1 >= y2) return true;
	return false;
}

bool less(int x1 , int y1 , int x2 , int y2)
{
	if(x1 < x2) return true;
	if(x1 == x2 && y1 < y2) return true;
	return false;
}

int main()
{
	freopen("BB.in" , "r" , stdin);
	freopen("BB.out" , "w" , stdout);
	int test , na , nb , i , t , kase = 1 , j;
	scanf("%d" , &test);
	while(test--)
	{
		scanf("%d" , &t);
		scanf("%d%d" , &na , &nb);
		for(i = 0;i<na;i++)
			scanf("%d:%d %d:%d" , &ana[i][0].hr , &ana[i][0].mn , &ana[i][1].hr , &ana[i][1].mn);
		for(i = 0;i<nb;i++)
			scanf("%d:%d %d:%d" , &anb[i][0].hr , &anb[i][0].mn , &anb[i][1].hr , &anb[i][1].mn);
		int reta , retb , x , y;
		reta = na;retb = nb;
		//for B
		memset(flag , false , sizeof(flag));
		for(i = 0;i<na;i++){
			x = ana[i][1].hr;
			y = ana[i][1].mn;
			y += t;
			if(y > 59){
				x++;
				y%=60;
			}
			if(x > 23) continue;
			int mx = 24 , my = 60 , l = -1;
			for(j = 0;j<nb;j++){
				if(flag[j]) continue;
				if(gt(anb[j][0].hr , anb[j][0].mn , x , y) && less(anb[j][0].hr , anb[j][0].mn , mx , my)){
					mx = anb[j][0].hr;
					my = anb[j][0].mn;
					l = j;
				}
			}
			if(l != -1){
				flag[l] = true;
				retb--;
			}
		}
		//for A
		memset(flag , false , sizeof(flag));
		for(i = 0;i<nb;i++){
			x = anb[i][1].hr;
			y = anb[i][1].mn;
			y += t;
			if(y > 59){
				x++;
				y%=60;
			}
			if(x > 23) continue;
			int mx = 24 , my = 60 , l = -1;
			for(j = 0;j<na;j++){
				if(flag[j]) continue;
				if(gt(ana[j][0].hr , ana[j][0].mn , x , y) && less(ana[j][0].hr , ana[j][0].mn , mx , my)){
					mx = ana[j][0].hr;
					my = ana[j][0].mn;
					l = j;
				}
			}
			if(l != -1){
				flag[l] = true;
				reta--;
			}
		}
		printf("Case #%d: %d %d\n" , kase++ , reta , retb);
	}
	return 0;
}
