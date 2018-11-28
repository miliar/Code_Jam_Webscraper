#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<ctime>
#include<algorithm>
#include <map>

using namespace std;
#define SZ(v) ((int)v.size())
#define FOR(i,b,e) for(int i = b;i < e; ++i)
#define REP(i,v) FOR(i,0,SZ(v))
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<char> VC;
typedef long long int64;
typedef unsigned long long uint64;
const double pi=acos(-1.0);
const double eps=1e-11;
#define zero(x) memset(&x, 0, sizeof x);
#define NUM 600

int main(){
	char wd[20]="welcome to code jam";

	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	char st[NUM];
	int T;
	cin>>T;
	cin.getline(st,NUM);
	FOR(k,0,T){
		int l;
		cin.getline(st,NUM);
		l=strlen(st);

		int cnt[19][NUM];
		zero(cnt);
		FOR(i,0,19)
			if (i==0){
				if (st[0]==wd[i]) cnt[i][0]=1;else cnt[i][0]=0; 
				FOR(j,1,l) 
					if (st[j]==wd[i]) cnt[i][j]=cnt[i][j-1]+1;
					else cnt[i][j]=cnt[i][j-1];
			}
			else{

//			
				int cc[NUM];
				if (st[l-1]==wd[i]) cc[l-1]=1;else cc[l-1]=0;
				for(int j=l-2;j>=i;--j)
					if (st[j]==wd[i]) cc[j]=cc[j+1]+1;else cc[j]=cc[j+1];
				cc[l]=0;

				FOR(j,i,l){
					cnt[i][j]=cnt[i-1][i-1]*(cc[i]-cc[j+1]);
					FOR(m,i+1,j+1)
						cnt[i][j]+=((cnt[i-1][m-1]-cnt[i-1][m-2]+10000)%10000*(cc[m]-cc[j+1]+10000))%10000;
						cnt[i][j]=cnt[i][j]%10000;
				}
		
				
			}
			cout<<"Case #"<<k+1<<": ";
			if (cnt[18][l-1]<1000) cout<<0;
			if (cnt[18][l-1]<100) cout<<0;
			if (cnt[18][l-1]<10) cout<<0;
			cout<<cnt[18][l-1]<<endl;	
	}

	return 0;

}