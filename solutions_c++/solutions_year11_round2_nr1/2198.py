#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 101
int mas[MAX][MAX];

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int t,n,i,j,k;
	char c;
	cin >> t;
	for(i=0;i<t;i++){
		cin >> n;
		getchar();
		for(j=0;j<n;j++){
			for(k=0;k<n;k++){
				c = getchar();
				if(c=='1') mas[j][k]=1;
				else if(c=='0') mas[j][k]=0;
				else mas[j][k]=-1;
			}
			getchar();
		}
		double WP[MAX],OWP[MAX],OOWP[MAX];
		int p,m;
		for(j=0;j<n;j++){
			int gen=0,wins=0;
			for(k=0;k<n;k++){
				if(mas[j][k]==1){
					wins++;
					gen++;
				}
				else if(mas[j][k]==0){
					gen++;
				}
			}
			WP[j]=wins*1.0/gen;
			double WP_l[MAX];
			for(m=0;m<n;m++){
				if(mas[j][m]==-1) continue;
				int gen_l=0;
				int wins_l=0;
				for(p=0;p<n;p++){
					if(p==j) continue;
					if(mas[p][m]==0){
						gen_l++;
						wins_l++;
					}
					else if(mas[p][m]==1){
						gen_l++;
					}
				}
				WP_l[m]=wins_l*1.0/gen_l;
			}
			double sum=0;
			int num=0;
			for(m=0;m<n;m++){
				if(mas[j][m]==1 || mas[j][m]==0){
					sum+=WP_l[m];
					num++;
				}
			}
			sum=sum*1.0/num;
			OWP[j]=sum;
		}
		for(int i=0;i<n;i++){
			double sum=0;
			int num=0;
			for(int j=0;j<n;j++){
				if(mas[i][j]==1 || mas[i][j]==0){
					sum+=OWP[j];
					num++;
				}
			}
			OOWP[i]=sum*1.0/num;
		}
		printf("Case #%d:\n",i+1);
		for(int i=0;i<n;i++){
			double rpi = 0.25*WP[i]+0.50*OWP[i]+0.25*OOWP[i];
			printf("%lf\n",rpi);
		}
		
	}
	return 0;
}