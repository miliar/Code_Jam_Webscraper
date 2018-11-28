#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

const int maxn=110;
const int maxm=1100;
const int maxlen=110;

int n,m,test=0;
char Name[maxn][maxlen];
char Query[maxm][maxlen];
int q[maxm];
int check[maxn];

void init(){
	scanf("%d\n",&n);
	for (int i=0;i<n;i++) cin.getline(Name[i],maxlen,'\n');
	scanf("%d\n",&m);
	for (int i=0;i<m;i++) cin.getline(Query[i],maxlen,'\n');
	memset(q,0,sizeof(q));
	for (int i=0;i<m;i++)
		for (int j=0;j<n;j++)
			if (strcmp(Query[i],Name[j])==0){
				q[i]=j;
				break;
			}
}

void work(){
	memset(check,0,sizeof(check));
	int ans=0,st=0,ed=0,total=0;

	while (ed<m){
		if (check[q[ed]]==1);
		else{
			total++;
			if (total==n){
				ans++;
				total=1;
				memset(check,0,sizeof(check));
			}
			check[q[ed]]=1;
		}
		ed++;
	}

	test++;
	cout << "Case #" << test << ": " << ans << endl;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int Q;
	scanf("%d\n",&Q);
	while (Q--){
		init();
		work();
	}
	return 0;
}