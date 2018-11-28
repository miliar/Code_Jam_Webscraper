#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int arr[1000];
char names[102][105];
int t, s, q;
int getn(char[]);
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t; cin.get();
	for(int i=0; i<t; ++i){
		cin>>s; cin.get();
		//Get names
		for(int j=0; j<s; ++j)
			cin.getline(names[j], 105);
		cin>>q; cin.get();
		//Init to 0
		for(int j=0; j<s; ++j)
			arr[j]=0;
		//Get queries
		char w[105];
		for(int j=0; j<q; ++j){
			cin.getline(w, 105);
			int x=getn(w);
			if(x!=-1){
				for(int k=0; k<s; ++k){
					arr[k]=(arr[k]<arr[x]+1)?arr[k]:(arr[x]+1);
				}
				arr[x]=999999;
			}
		}
		//Get minimum
		cout<<"Case #"<<i+1<<": ";
		int mini=arr[0];
		for(int j=0; j<s; ++j){
			mini=(mini<arr[j])?mini:arr[j];
		}
		cout<<mini<<endl;
	}	
	
	return 0;
}

int getn(char w[]){
	for(int i=0; i<s; ++i)
		if(strcmp(names[i], w)==0)
			return i;
	return -1;
}

