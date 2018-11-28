#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <set>
#include <map>
#include <vector>

using namespace std;

char a[110][110];
double WP[110],OWP[110],OOWP[110];
int n;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;

	scanf("%d\n",&tests);
	for (int tt=1; tt<=tests; tt++){
		printf("Case #%d:\n",tt);
		scanf("%d\n",&n);

		for (int i=0; i<n; i++){
			for (int j=0; j<n; j++){
				scanf("%c",&a[i][j]);
			}
			scanf("\n");
		}

		for (int i=0; i<n; i++){
			double x=0;
			double y=0;
			for (int j=0; j<n; j++){
				if (a[i][j]!='.') y++;
				if (a[i][j]=='1') x++;
			}
			WP[i]=x/y;
		}

		for (int i=0; i<n; i++){
			double sum=0;
			double cnt=0;
			for (int j=0; j<n; j++)
				if (a[i][j]!='.'){
					cnt++;
					double x=0, y=0;
					for (int k=0; k<n; k++)
						if (k!=i){
							if (a[j][k]!='.') y++;
							if (a[j][k]=='1') x++;
						}
					sum+=x/y;
				}
			OWP[i]=sum/cnt;
		}

		for (int i=0; i<n; i++){
			double sum=0;
			double cnt=0;
			for (int j=0; j<n; j++)
				if (a[i][j]!='.')
					sum+=OWP[j], cnt++;
			OOWP[i]=sum/cnt;
		}

		for (int i=0; i<n; i++)
			printf("%.10lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
	}

	return 0;
}