#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <set>
#include <map>
#include <vector>
#include <bitset>

using namespace std;

int n,m;
int x[3000];
int y[3000];
int cl[10];
int res=-1;
int ans[10];
vector <int> s[2000];
vector <int> g[20];
int v=0;

set<pair<int,int> > st;

void check(){
	int num=0;
	int used[10];
	memset(used,0,sizeof(used));
	for (int i=1; i<=n; i++)
		used[cl[i]]=1;
	for (int i=1; i<=n; i++)
		num+=used[i];

	for (int i=0; i<v; i++){
		memset(used,0,sizeof(used));
		for (int j=0; j<s[i].size(); j++)
			used[cl[s[i][j]]]=1;
		int k=0;
		for (int j=1; j<=n; j++)
			k+=used[j];
		if (k!=num) return;
	}

	if (num>res){
		res=num;
		for (int i=1; i<=n; i++)
			ans[i]=cl[i];
	}

}

void rec(int x){
	if (x==n+1){
		check();
		return;
	}
	for (int i=1; i<=n; i++)
		cl[x]=i, rec(x+1);
}

/*void rec(vector <int> cur){
	if (cur[0]==cur[(int)cur.size()-1]&&cur.size()>1){
		s[v]=cur;
		v++;
		return;
	}

	int st=cur[0];
	int tk=cur[cur.size()-1];
	if (g[tk].size()==0){
		int nw=tk+1;
		if (nw==n+1) nw=1;
		cur.push_back(nw);
		rec(cur);
	} else
	{

	}
}*/

int ins(int a,int b,int c,int d){
	if (a>b) swap(a,b);
	if (c>d) swap(c,d);
	int used[2];
	used[1]=used[0]=0;
	if (a>c&&a<d) used[1]=1;
	if (b>c&&b<d) used[1]=1;
	if (a<c&&a>d) used[0]=1;
	if (b<c&&b>d) used[0]=1;
	return used[0]&&used[1];
}

void find(){
	/*for (int i=1; i<=n; i++){
		vector <int> tek;
		tek.push_back(i);
		rec(tek);
	}*/

	for (int i=1; i<(1<<n); i++){
		bitset<10> b=i;
		if (b.count()>2){
			vector <int> vt;
			for (int j=0; j<10; j++)
				if (b[j]) vt.push_back(j+1);
			vt.push_back(vt[0]);
			int gd=1;
			for (int j=0; j<vt.size()-1; j++)
				if (!st.count(make_pair(vt[j],vt[j+1]))) gd=0;

			int pt=0;
			for (int j=0; j<vt.size()-1; j++)
				for (int k=j+1; k<vt.size()-1; k++)
					if (st.count(make_pair(vt[j],vt[k]))) pt++;

			if (pt!=vt.size()-1) gd=0;

			vector <pair<int,int> > d;
			for (int j=0; j<vt.size()-1; j++)
				d.push_back(make_pair(vt[j],vt[j+1]));

			for (set<pair<int,int> >::iterator it=st.begin(); it!=st.end(); it++){
				int x=it->first;
				int y=it->second;
				for (int j=0; j<d.size(); j++)
					if (ins(x,y,d[j].first,d[j].second)) gd=0;
			}


			if (gd){
				s[v]=vt;
				v++;
			}
		}
	}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;

	scanf("%d\n",&tests);
	for (int tt=1; tt<=tests; tt++){
		cerr<<tt<<endl;
		st.clear();
		printf("Case #%d: ",tt);
		scanf("%d%d",&n,&m);
		for (int i=0; i<m; i++)
			scanf("%d",&x[i]);
		for (int i=0; i<m; i++)
			scanf("%d",&y[i]);
		for (int i=0; i<m; i++)
			g[x[i]].push_back(y[i]),
			g[y[i]].push_back(x[i]);

		for (int i=0; i<m; i++)
			st.insert(make_pair(x[i],y[i])),
			st.insert(make_pair(y[i],x[i]));

		for (int i=1; i<=n; i++){
			int nx=i+1;
			if (nx==n+1) nx=1;
			st.insert(make_pair(i,nx));
			st.insert(make_pair(nx,i));
		}
		
		res=-1;
		v=0;
		find();
		rec(1);
		printf("%d\n",res);
		for (int i=1; i<=n; i++)
			printf("%d ",ans[i]);
		printf("\n");
	}	

	return 0;
}