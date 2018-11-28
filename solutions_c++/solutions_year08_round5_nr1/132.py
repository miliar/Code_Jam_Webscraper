#include <algorithm>
#include <cstring>
#include <set>
#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <numeric>
#include <cctype>

using namespace std;

#define fo(i,n) for(int i=0;i<n;i++)
#define fi fo(i,n)
#define fj fo(j,n)
#define go(i,v) for(typeof(v.begin()) i=v.begin();i!=v.end();i++)

typedef long long LL;
typedef long double LD;

int get(){int x; scanf("%d",&x); return x;}

string getseq(){
	int n=get();
	char s[40];
	string ret;
	fi{
		scanf("%s",&s);
		int rep=get();
		fo(j,rep)ret+=s;
	}
	if(ret[ret.size()-1]=='F')ret+='L';
	return ret;
}

int maxr[6001],minr[6001];
int maxc[6001],minc[6001];

int put(int r,int c){
	if(maxr[c]==-1||maxr[c]<r)maxr[c]=r;
	if(minr[c]==-1||minr[c]>r)minr[c]=r;
	if(maxc[r]==-1||maxc[r]<c)maxc[r]=c;
	if(minc[r]==-1||minc[r]>c)minc[r]=c;
}

int soln(){
	memset(maxr,0xFF,sizeof(maxr));
	memset(minr,0xFF,sizeof(minr));
	memset(maxc,0xFF,sizeof(maxc));
	memset(minc,0xFF,sizeof(minc));
	string seq=getseq();
	int n=seq.size();
	int dr[]={-1,0,1,0};
	int dc[]={0,1,0,-1}; // turn to the right = +1
	int dir=0;
	int r=3000,c=3000,lr,lc;
	int shape=0;
	fi{
		put(r,c);
		if(r==lr&&c!=lc&&i) shape+=(c-lc)*r;
		lc=c;
		lr=r;
		if(seq[i]=='F'){
			r+=dr[dir];
			c+=dc[dir];
		} else if(seq[i]=='L'){
			dir--;
			if(dir==-1)dir=3;
		} else if(seq[i]=='R'){
			dir++;
			if(dir==4)dir=0;
		}
	}
	if(shape<0)shape=-shape;
	fo(i,6001){
		if(minc[i]!=-1)
			for(int j=minc[i];j<=maxc[i];j++)
				put(i,j);
	}
	int everything=0;
	fo(i,6001)if(i&&maxr[i]!=-1&&maxr[i-1]!=-1)everything+=min(maxr[i],maxr[i-1]);
	fo(i,6001)if(i&&minr[i]!=-1&&minr[i-1]!=-1)everything-=max(minr[i],minr[i-1]);
	return everything-shape;
}

int main(){
	int n=get();
	fi{
		int ans=soln();
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
