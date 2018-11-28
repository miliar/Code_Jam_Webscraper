#include <iostream>
#include <cstdio>
#include <cstring>
#include<string>

using namespace std;

void next(string s){
	
	int size = s.length();
	int swap;
	int i;
	for(i=size-2; i>=0; i--){
		if(s[i]<s[i+1]){
			swap = i;
			break;
		}
	}
	
	if(i==-1){
		
		int index=0;
		
		for(int j=0; j<size; j++){
			if(s[j]!='0'){
				index = j;
			}
		}
		
		cout<<s[index];
		cout<<'0';
		
		for(int j=size-1; j>=0; j--){
			if(j!=index)
			cout<<s[j];
		}
		
		
		/*
		string ans = "";
		
		for(int j=size-1; j>=0; j--){
			if(s[j]=='0')
			break;
			else{
				ans+= s[j];
			}
		}
		
		/*
		while(ans.length()<=size){
			ans = ans[0]+'0'+ans.substr(1,ans.length()-1);
		}
		
		
		return ans;
		*/
	}
	else{
		int swap1 = swap+1;
		
		for(int j=swap+1; j<size; j++){
			if(s[j]>s[swap])
			swap1 = j;
		}
		
		char temp = s[swap];
		s[swap] = s[swap1];
		s[swap1] = temp;
		
		for(int j=swap+1; ; j++){
			int k = size-1+swap+1-j;
			
			if(k<=j)
			break;
			else{
				temp = s[j];
				s[j] = s[k];
				s[k] = temp;
			}
		}
		cout<<s;
		//return s;
	}
	return;
}	
		

int main(){
	
	int t;
	
	cin>>t;
	
	for(int i=0; i<t; i++){
		
		string n;
		
		cin>>n;
		
		cout<<"Case #"<<i+1<<": ";
		next(n);
		cout<<endl;
		//next(n)<<endl;
		
	}
	
	return 0;
}
