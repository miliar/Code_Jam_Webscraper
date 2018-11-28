#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <iostream>
#include <cstdio>
#include <queue>
#include <deque>

using namespace std;

int main()	{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int k;
	scanf("%d",&k);
	for (int t=1; t<=k; t++) {
		int n,s,ii;
		double fs;
		char c;
		scanf("%d\n",&n);
		vector <vector<int> > v(n,vector<int> (n,-1));
		vector <vector<double> > v2(n,vector<double> (n,-1)),v3(n,vector<double> (n,-1));
		vector<double> wp(n,0),owp(n,0),oowp(n,0);
		for (int i=0; i<n; i++) {
			s=0;
			ii=0;
			for (int j=0; j<n; j++) {
				scanf("%c",&c);
				if (c=='.') v[i][j]=-1;
				else {
					if (c=='0') v[i][j]=0;
					else if (c=='1') v[i][j]=1;
					s+=v[i][j];
					ii++;
				}
			}
			scanf("\n");
			if (ii==0) wp[i]=0; 
			else wp[i]=(s+0.0)/ii;
		}
		printf("Case #%d:\n",t);
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				s=0;
				ii=0;
				for (int l=0; l<n; l++) {
					if (j!=l&&v[i][l]!=-1) {
						s+=v[i][l];
						ii++;
					}
				}
				if (ii==0) v2[i][j]=0; 
				else v2[i][j]=(s+0.0)/ii;
			}
		}
		for (int i=0; i<n; i++) {
			fs=0;
			ii=0;
			for (int j=0; j<n; j++) {
				if (i!=j&&v[i][j]!=-1) {
					fs+=v2[j][i];
					ii++;
				}
			}
			if (ii==0) owp[i]=0; 
			else owp[i]=fs/ii;
		}

		for (int i=0; i<n; i++) {
			fs=0;
			ii=0;
			for (int j=0; j<n; j++) {
				if (i!=j&&v[i][j]!=-1) {
					fs+=owp[j];
					ii++;
				}
			}
			if (ii==0) oowp[i]=0; 
			else oowp[i]=fs/ii;
		}
		for (int i=0; i<n; i++) {
			printf("%.9lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
    return 0;
}
