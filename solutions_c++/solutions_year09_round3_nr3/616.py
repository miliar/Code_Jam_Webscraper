#include <cstdio>
#include <algorithm>

using namespace::std;

int count(int *cells, int *rel, int n, int m) 
{
	int i,j,r,left, right;
	left = right = 0;
	for(i=0;i<n;i++) {
		r = rel[i];
		cells[r]=0;
		
		for(j=r-1;j>0;j--)
			if(cells[j]==0)
				break;
			else
				left++;
		for(j=r+1;j<=m;j++)
			if(cells[j]==0)
				break;
			else
				right++;
	}
	return left+right;
}

int main() {
	int i,j,k,t,p,q,r;
	int rel[10],cells[102];
	scanf("%d",&t);
	int res = 999999;
	for(i=0;i<t;i++) {
		res = 99999999;
		scanf("%d %d",&p,&q);
		for(j=0;j<=100;j++)
			cells[j]=1;
		for(j=0;j<q;j++) {
			scanf("%d",&k);
			rel[j]=k;
		}
		res = count(cells, rel,q,p);
		for(k=0;k<q;k++)
				cells[rel[k]]=1;
		if(q == 1)
			res = p-1;
		
		while(next_permutation(rel,rel+q)) {
			r=count(cells, rel,q,p);
			for(k=0;k<q;k++)
				cells[rel[k]]=1;
			if(res>r)
				res = r;
		}

		while(next_permutation(rel,rel+q)) {
			r = count(cells, rel,q,p);
			for(k=0;k<q;k++)
				cells[rel[k]]=1;

			if (res>r)
				res = r;
		}
	
		printf("Case #%d: %d\n",i+1, res);
	}

	return 0;
}

