#include<iostream>
#include<vector>
using namespace std;

int key[5];
int i,j,k,l,maxi,mini,x,tc;
string s,st;

int main() {
	scanf("%d",&tc);
	for(x=1;x<=tc;x++) {
		scanf("%d",&k);
		cin>>s;
		st=s;
		for(i=0;i<5;i++) key[i]=i;
		mini=2000000000;
		do {
			l=0;
			for(i=0;i<(s.length()/k);i++) {
				for(j=0;j<k;j++) st[i*k+j]=s[i*k+key[j]];
			}
			maxi=1;
			for(i=1;i<st.length();i++) {
				if(st[i]!=st[i-1]) maxi++;
			}
			mini=min(mini,maxi);
			//cout<<st<<" "<<maxi<<endl;
			//getchar();
		} while(next_permutation(key,key+k));
		printf("Case #%d: ",x);
		cout<<mini<<endl;
	}
}

