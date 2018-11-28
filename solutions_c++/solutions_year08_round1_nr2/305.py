#include <iostream>
#include <string>
#include <vector>
#include<utility>
#include<algorithm>
#define ll long long
#define pib pair<int,bool>
using namespace std;
int C;		int N,M,T;
		vector<bool> ans,filled;
		vector<vector<pib> > customers;
		vector<bool> cust;
void printall(){
		cout<<"customer prefs"<<endl;
		for(int i=0;i<M;i++){
			for(int j=0;j<customers[i].size();j++){
				cout<<customers[i][j].first<<" "<<customers[i][j].second<<endl;	
			}
			cout<<endl;
		}
		cout<<"ans\n";
		for(int i=0;i<ans.size();i++)
			cout<<ans[i]<<" ";
		cout<<endl;
}
bool legal(){
	for(int i=0;i<M;i++){
		bool custgood=false;
		for(int j=0;j<customers[i].size();j++){				
			if(ans[customers[i][j].first]==customers[i][j].second)
				custgood=true;			
		}
		if(!custgood)
			return false;
	}
	return true;
}
int counter(){
	int count=0;
	for(int i=0;i<ans.size();i++)
		if(ans[i])
			count++;
	return count;
}
void fillans(int filler){
		int i=0;
		while(filler>0){		
			ans[i]=filler%2;
			filler/=2;	
			i++;
		}
}/*
bool fill(){
		for(int i=0;i<M;i++){
			if(customers[i].size()==1){
				if(filled[customers[i].first]&&ans[customers[i].first]!=customers[i].second)
					return 0;
				else{
					filled[customers[i]]=1;
					ans[customers[i].first]=customers[i].second;		
					cust[i]=1;
				}
			}			
		}
		for(int i=0;i<M;i++){
			if(!cust[i]){
				for(int j=0;j<customers[i].size();j++){
					
			
				}
			}
		}
}*/
int main(){
	cin>>C;
	for(int z=1;z<=C;z++){
		cout<<"Case #"<<z<<": ";
		cin>>N>>M;
		ans.clear();
		filled.clear();
		customers.clear();
		cust.clear();
		for(int i=0;i<N;i++){
			ans.push_back(false);
			filled.push_back(false);
		}
		for(int i=0;i<M;i++){	
			cust.push_back(false);		
			cin>>T;
			vector<pib> customer;
			for(int j=0;j<T;j++){
				pib temp;
				int t1;
				bool t2;
				cin>>t1>>t2;
				temp.first=t1-1;
				temp.second=t2;			
				customer.push_back(temp);
			}
			customers.push_back(customer);
		}
		int minN=N+1;
		bool none=true;
		vector<bool> finalans;
		for(int i=0;i<=(1<<(N+1)-1);i++){
			fillans(i);
			if(legal()){				
				if(counter()<minN){
					none=false;
					minN=counter();	
					finalans=ans;
				}
			}
			else{
				//printall();
			}
		}
		if(none)
			cout<<"IMPOSSIBLE\n";
		else{
			if(finalans[0])
				cout<<"1";
			else
				cout<<"0";
			for(int i=1;i<N;i++){
				if(finalans[i])
					cout<<" 1";
				else
					cout<<" 0";
			}
			cout<<endl;
		}
	}
}
