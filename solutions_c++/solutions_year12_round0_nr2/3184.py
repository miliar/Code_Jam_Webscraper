#include<iostream>
#include<stdio.h>
#include<vector>
#include<cmath>
using namespace std;

int main(){
	int T;
	cin>>T;
	vector<int> results;
	results.resize(T);
	vector<int> sumS;
	int N,S,p;
	int rawP;
	int supP;
	for(int i=0;i<T;i++)
	{
		rawP=0;
		supP=0;
		cin>>N;
		cin>>S;
		cin>>p;
		sumS.resize(N);
		for(int j=0;j<N;j++)
			cin>>sumS[j];
		for(int j=0;j<N;j++)
		{
			if(p>sumS[j])
				continue;
			if(sumS[j]>=(3*p-2))
				rawP++;
			else if(sumS[j]>=(3*p-4))
				supP++;
		}
		if(S<=supP)
			results[i]=rawP+S;
		else
			results[i]=rawP+supP;
	}
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": "<<results[i]<<endl;
	}	

	return 0;
}
