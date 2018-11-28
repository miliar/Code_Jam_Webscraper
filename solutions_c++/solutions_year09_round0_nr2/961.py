#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int M[101][101];
char u[101][101];
int qi[10001];
int qj[10001];

const int di[4]={1,0,0,-1};
const int dj[4]={0,1,-1,0};

int main(){
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int q,n,m,i,j,w,st,en,ci,cj,ti,tj;
	scanf("%d",&q);
	char c;
	for(int k=1;k<=q;k++){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&M[i][j]);
		memset(u,0,sizeof(u));
		c='a';
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(!u[i][j]){
					u[i][j]=c;
					st=0;
					en=1;
					qi[st]=i;
					qj[st]=j;
					while(st<en){
						ci=qi[st];
						cj=qj[st];
						int mn=15000,mni,mnj;
						for(w=0;w<4;w++){
							ti=ci+di[w];
							tj=cj+dj[w];
							mn=15000;
							if(ti>=0 && ti<n && tj>=0 && tj<m)
								if(!u[ti][tj] && M[ti][tj]>M[ci][cj]){
									for(int z=0;z<4;z++){
										if(ti+di[z]>=0 && ti+di[z]<n && tj+dj[z]>=0 && tj+dj[z]<m)
											if(M[ti+di[z]][tj+dj[z]]<=mn){
												mn=M[ti+di[z]][tj+dj[z]];
												mni=ti+di[z];
												mnj=tj+dj[z];
											}
									}
									if(mni==ci && mnj==cj){
										u[ti][tj]=c;
										qi[en]=ti;
										qj[en]=tj;
										en++;
									}
								}
						}
						mn=15000;
						for(w=0;w<4;w++){
							ti=ci+di[w];
							tj=cj+dj[w];
							if(ti>=0 && ti<n && tj>=0 && tj<m)
								if(M[ti][tj]<=mn){
									mn=M[ti][tj];
									mni=ti;
									mnj=tj;
								}
						}
//						if(u[mni][mnj])puts("wtf dude");
						if(mn<M[ci][cj] && !u[mni][mnj]){
							u[mni][mnj]=c;
							qi[en]=mni;
							qj[en]=mnj;
							en++;
						}
						st++;
					}
					c++;
/*					for(int i1=0;i1<n;i1++){
						for(int j1=0;j1<m;j1++)
							printf("%c ",(u[i1][j1])?u[i1][j1]:' ');
						puts("");
					}
					puts("");
*/
				}
		printf("Case #%d:\n",k);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++)
				printf("%c ",u[i][j]);
			puts("");
		}
	}
	return 0;
}
