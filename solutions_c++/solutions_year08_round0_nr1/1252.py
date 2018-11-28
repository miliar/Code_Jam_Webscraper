#include<iostream>
#include<string>
#include<queue>
#include<cstdio>
using namespace std;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int n;
	cin>>n;
	for(int t=1;t<=n;t++){
		queue<int> pos[128];
		char tmp[10240];

		string se[128];
		int s;
		cin>>s;
		gets(tmp);

		for(int i=0;i<s;i++){gets(tmp);se[i]=tmp;}

		string query[1024];
		int q;
		cin>>q;
		gets(tmp);

		for(int i=0;i<q;i++){gets(tmp);query[i]=tmp;}

		for(int i=0;i<q;i++){
			for(int j=0;j<s;j++){
				if(query[i]==se[j]){
					pos[j].push(i);
				}
			}
		}

		int ans=0;
		while(true){
			int maxi=-1;
			bool end=0;

			for(int i=0;i<s;i++){
				if(pos[i].empty()){
					end=1;
					break;
				}
				else{
					if(pos[i].front()>maxi)maxi=pos[i].front();
				}
			}
			ans++;
			if(end)break;

			for(int i=0;i<s;i++){
				while(!pos[i].empty() && pos[i].front()<maxi)pos[i].pop();
			}
		}

		cout<<"Case #"<<t<<": "<<ans-1<<endl;
	}
}