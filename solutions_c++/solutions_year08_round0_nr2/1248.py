#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

#include <string.h>
#define MAXN 256
#define _clr(x) memset(x,0xff,sizeof(int)*MAXN)

int hungary(int m,int n,int mat[][MAXN],int* match1,int* match2){
	int s[MAXN],t[MAXN],p,q,ret=0,i,j,k;
	for (_clr(match1),_clr(match2),i=0;i<m;ret+=(match1[i++]>=0))
		for (_clr(t),s[p=q=0]=i;p<=q&&match1[i]<0;p++)
			for (k=s[p],j=0;j<n&&match1[i]<0;j++)
				if (mat[k][j]&&t[j]<0){
					s[++q]=match2[j],t[j]=k;
					if (s[q]<0)
						for (p=j;p>=0;j=p)
							match2[j]=k=t[j],p=match1[k],match1[k]=j;
				}
	return ret;
}


bool earlier(pair<int,int> a,pair<int,int> b,int t){
	a.second+=t;
	if(a.second>=60)a.second-=60,a.first++;

	if(a<=b)return 1;return 0;
}


int main(){

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);


	int n;
	cin>>n;
	for(int ca=1;ca<=n;ca++){
		int t;
		cin>>t;
		int na,nb;
		cin>>na>>nb;

		vector<pair<pair<int,int>,pair<int,int> > > ta;
		for(int i=0;i<na;i++){
			pair<int,int> start;
			pair<int,int> end;
			char tmp;
			cin>>start.first>>tmp>>start.second;
			cin>>end.first>>tmp>>end.second;
			ta.push_back(make_pair(start,end));
		}

		vector<pair<pair<int,int>,pair<int,int> > > tb;
		for(int i=0;i<nb;i++){
			pair<int,int> start;
			pair<int,int> end;
			char tmp;
			cin>>start.first>>tmp>>start.second;
			cin>>end.first>>tmp>>end.second;
			tb.push_back(make_pair(start,end));
		}

		int con[MAXN][MAXN]={0};
		for(int i=0;i<na;i++){
			for(int j=0;j<nb;j++){
				if(earlier(ta[i].second,tb[j].first,t))
					con[i][na+j]=1;
				if(earlier(tb[j].second,ta[i].first,t))
					con[na+j][i]=1;
			}
		}


		int m1[MAXN];
		int m2[MAXN];
		hungary(na+nb,na+nb,con,m1,m2);

		int ansa=0;
		for(int i=0;i<na;i++)
			if(m2[i]==-1)ansa++;

		int ansb=0;
		for(int i=na;i<na+nb;i++)
			if(m2[i]==-1)ansb++;

		cout<<"Case #"<<ca<<": "<<ansa<<" "<<ansb<<endl;
	}
}