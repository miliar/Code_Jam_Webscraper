#include <iostream>
#include <string>
#include <map>

using namespace std;

int a[101][1001];
int inp[1001];
map <string,int> mp;
int mpinx;

int main(){
	int t, s, q,res;
	string st;
	char cst[101];
	cin.getline(cst,102);
	t=atoi(cst);
	for(int tc=1;tc<=t;tc++){
		mpinx=0;
		res=1001;
		memset(a,-1,sizeof(a));
		memset(inp,-1,sizeof(inp));
		mp.clear();
		cin.getline(cst,102);
		s=atoi(cst);
		for(int i=0;i<s;i++){
			cin.getline(cst,102);
			st=string(cst);
			//cout<<"'"<<st<<"'"<<endl;
			mp[st]=mpinx++;
		}
		//cout<<s<<endl;
		cin.getline(cst,102);
		q=atoi(cst);
		for(int i=0;i<q;i++){
			cin.getline(cst,102);
			st=string(cst);
			if(mp.count(st)!=0)inp[i]=mp[st];
		}
		for(int i=0;i<s;i++){
			if(inp[0]!=i){
				a[i][0]=0;
			}
			else{ a[i][0]=1001;}
		}

		for(int i=1;i<q;i++){
			for(int j=0;j<s;j++){
				if(inp[i]==j){
					a[j][i]=1001;
					continue;
				}
				else{
					a[j][i]=a[j][i-1];
					for(int k=0;k<s;k++)
					if(k!=j){
						a[j][i]=min(a[j][i],a[k][i-1]+1);
					}
				}
			}
		}
		for(int i=0;i<s;i++)res=min(res,a[i][q-1]);
		if(res==-1)res=0;
		cout<<"Case #"<<tc<<": "<<res<<endl;
	}
}