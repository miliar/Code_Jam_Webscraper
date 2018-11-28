#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>

#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-9




int ABS( int a ) { return a < 0 ? -a : a ;}
#define siz 110
int N;
char str[siz][siz];
double WP[siz];
double OWP[siz];
double OOWP[siz];

void genWP(){
	int i,j;
	double win;
	double res,play;
	for( i =0 ; i<N; i++){
		play = 0;
		win = 0;
		for( j =0; j < N; j++){
			if(str[i][j]=='1'){
				win++;
				play++;
			}
			else if(str[i][j]=='0'){
				play++;
			}
		}
		res =  win/play;
		WP[i] = res;
	}
}

void genOWP(){
	int i, j, k;
	double res,op,win;
	double pl;
	for( i= 0 ; i < N; i++){
			op = 0;
			res = 0;
		for(j  =0; j < N; j++){
		
	
		win = 0;
		pl = 0;
			if(str[i][j]!='.'){
				op++;
				for( k = 0; k < N; k++){
					if(i!=k ){
						if(str[j][k]=='1'){
							win++;
							pl++;
						}
						else if(str[j][k]=='0'){
							pl++;
						}
					}
				}
				res+=(win/pl);
			}
		}
		OWP[i] = res/op;
	}
}

void genOOWP(){
		int i, j;
	double res,op;
	
	for( i= 0 ; i < N; i++){
		res = 0;
		op = 0;
		for(j  =0; j < N; j++){
			if(str[i][j]!='.'){
				res+=OWP[j];
				op++;
			}
		}
		OOWP[i] = res/op;
	}
}
int main()
{
	 //freopen("A.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int  kase, ct = 1;
	int i ;
	scanf("%d",&kase);
	while(kase--){
		scanf("%d",&N);
		for(i=0 ; i <N; i++){
			scanf("%s",str[i]);
		}
		genWP();
		genOWP();
		genOOWP();
		printf("Case #%d:\n",ct++);
		for( i= 0 ; i <N; i++){
		//	printf("WP %.10lf\n",WP[i]);
		//	printf("OWP %.10lf\n",OWP[i]);
			//printf("OOWP %.10lf\n",OOWP[i]);

			printf("%.10lf\n",0.25*WP[i] + 0.5 *OWP[i] + 0.25 * OOWP[i] + eps);

		}
	}
	
	return 0;


}