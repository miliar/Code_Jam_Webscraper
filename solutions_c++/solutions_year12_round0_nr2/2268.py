#include <iostream>
#include <cstdio>
#include <cstring>
#include <stack>
#include <algorithm>
#include <vector>
using namespace std;



int main()
{

	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		cout<<"Case #"<<i+1<<": ";
		
		int N,s,p;
		cin>>N>>s>>p;
		int ar[105];
		int ans=0;	
		for(int j=0;j<N;j++)
			cin>>ar[j];		
		sort(ar, ar+N);
		vector<int> vc;
		for(int j=0;j<N;j++){
			int mx = (ar[j]+2)/3;
			if(mx>=p)ans++;
			if(ar[j]>=2 && ar[j]<=28){
				if(mx==p-1&& (ar[j]%3)!=1 && s>0){
					ans++;
					s--;
				}else{
					//vc.push_back();
				}
			}	
		}
		cout<<ans<<endl;

	}
/*
	for(char i = 'a'; i<='z';i++)
	{
		ap[ch[i]]=1;
	}
	for(char i = 'a'; i<='z';i++)
	{
		if(ch[i])printf("%c %c",i,ch[i]);
		else printf("%c ???",i);
		if(ap[i])printf(" v \n");
		else printf(" x \n");
	}*/


	return 0;
}
