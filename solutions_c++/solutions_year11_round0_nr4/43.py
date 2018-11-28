#include<iostream>

using namespace std;

int compare (const void * a, const void * b) 
{  
	return ( *(int*)a - *(int*)b);
}


int num[2000], bnum[2000];

int main(){
	int cs;
	double ans;
	cin>>cs;
	freopen("D.out","w",stdout);
	for(int css=1;css<=cs;css++){
		int n;
		cin>>n;
		for(int i=0;i<n;i++) {cin>>num[i]; bnum[i]=num[i];}
		qsort(bnum, n, sizeof(int), compare);
		ans = 0;
		for(int i=0;i<n;i++) 
		{
			if(num[i]!=bnum[i]) ans++;
		}

		printf("Case #%d: %f\n", css, ans);
	}
	return 0;
}