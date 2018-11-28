#include <stdio.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <math.h>
#include <map>
#define MaxLength INT_MAX
#define MaxNode 12
#define MN 2000005
using namespace std;

int M,T,N,S;
vector<int> mem[MN];
vector<int>::iterator it1,it2;
int size;
int p10[8]={1,10,100,1000,10000,100000,1000000,10000000};
int len(int n){
	if(n>=1000000)
		return 7;
	if(n>=100000)
		return 6;
	if(n>=10000)
		return 5;
	if(n>=1000)
		return 4;
	if(n>=100)
		return 3;
	if(n>=10)
		return 2;
	return 1;
}
int main(){
	int i,j,k,l,tt,a,b;
	long long res;
	for(i=1; i<MN;i++){
		//printf("%d: ",i);
		l = len(i);
		a = i;
		for(j=1; j<l;j++){
			a = (a%10)*p10[l-1] + (a/10);
			if(a<i)
				mem[i].push_back(a);
		}
		if(mem[i].size()>1){
			for(j=0; j<mem[i].size(); j++)
				for(k=j+1; k<mem[i].size(); k++)
					if(mem[i][j] == mem[i][k])
						mem[i].erase(mem[i].begin()+k);
			sort(mem[i].begin(), mem[i].end());
		}
	}
	scanf("%d",&T);
	for(tt=1; tt<=T;tt++){
		res = 0;
		scanf("%d %d",&a,&b);
		for(i=a+1; i<=b ;i++)
			for(j=0; j<mem[i].size(); j++)
				if(mem[i][j]>=a)
					res++;

		printf("Case #%d: %lld\n",tt,res);
	}

	return 0;
}
