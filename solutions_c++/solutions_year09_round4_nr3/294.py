#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <set>
#include <algorithm>
#include <deque>

using namespace std;
#define TASK "file"
int test;

#define N 300

int a[N][N];
int n,k;

int f[N][N];
int c[N][N];
int u[N];
int p[N];

deque<int> Q;

int cool(int l,int r){	
	for (int i=0;i<k;i++)
		if (a[l][i]<=a[r][i]) return 0;
	return 1;
}

int great(int i,int j){
	for (int l=0;l<k;l++){
		if (a[i][l]>a[j][l]) return true;
		if (a[i][l]<a[j][l]) return false;
	}
	return false;
}



int main(void){
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
	
	scanf("%i",&test);
	for (int tst=0;tst<test;tst++){
		printf("Case #%i: ",tst+1);
		scanf("%i %i",&n,&k);
		for (int i=0;i<n;i++)
			for (int j=0;j<k;j++) scanf("%i ",&a[i][j]);
		for (int i=0;i<n+n+2;i++)
			for (int j=0;j<n+n+2;j++) f[i][j]=c[i][j]=0;
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				if (i!=j)
					c[i][n+j]=cool(i,j);
		for (int i=0;i<n;i++) c[n+n][i]=1;
		for (int i=0;i<n;i++) c[i+n][n+n+1]=1;

		int flow=0;
		while (true){
			for (int i=0;i<n+n+2;i++){
				u[i]=0;
				p[i]=-1;
			}
			u[n+n]=1;
			Q.push_back(n+n);
			while (!Q.empty()){
				int ver=Q.front();				
				Q.pop_front();
				for (int i=0;i<n+n+2;i++)
					if (!u[i] && c[ver][i]-f[ver][i]>0){
						u[i]=1;
						Q.push_back(i);
						p[i]=ver;
					}

			}
			if (p[n+n+1]==-1) break;
			flow++;
			int t=n+n+1;
			while (t!=n+n){
				int pv=p[t];
				f[pv][t]=1;
				f[t][pv]=-1;
				t=pv;
			}

		}
		
		cout<<n-flow<<endl;
	}

	
	return 0;
}