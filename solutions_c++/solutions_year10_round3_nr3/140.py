#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<list>
using namespace std;
char he[16]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int tt;
	cin>>tt;
	for(int t=1;t<=tt;++t){
		int m,n;
		cin>>m>>n;
		vector<vector<int> >a(m,vector<int>(n));
		for(int i=0;i<m;++i){
			string st;
			cin>>st;
			for(int i1=0;i1<n/4;++i1){
				int value=0;
				while(he[value]!=st[i1])
					value++;
				a[i][i1*4]=value>>3;
				a[i][i1*4+1]=(value>>2)%2;
				a[i][i1*4+2]=(value>>1)%2;
				a[i][i1*4+3]=value%2;
			}
		}
		vector<vector<int> >cels(m,vector<int>(n,1));
		for(int i=1;i<m;++i){
			//cout<<cels[i][0];
			for(int i1=1;i1<n;++i1){
				if(a[i][i1]==a[i-1][i1-1] && a[i][i1]!=a[i][i1-1] && a[i][i1]!=a[i-1][i1]){
					cels[i][i1]=min(cels[i-1][i1-1],min(cels[i][i1-1],cels[i-1][i1]))+1;
				}
				/*if(cels[i][i1]<10)
						cout<<' ';
					cout<<cels[i][i1]<<' ';*/
			}
			//cout<<endl;
		}
		vector<int>rez(550,0);

		while(1){
			int ma=0;
			int mai;
			int mai1;
			for(int i=0;i<m;++i){
				for(int i1=0;i1<n;++i1){
					if(cels[i][i1]>ma){
						ma=cels[i][i1];
						mai=i;
						mai1=i1;
					}
				}
			}

			if(ma==0)
				break;

			rez[ma]++;
			for(int i=mai-ma+1;i<=mai;++i)
				for(int i1=mai1-ma+1;i1<=mai1;++i1)
					cels[i][i1]=0;

			for(int i=max(1,mai-ma+1);i<min(m,mai+ma+1);++i){
			//cout<<cels[i][0];
				for(int i1=max(1,mai1-ma+1);i1<min(n,mai1+ma+i);++i1){
					if(cels[i][i1]==0)
						continue;
					if(a[i][i1]==a[i-1][i1-1] && a[i][i1]!=a[i][i1-1] && a[i][i1]!=a[i-1][i1]){
						cels[i][i1]=min(cels[i-1][i1-1],min(cels[i][i1-1],cels[i-1][i1]))+1;
					}

				}
			}

		}

		int k=0;
		for(int i=0;i<rez.size();++i)
			k+=rez[i]!=0;
		cout<<"Case #"<<t<<": ";
		cout<<k<<endl;
		for(int i=rez.size()-1;i>=0;--i){
			if(rez[i])
				cout<<i<<' '<<rez[i]<<endl;
		}
		//cout<<endl;
	}
	return 0;
}