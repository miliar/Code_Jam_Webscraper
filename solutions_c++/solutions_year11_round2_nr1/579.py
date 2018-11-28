#include<cstdio>
#include<queue>
#include<vector>
#include<string>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<set>

// freopen("1.in","r",stdin);
// freopen("1.out","w",stdout);

using namespace std;
int n;
char map[110][110];
double wp[110];
double owp[110];
double oowp[110];
void getwp()
{
	int one,sum;
	for(int i = 0 ; i < n; i ++){
		one = sum = 0;
		for(int j =  0; j < n; j ++){
			if(map[i][j] == '1'){
				one ++;
				sum ++;
			}
			else if(map[i][j] == '0')
				sum++;
		}
		if(sum != 0)
			wp[i] = one*1.0/sum;
		else wp[i] = 0;
	//	printf("  %d %lf\n",i,wp[i]);
	}
}
double tmp[110];
void gettmp(int a){
	int one,sum;
	for(int i = 0 ; i < n; i ++){
		if(i == a) continue;
		one = sum = 0;
		for(int j =  0; j < n; j ++){
			if(j == a) continue;
			if(map[i][j] == '1'){
				one ++;
				sum ++;
			}
			else if(map[i][j] == '0')
				sum++;
		}
		if(sum != 0)
			tmp[i] = one*1.0/sum;
		else tmp[i] = 0;
	}
}
void getowp()
{
	for(int a = 0; a < n; a ++){
		// delete the game with a
		gettmp(a);
		owp[a] = 0;
		int sum = 0;
		for(int i = 0 ; i < n; i ++){
			if(i == a) continue;
			if(map[a][i] != '.'){
				owp[a] += tmp[i];
				sum ++;
			}
		}
		if(sum != 0)
			owp[a] /= sum;
	//	printf("%d %lf\n",a,owp[a]);
	}
}
void getoowp()
{
	for(int i = 0 ; i < n; i ++){
		int sum = 0;
		oowp[i] = 0;
		for(int j = 0 ; j < n; j ++){
			if(map[i][j] != '.'){
				oowp[i] += owp[j];
				sum ++;
			}
		}
		if(sum != 0)
			oowp[i] /= sum;
		
	}
}
void getans()
{
	for(int i = 0 ; i < n; i ++){
		printf("%.11lf\n",0.25*wp[i]+0.50 * owp[i] + 0.25 * oowp[i]);
	}
}
int main()
{
	 freopen("1.in","r",stdin);
	 freopen("1.out","w",stdout);
	int t;
	int cas = 0;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		for(int i = 0; i < n; i ++)
			scanf("%s",&map[i]);
		getwp();
		getowp();
		getoowp();
		cas ++;
		printf("Case #%d:\n",cas);
		getans();
	}
	return 0;
}

