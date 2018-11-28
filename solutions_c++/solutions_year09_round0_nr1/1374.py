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

long a,b,d,n,i,k,c,i1,k1,j,z,m,l;
long t,cas,k0;
char ts[6000][20],we[20];
string wex;

vector <string> tw[15][30],tss,tss2;
vector <vector<long> > tx;
vector <long> ta; 

int main() { //convex hull
	freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin);
		//int czas=clock();
	

	//czas = clock() - czas;
	//printf("%lf\n",double(czas)/CLOCKS_PER_SEC);
	//while(1){
	
	scanf("%ld%ld%ld",&l,&d,&n);
	
	for(i=0;i<15;i++){
		for(j=0;j<30;j++){
			tw[i][j].clear();
		}
	}
	for(i=0;i<d;i++){
		scanf("%s",&ts[i]);

		wex=ts[i];
		for(j=0;j<l;j++){
			a=wex[j]-'a';
			tw[j][a].push_back(wex);
		}
	}

	for(cas=1;cas<=n;cas++){

		scanf("%s",&we);
		
		k=strlen(we);

		i=0;

		a=0;
		tx.clear();
		while(i<k){
			ta.clear();
			if(we[i]=='('){
				i++;
				
				while(we[i]!=')')
					ta.push_back(we[i++]-'a');
				i++;
			}
			else 
				ta.push_back(we[i++]-'a');
			tx.push_back(ta);
		}


		k=tx[0].size();
		tss.clear();
		for(i=0;i<k;i++){
			a=tx[0][i];
			k1=tw[0][a].size();
			for(j=0;j<k1;j++)
			
				tss.push_back(tw[0][a][j]);
		}
		tss2.clear();
		k0=tss.size();
		for(i=1;i<l;i++){
			k=tx[i].size();
			for(j=0;j<k;j++){
				for(i1=0;i1<k0;i1++){
					if(tss[i1][i]==tx[i][j]+'a')
						tss2.push_back(tss[i1]);
				}
			}
			tss.clear();
			k0=tss2.size();
			for(j=0;j<k0;j++)
				tss.push_back(tss2[j]);
			tss2.clear();
		}
				

		b=tss.size();





		printf("Case #%ld: %ld\n",cas,b);


	}


	
	return 0;
} 
