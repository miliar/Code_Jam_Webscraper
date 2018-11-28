/*
 * Recycle2012C.cpp
 *
 *  Created on: Apr 15, 2012
 *      Author: batchunag
 */

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <stdio.h>
#include <string.h>
#include <list>
#include <set>
#include <cmath>
#define FOR(i,a,b) for (int i=a; i<b; i++)
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define mp make_pair
#define pb push_back

using namespace std;
typedef vector<int> VI;
typedef pair <int,int> PII;
const int M= 20;

int main(){
	int t,a,b;
	FILE *out=fopen("answer.txt","w");
	ifstream in ("input.txt");
	in>>t;
	/*
	int ans[M];
	set <int> sack;
	for (int x=1; x<M; x++){
		int y=x;
		sack.clear();
		int p=log(x)/log(10);
		int k=(int)pow(10.0,p);
		for (int i=1; i<=p; i++){
			y+=k*10*(y%10);
			y/=10;
			if (y>x) sack.insert(y);
		}
		ans[x]=sack.size();
	}
	*/
	/*
	for (int i=1; i<M; i++)
		fprintf(out,"%d\n",ans[i]);
		*/
	for (int i=1; i<=t; i++){
		in>>a>>b;
		int ans=0;
		for (int n=a; n<b; n++){
		//	cout<<n<<":: ";
			for (int m=n+1; m<=b; m++){
				int y=n;
				int p=log(n)/log(10);
				int k=(int)pow(10.0,p);
				for (int s=1; s<=p; s++){
					y+=k*10*(y%10);
					y/=10;
					if (y==m) {
						ans++;
					//	cout<<y<<' ';
					}
				}
			}
	//		cout<<endl;
		}

		fprintf(out,"Case #%d: %d\n",i,ans++);
	}

	return 0;
}
