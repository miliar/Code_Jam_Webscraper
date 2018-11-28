#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef long int int64;


void answer(vector <int64> v1,vector <int64>v2,int n,int i){

	std::sort(v1.begin(),v1.end());
	std::sort(v2.rbegin(),v2.rend());
	int64 res=0;

	for(int i=0;i<n;++i)
		res+=(v1[i]*v2[i]);

	printf("Case #%d: %ld\n",i,res);


}



void main(){

	int t,n,num;

	


	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);

	scanf("%d",&t);

	for(int i=0;i<t;++i){

		scanf("%d",&n);

		vector<int64> v1(n);
		vector<int64> v2(n);

		for(int j=0;j<n;++j){
			scanf("%ld",&num);
			v1[j]=num;

		}

		for(int k=0;k<n;++k){
			scanf("%ld",&num);
			v2[k]=num;

		}

		answer(v1,v2,n,i+1);

	}




}