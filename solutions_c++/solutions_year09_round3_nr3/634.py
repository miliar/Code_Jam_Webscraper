#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
long long int func(vector<int>prison,vector<int>v,int p){
	long long int cnt=0,j,k;
//	cout<<"in func"<<"\n";
	unsigned int i;
//	long long min=9999999999;
	for(i=0;i<v.size();i++){
	//	cout<<v[i]<<" ";
		j=v[i]+1;
		k=v[i]-1;
//		cout<<"1";
		while(j<=p && prison[j]>0){
			cnt++;
			j++;
		}
		while(k>=1&& prison[k]>0){
			cnt++;
			k--;
		}
		prison[v[i]]=-1;
	}
//	cout<<"out"<<"\n";
	return cnt;

	
}
	



int main(){
	int t,i,j,k,count=1;
	cin>>t ;
	while(t){
		int p,q;
		cin>>p>>q;
		vector<int> pris(105,-1);
		pris[0]=0;
		for(i=1;i<=p;i++){
			pris[i]=i;
		}
//		cout<<"k"<<"\n";
		vector<int>v;
		int k;
		for(i=0;i<q;i++){
			cin>>k;
			v.push_back(k);
		}
//		cout<<"k1"<<"\n";


	//	sort(v.begin(),v.end());
		vector<int>v1;
		v1=v;
		long long min=999999999;
		while(1){
			long long m=func(pris,v,p);
		//	cout<<m<<"\n";
			if(m<min)min=m;
			next_permutation(v.begin(),v.end());
			for(i=0;i<v.size();i++){
	//			cout<<v[i]<<" ";
				if(v[i]!=v1[i])break;
				
			}
		//	cout<<"\n";
			if(i==v.size())break;
		}
		cout<<"Case #"<<count<<": "<<min<<"\n";
//		while(1){
		t--;count++;
	}
}







