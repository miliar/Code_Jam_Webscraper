#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int main(){

	int T;
	cin>>T;
	
	for(int tc=1;tc<=T;tc++){
		int N;
		cin>>N;
		vector<int> data(N);
		for(int i=0;i<N;i++)
			cin>>data[i];
		bool flag=true;
		int count=0;
		for(int i=0;i<N;i++){
			if(data[i]-1==i)
				count++;
			else
				flag=false;
		}
		double result;
		count=min(N,count);
		
		if(flag)
			result=0;
		else
			result=N-count;
		printf("Case #%d: %.6lf\n",tc,result);
	}
	
	return 0;
}
