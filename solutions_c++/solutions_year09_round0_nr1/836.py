#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
int main(){
	int len,n,q;
	cin>>len>>n>>q;
	vector<string> v(n);
	for(int i=0;i<n;i++){
		cin>>v[i];
	}
	int count=0;
	for(int z=0;z<q;z++){
		string s;
		cin>>s;
		count =0;
		for(int i=0;i<n;i++){
			int index=0;
			for(int p=0;p<s.size();p++){
				bool flag =0;
				if(s[p]=='('){
					while(s[p]!=')'){
						if(s[p]==v[i][index]){
							flag=1;
							
						}
						p++;
					}
				}
				else{
					if(s[p]==v[i][index])
						flag =1;
				}
				if(flag)
					index++;
				else
					break;
			}
			if(index==len){
				++count;
			}
		}
		printf("Case #%d: %d\n",z+1,count);
	}
}
