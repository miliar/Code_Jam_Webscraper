#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;

vector<int>googler;

int main()
{
	freopen("sam.txt","r",stdin);
	freopen("ram1.txt","w",stdout);
	int n,t,i,s,temp,p;
	cin>>t;
	for(int q=1;q<=t;q++){
		printf("Case #%d: ",q);
		cin>>n>>s>>p;
		for(i=0;i<n;i++){
			cin>>temp;
			googler.push_back(temp);
		}
		sort(googler.begin(),googler.end());
		int answer=0;
		for(i=0;i<googler.size();i++){
			temp=googler[i];
			if(s){
				if( (3*p-4<=temp) && (temp>=2 && temp<=28) ){
					++answer;
					--s;
				}
			}
			else if(3*p-2<=temp)++answer;
		}
		cout<<answer<<endl;
		googler.clear();
	}
	return 0;
}