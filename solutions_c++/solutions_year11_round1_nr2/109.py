#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

int b[10000][26];
string s[10000];
string o;
int w[10000];

bool cmp(int x,int y){
	if(s[x].length()!=s[y].length())
		return s[x].length()<s[y].length();
	for(string::iterator j=o.begin();j!=o.end();j++)
		if(b[x][*j]!=b[y][*j])
			return b[x][*j]>b[y][*j];
	return false;
}

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n,m;
		cin>>n>>m;
		memset(b,0,n*sizeof *b);
		for(int j=0;j<n;j++){
			string &t=s[j];
			cin>>t;
			for(int k=0;k<t.length();k++)
				b[j][t[k]<'a'?t[k]-'A':t[k]-'a']|=1<<k;
		}
		cout<<"Case #"<<i<<":";
		for(int j=0;j<m;j++){
			cin>>o;
			for(int k=0;k<26;k++)o[k]-=o[k]<'a'?'A':'a';
			for(int k=0;k<n;k++)w[k]=k;
			sort(w,w+n,cmp);
			int st[26]={0},l=0,a=0,r=0;
			for(int k=1;k<n;k++)
				if(s[w[k]].length()!=s[w[k-1]].length())
					st[0]=l=0;
				else{
					int h;
					for(h=0;h<26;h++)if(b[w[k]][o[h]]!=b[w[k-1]][o[h]])break;
					for(;l<h;l++)st[l+1]=st[l];l=h;
					if(b[w[k]][o[h]]==0)st[l]++;
					if(st[l]>r||(st[l]==r&&w[k]<a)){
						a=w[k];
						r=st[l];
					}
				}
			cout<<" "<<s[a];
		}
		cout<<endl;
	}
	return 0;
}

