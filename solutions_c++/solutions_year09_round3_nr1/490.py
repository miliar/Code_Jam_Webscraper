#include<stdio.h>
#include<string>
#include<vector>
#include<iostream>

using namespace std;

int tc,t;
string s;
vector <int> ar;
int i,j;
long long res;
int co;

int main(){
	freopen("ayb2.in","r",stdin);
	freopen("ayb2.out","w",stdout);

	scanf("%d\n",&t);
	for(tc=1;tc<=t;tc++){
		getline(cin,s);
		ar.clear();
		ar.resize(128);
		for(i=0;i<128;i++) ar[i]=-1;
		j=0;
		res=0;
		co=0;
		for(i=0;i<s.length();i++){
			if(ar[s[i]]==-1){
				ar[s[i]]=j;
				if(j==0) ar[s[i]]=1;
				else if(j==1) ar[s[i]]=0;
				co++;
				j++;
			}
		}
		if(co<2) co=2;
		for(i=0;i<s.length();i++){
			//printf("%c %d\n",s[i],ar[s[i]]);
			res*=co;
			res+=ar[s[i]];
		}
		printf("Case #%d: %lld\n",tc,res);
	}

	return 0;
}