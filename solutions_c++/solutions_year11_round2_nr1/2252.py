#include<iostream>
using namespace std;
#define R  360
#define C  360
struct elem{
	int win;
	int lose;
	double wp;
	double owp;
	double oowp;
	int count;
};

char map[R][C];
int n;
elem ans[R];

int main()
{
	int i,j;
	int tcase;
	int walk = 0;
	int k;
	int count;
	double RPI;
	FILE *in,*out;
	in = freopen("A-large.in","r",stdin);   
    out = freopen("A-large.txt","w",stdout);   
	scanf("%d",&tcase);
	while(tcase--){
		scanf("%d",&n);
		getchar();
		for(i = 0;i < n;i++){
			ans[i].win = ans[i].lose = ans[i].count = 0;
			for(j = 0;j < n;j++){
				scanf("%c",&map[i][j]);//cout <<map[i][j] <<' ';
				if(map[i][j] == '1'){
					ans[i].count++;
					ans[i].win++;
				}
				else if(map[i][j] == '0'){
					ans[i].count++;
					ans[i].lose++;
				}
			}
			getchar();
		}
		for(i = 0;i < n;i++){
			ans[i].wp = 1.0*ans[i].win/(ans[i].win+ans[i].lose);
		}
		for(i = 0;i < n;i++){
			ans[i].owp = 0; count = 0;
			for(j = 0;j < n;j++){
				if(map[i][j] == '1'){
					k = ans[j].win-1+ans[j].lose;
					if(k > 0)
					ans[i].owp += 1.0*(ans[j].win)/k;
				}
				else if(map[i][j] == '0'){
					k = ans[j].win+ans[j].lose-1;//if(i == 1)cout <<ans[j].win<<' ';
					if(k > 0)
					  ans[i].owp += 1.0*(ans[j].win-1)/k;
				}//if(i ==1)cout <<'(' <<ans[i].owp <<')';
			}
			ans[i].owp /= ans[i].count;
		}
		for(i = 0; i < n;i++){
			ans[i].oowp = 0;
			for(j = 0;j < n;j++){
				if(map[i][j] != '.')
					ans[i].oowp += ans[j].owp;
			}
			ans[i].oowp /= ans[i].count;
		}
		printf("Case #%d:\n",++walk);
		for(i = 0;i < n;i++){
			RPI = 0.25*ans[i].wp+0.5*ans[i].owp+0.25*ans[i].oowp;
			cout <<RPI <<endl;
		}
	}
	fclose(in);   
    fclose(out); 
	return 0;
}