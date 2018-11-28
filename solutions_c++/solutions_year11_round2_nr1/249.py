#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxn=101;
int a[maxn][maxn];
char str[maxn+1];
double owp[maxn];
int n;

void init(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++){
		scanf("%s",str);
		for (int j=0;j<n;j++){
			if (str[j]=='.'){
				a[i][j+1]=-1;
			} else {
				a[i][j+1]=str[j]-'0';
			}
		}
	}
	return;
}

double calcrwp(int x,int y){
	int tot=0;
	int win=0;
	for (int i=1;i<=n;i++){
		if (i==y){
			continue;
		}
		if (a[x][i]==-1){
			continue;
		}
		tot++;
		if (a[x][i]==1){
			win++;
		}
	}
	if (tot==0){
		return 0;
	}
	return ((double)win)/((double)tot);
}

double calcwp(int x){
	int tot=0;
	int win=0;
	for (int i=1;i<=n;i++){
		if (a[x][i]==-1){
			continue;
		}
		tot++;
		if (a[x][i]==1){
			win++;
		}
	}
	if (tot==0){
		return 0;
	}
	return ((double)win)/((double)tot);
}

double calcoowp(int x){
	int tot=0;
	double sum=0;
	for (int i=1;i<=n;i++){
		if (a[x][i]==-1){
			continue;
		}
		tot++;
		sum+=owp[i];
	}
	if (tot==0){
		return 0;
	}
	return sum/((double)tot);
}

double calcowp(int x){
	int tot=0;
	double sum=0;
	for (int i=1;i<=n;i++){
		if (a[x][i]==-1){
			continue;
		}
		tot++;
		sum+=calcrwp(i,x);
	}
	if (tot==0){
		return 0;
	}
	return sum/((double)tot);
}

void process(){
	for (int i=1;i<=n;i++){
		owp[i]=calcowp(i);
	}
	for (int i=1;i<=n;i++){
		printf("%.8lf\n",0.25*calcwp(i)+0.5*owp[i]+0.25*calcoowp(i));
	}
	return;
}

int main(){
	int cse;
	scanf("%d",&cse);
	for (int i=1;i<=cse;i++){
		init();
		printf("Case #%d:\n",i);
		process();
	}
	return 0;
}
