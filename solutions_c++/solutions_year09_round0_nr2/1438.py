#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h> 
#include <string>
#include <vector> 
#include <iostream>
#include <sstream>
#include <queue>
using namespace std;

long a,b,d,n,i,k,c,i1,k1,j,m,l,h,w;
long t,cas,k0;
char ts[110][110],z,z1;
long tb[110][110];
pair <long,long> p1,p2;
vector <pair<long, long> > tp;	//scie¿ka

pair <long,long> dalej(pair <long,long> p1){
	long i,j,a;

	pair <long,long> p2;

	a=tb[p1.first][p1.second];
	i=p1.first;
	j=p1.second;
	p2=p1;
	if(i>0){
		if(tb[i-1][j]<a){
			a=tb[i-1][j];
			p2.first=i-1;
			p2.second=j;
		}
	}
	if(j>0){
		if(tb[i][j-1]<a){
			a=tb[i][j-1];
			p2.first=i;
			p2.second=j-1;
		}
	}
	if(j<w-1){
		if(tb[i][j+1]<a){
			a=tb[i][j+1];
			p2.first=i;
			p2.second=j+1;
		}
	}
	if(i<h-1){
		if(tb[i+1][j]<a){
			a=tb[i+1][j];
			p2.first=i+1;
			p2.second=j;
		}
	}
	return p2;
}







int main() { //convex hull
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin);
		//int czas=clock();
	

	//czas = clock() - czas;
	//printf("%lf\n",double(czas)/CLOCKS_PER_SEC);
	//while(1){
	
	scanf("%ld",&t);
	
	
	for(cas=1;cas<=t;cas++){

		scanf("%ld%ld",&h,&w);
		
		
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				scanf("%ld",&tb[i][j]);
				ts[i][j]=0;

			}
		}
			
		z='a';
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				if(ts[i][j]==0){
					tp.clear();
					p1.first=i;
					p1.second=j;
					ts[i][j]=z;
					tp.push_back(p1);
					p2=dalej(p1);
					while(ts[p2.first][p2.second]==0){
						ts[p2.first][p2.second]=z;
						tp.push_back(p2);
						p1=p2;
						p2=dalej(p1);
					}
					if(ts[p2.first][p2.second]==ts[p1.first][p1.second]){
						z++;
					}
					else {
						z1=ts[p2.first][p2.second];
						k=tp.size();
						for(i1=0;i1<k;i1++){
							p1=tp[i1];
							ts[p1.first][p1.second]=z1;
						}
					}
				}
			}
		}

				


		printf("Case #%ld:\n",cas);
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				printf("%c ",ts[i][j]);
			}
			printf("\n");
		}


	}


	
	return 0;
} 
