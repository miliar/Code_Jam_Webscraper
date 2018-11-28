#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define equal(a,b) (ABS((a)-(b))<eps)
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pair pair<int,int>
#define MAX 101
using namespace std;
int P[MAX];
int W[MAX];
double WP[MAX];
double OWP[MAX];
double OOWP[MAX];
char s[MAX][MAX];
int main(){
	string filename, fileword;
	fileword = "A";
	filename = fileword;
	filename = fileword+"-small-attempt0";
	filename = fileword+"-large";
	freopen((filename+".in").c_str(),"r",stdin);
	freopen((filename+".out").c_str(),"w",stdout);
	int T,N;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		scanf("%d",&N);
		for(int i=0; i<N; i++){
			scanf("%s",s[i]);
			W[i]=0;
			P[i]=0;
			for(int j=0; j<N; j++) {
				if(s[i][j]=='1' && i!=j) W[i]++;
				if(s[i][j]!='.' && i!=j) P[i]++;
			}
		}
		for(int i=0; i<N; i++) {
			WP[i]=double(0.0+W[i])/P[i];
		}
		for(int i=0; i<N; i++) {
			double sum=0.0;
			for(int j=0; j<N; j++){
				if(s[i][j]!='.' && i!=j) {
					if(s[j][i]=='1') sum+=(0.0+W[j]-1)/(P[j]-1);
					else sum+=(0.0+W[j])/(P[j]-1);
				}
			}
			OWP[i]=sum/P[i];
		}
		for(int i=0; i<N; i++) {
			double sum=0.0;
			for(int j=0; j<N; j++){
				if(s[i][j]!='.' && i!=j) {
					sum+=OWP[j];
				}
			}
			OOWP[i]=sum/P[i];
		}
		printf("Case #%d:\n",t);
		for(int i=0; i<N; i++) {
			cout<<((0.25)*WP[i]+(0.50)*OWP[i]+(0.25)*OOWP[i])<<endl;//.convert()<<endl;
		}
	}
	//system("pause");
	return 0;
}
