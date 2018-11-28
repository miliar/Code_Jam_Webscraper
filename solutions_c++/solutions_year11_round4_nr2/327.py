#include<cstdio>
#include<iostream>


using namespace std;
int map[600][600];
long long  zhongx[600][600]={0},zhongy[600][600]={0}, part[600][600]={0};

bool calc(int a,int b, int c){
	int midx, midy;
	if(c %2==1){
		midx = (a+c/2)*2;
		midy = (b+c/2)*2;
	}
	else {
		midx = a*2+c-1;
		midy = b*2+c-1;
	}
	
	long long pp = part[a+c-1][b+c-1] -part[a-1][b+c-1] - part[a+c-1][b-1] + part[a-1][b-1];
	long long xx = zhongx[a+c-1][b+c-1] -zhongx[a-1][b+c-1] - zhongx[a+c-1][b-1] + zhongx[a-1][b-1];
	long long yy = zhongy[a+c-1][b+c-1] -zhongy[a-1][b+c-1] - zhongy[a+c-1][b-1] + zhongy[a-1][b-1];	
	pp -= map[a][b];
	pp -= map[a][b+c-1];
	pp -= map[a+c-1][b];
	pp -= map[a+c-1][b+c-1];
	xx -= map[a][b] * a;
	xx -= map[a][b+c-1] * a;
	xx -= map[a+c-1][b] * (a+c-1);
	xx -= map[a+c-1][b+c-1] *(a+c-1);
	yy -= map[a][b] * b;
	yy -= map[a][b+c-1] * (b+c-1);
	yy -= map[a+c-1][b] * b;
	yy -= map[a+c-1][b+c-1]*(b+c-1);
	if(2 * xx - pp * midx == 0 && 2*yy-pp * midy == 0)return true;
	return false;
}
void work(int x)
{

	int R,C,D;
	printf("Case #%d: ",x);
	cin >> R >> C >> D;
	for(int i = 1; i <= R; i++){
		string s;
		cin >> s;
		for(int j = 1; j <= C; j++){
			map[i][j] = s[j-1]-'0';
			zhongx[i][j] = zhongx[i-1][j]+ zhongx[i][j-1] -zhongx[i-1][j-1];
			zhongx[i][j] += map[i][j] * i;
			zhongy[i][j] = zhongy[i-1][j]+ zhongy[i][j-1] -zhongy[i-1][j-1];
			zhongy[i][j] += map[i][j] * j;
			part[i][j] =  part[i-1][j] + part[i][j-1] - part[i-1][j-1];
			part[i][j] += map[i][j];
		}
	}
//	printf("readdone\n");
	int max = -1;
	for(int i= 1; i<=R; i++)
		for(int j=1; j<=C; j++)
			for(int k = 3; i+k-1 <=R && j+k-1 <=C; k++){
				if(k> max && calc(i,j,k)){
					max = k;
				}
			}
	if(max!=-1)printf("%d\n", max);
	else printf("IMPOSSIBLE\n");
/*	printf("part\n");
	for(int i =1; i<=R; i++){
		for(int j = 1; j <=C; j++)
			printf("%d ", part[i][j]);
		printf("\n");
	}
	printf("zhongx\n");
	for(int i =1; i<=R; i++){
		for(int j = 1; j <=C; j++)
			printf("%d ", zhongx[i][j]);
		printf("\n");
	}
	printf("zhongy\n");
	for(int i =1; i<=R; i++){
		for(int j = 1; j <=C; j++)
			printf("%d ", zhongy[i][j]);
		printf("\n");
		}*/

}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)work(i);
}
