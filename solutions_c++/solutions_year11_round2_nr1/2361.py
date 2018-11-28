#include <cstdio>

using namespace std;

struct point
{
	char results[105];
	double wp, owp, oowp, result;
	int ene;
};

int t;
int n;

point tab[105];


int main()
{
	
	scanf("%d", &t);
	for(int k=1; k<=t; k++){
		printf("Case #%d:\n", k);
		scanf("%d", &n);
		for(int i=0; i<=n; i++)
			tab[i].wp = tab[i].owp = tab[i].oowp = tab[i].result =tab[i].ene= 0;
		for(int i=0; i<n; i++){
			scanf("%s", tab[i].results);
			for(int j=0; j<n; j++){
				if(tab[i].results[j]!='.'){
					tab[i].ene++;
					if(tab[i].results[j]=='1')
						tab[i].wp++;
				}
			}
		}
		
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if(tab[i].results[j]!='.'){
					tab[i].owp += (tab[j].wp-(tab[j].results[i]-'0'))/(tab[j].ene-1);
				}
			}
			tab[i].owp = tab[i].owp/ tab[i].ene;
		}
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if(tab[i].results[j]!='.'){
					tab[i].oowp += tab[j].owp;
				}
			}
			tab[i].oowp = tab[i].oowp/tab[i].ene;
		}
		for(int i=0; i<n; i++){
			printf("%.12lg\n", (tab[i].wp/tab[i].ene)/4 + tab[i].owp/2 + tab[i].oowp/4);
		}
	}
	return 0;
}