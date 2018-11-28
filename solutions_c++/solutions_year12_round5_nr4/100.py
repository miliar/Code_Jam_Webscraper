#include<iostream>
#include<cstdio>
#define MS 1009
using namespace std;
typedef long long ll;
char mc[10]="oieastbg";
int ac(char a){
	for(int i=0;i<8;i++){
		if(a==mc[i])
			return 26+i-(a-'a');
	}
	return 0;
}
int main(){
	int t,k;
	char s[MS];
	int dg[40];
	bool fd[40][40];
	cin>>t;
	//scanf("%d",&t);
	
	for(int z=1;z<=t;z++){
		cin>>k;
		cin>>s;
		for(int i=0;i<40;i++){
			dg[i]=0;
			for(int j=0;j<40;j++){
				fd[i][j]=false;
			}
		}
		for(int i=0;s[i+1]!='\0';i++){
			fd[s[i]-'a'][s[i+1]-'a']=true;
			fd[ac(s[i])+s[i]-'a'][s[i+1]-'a']=true;
			fd[s[i]-'a'][ac(s[i+1])+s[i+1]-'a']=true;
			fd[ac(s[i])+s[i]-'a'][ac(s[i+1])+s[i+1]-'a']=true;
		}
		ll tdg=0;
		ll tsp=0;
		for(int i=0;i<40;i++){
			for(int j=0;j<40;j++){
				dg[i]+=fd[i][j];
				dg[j]-=fd[i][j];
				tsp+=fd[i][j];
			}
		}
		for(int i=0;i<40;i++){
			if(dg[i]>0)
				tdg+=dg[i];
		}
		if(tdg>0)
			tdg--;
		cout<<"Case #"<<z<<": "<<(1+tsp+tdg);
		//printf("Case #%d: ",z);
		cout<<endl;
		//printf("\n");
	}
	return 0;
}
