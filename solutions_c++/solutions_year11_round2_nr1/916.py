#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#define FOR(x,y,z) for(int (x)=(y);(x)<(z);(x)++)
#define FORQ(x,y,z) for(int (x)=(y);(x)<=(z);(x)++)
#define FORDQ(x,y,z) for(int (x)=(y);(x)>=(z);(x)--)
#define R 111
using namespace std;
char tab[R][R];
double out[R][3];
int numop[R];
int main(){
	int packs;
	scanf("%d",&packs);
	FORQ(lololol,1,packs){
		int n;
		scanf("%d",&n);
		FOR(i,0,n)scanf("%s",tab[i]);
		FOR(i,0,n){
			double ng=0,wg=0;
			FOR(j,0,n){
				if(tab[i][j]=='1'){ng++;wg++;}
				else if(tab[i][j]=='0')ng++;
			}
			out[i][0]=wg/ng;
			numop[i]=(int)ng;
		}
		FOR(h,0,n){
			double sumowp=0;
			FOR(i,0,n){
				if(i==h)continue;
				double ng=0,wg=0;
				if(tab[h][i]=='.')continue;
				FOR(j,0,n){
					if(j==h)continue;
					if(tab[i][j]=='1'){ng++;wg++;}
					else if(tab[i][j]=='0')ng++;
				}
				sumowp+=wg/ng;
			}
			out[h][1]=sumowp/((double)(numop[h]));
		}
		FOR(i,0,n){
			double sumoowp=0;	
			FOR(j,0,n){
				if(i==j)continue;
				if(tab[i][j]=='.')continue;
				sumoowp+=out[j][1];
			}
			out[i][2]=sumoowp/((double)(numop[i]));
		}
		//FOR(i,0,n){FOR(j,0,3)printf("%Lf ",out[i][j]);putchar('\n');}
		printf("Case #%d:\n",lololol);
		FOR(i,0,n)printf("%.6Lf\n",0.25*out[i][0]+0.5*out[i][1]+0.25*out[i][2]);
	}
	return 0;
}