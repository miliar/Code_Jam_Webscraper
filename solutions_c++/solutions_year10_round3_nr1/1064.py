#include <algorithm>
#include <cmath>
#include <climits>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;


int main(){
	
	FILE *fp;
	FILE *gp;
	fp=fopen("small.in","r");
	gp=fopen("output.out","w");
	vector<int>left;
	vector<int>right;
	int t,n;
	fscanf(fp,"%d",&t);
	for(int ee=0;ee<t;ee++){
		fscanf(fp,"%d",&n);
		left.clear();
		right.clear();
		for(int a=0;a<n;a++){
			int p,q;
			fscanf(fp,"%d %d",&p,&q);
			left.push_back(p);
			right.push_back(q);
		}
		int m=left.size();
		int ans=0;
		for(int a=0;a<m;a++)for(int b=a+1;b<m;b++){
			if((left[a]-left[b])*(right[a]-right[b])<0)ans++;
		}
		fprintf(gp,"Case #%d: %d\n",ee+1,ans);
	}
	fclose(fp);
	fclose(gp);
	return 0;
}
