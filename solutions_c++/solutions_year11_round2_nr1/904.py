#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
using namespace std;

const int maxn = 110;
const int maxm = 1100100;

struct node {
	double win;
	double tot;
	double wp;
	double owp;
	double oowp;
}w[maxn];
int g[maxn][maxn];


int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k;

	int n;
	string str;
	int nca;

	cin>>nca;
	for(int cid=1;cid<=nca;cid++){
		cin>>n;
		
		memset(g,-1,sizeof(g));
		
		for(i=0;i<n;i++){
			w[i].tot = w[i].win = 0;

			cin>>str;
			for(j=0;j<str.size();j++){
				if( str[j] == '0' ){
					g[i][j] = 0;
					w[i].tot = w[i].tot + 1;
				}else if( str[j] == '1' ){
					g[i][j] = 1;
					w[i].tot = w[i].tot + 1;
					w[i].win = w[i].win + 1;
				}
			}
		}

			for(i=0;i<n;i++){
				if( w[i].tot <= 1 ) w[i].owp = 0;
				else {
					double temp = 0;
					int tn = 0;
					for(j=0;j<n;j++){
						if( g[i][j] == 0 ){
							temp += ( w[j].win - 1 )/(w[j].tot-1);
							tn++;
						}
						else if( g[i][j] == 1 ){
							temp += ( w[j].win  )/(w[j].tot-1);
							tn++;
						}
					}

					if( tn!= 0 )
					w[i].owp = temp / tn ;
				}
			}

			for(i=0;i<n;i++){
				
					double temp = 0;
					int tn=0;
					for(j=0;j<n;j++){
						if( g[i][j] != -1 ){
							temp += w[j].owp ;
							tn++;
						}
					}

					if( tn != 0 )
					w[i].oowp = temp / tn;
					else {
						w[i].oowp = 0;
					}
				
			}

		printf("Case #%d:\n",cid);
		for(i=0;i<n;i++){
			printf("%.12lf\n",0.25 * (w[i].win / w[i].tot ) + 0.5 * w[i].owp + 0.25 * w[i].oowp );
		}
	}

		
}

/*
4
4
.11.
0.00
01.1
.10.


*/