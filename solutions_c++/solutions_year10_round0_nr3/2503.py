#include<iostream>
#include<vector>
#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
	int t;scanf("%d",&t);
	FILE *pFile;
	pFile = fopen ("E:\\A11\\roller_coster.txt","w");
	for(int c=1;c<=t;c++){
		int n,k,r;
		scanf("%d%d%d",&r,&k,&n);int i;
		vector<int>v(n,0);
		for(i=0;i<n;i++)scanf("%d",&v[i]);
		int sum=0;
		while(r){
			int t=0;vector<int>q;
			while(t<k&&v.size()){
				sum+=v[0];
				t+=v[0];
				if(t>k){
					sum-=v[0];break;
				}
				q.push_back(v[0]);
				v.erase(v.begin(),v.begin()+1);
			}
			r--;
			for(i=0;i<q.size();i++)v.push_back(q[i]);
		}fprintf(pFile,"Case #%d: %d\n",c,sum);
	}
	fclose(pFile);
	return 0;
}