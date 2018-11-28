#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;

const int maxn=110;

int na,nb,T,test=0;
string da[maxn],aa[maxn],db[maxn],ab[maxn];
int check[maxn];

void init(){
	cin >> T;
	cin >> na >> nb;
	for (int i=0;i<na;i++) cin >> da[i] >> aa[i];
	for (int i=0;i<nb;i++) cin >> db[i] >> ab[i];
}

int operator - (const string& a,const string& b){
	int aa=((a[0]-48)*10+a[1]-48)*60+(a[3]-48)*10+a[4]-48;
	int bb=((b[0]-48)*10+b[1]-48)*60+(b[3]-48)*10+b[4]-48;
	return aa-bb;
}

void work(){
	int ansa=na,ansb=nb;
	memset(check,0,sizeof(check));
	sort(aa,aa+na);
	sort(db,db+nb);
	for (int i=0;i<na;i++)
		for (int j=0;j<nb;j++)
			if (check[j]==0&&db[j]-aa[i]>=T){
				check[j]=1;
				ansb--;
				break;
			}
	memset(check,0,sizeof(check));
	sort(ab,ab+nb);
	sort(da,da+na);
	for (int i=0;i<nb;i++)
		for (int j=0;j<na;j++)
			if (check[j]==0&&da[j]-ab[i]>=T){
				check[j]=1;
				ansa--;
				break;
			}
	test++;
	cout << "Case #" << test << ": " << ansa << " " << ansb << endl;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Q;
	cin >> Q;
	while (Q>0){
		Q--;
		init();
		work();
	}
	return 0;
}