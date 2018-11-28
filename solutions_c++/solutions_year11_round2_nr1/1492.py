#include<fstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<queue>
using namespace std;
ifstream cin("1.txt");
ofstream cout("2.txt");
int t,m,n,sum,win,ju;
double now,wp[200],owp[200],oowp[200];
char tu[200][200];
int main()
{
	int i,j,k,l,ju;
	cin>>t;
	for(l=1;l<=t;l++){
		cin>>n;
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				cin>>tu[i][j];
		for(i=1;i<=n;i++){
			win=0;ju=0;
			for(j=1;j<=n;j++){
				if(tu[i][j]=='1') win++;
				if(tu[i][j]!='.') ju++;
			}
			wp[i]=double(win)/ju;
		}
		
		for(i=1;i<=n;i++){
			sum=0;now=0;
			for(j=1;j<=n;j++)if(tu[i][j]!='.'){
				win=0;ju=0;
				for(k=1;k<=n;k++){
					if(k==i) continue;
					if(tu[j][k]=='1')win++;
					if(tu[j][k]!='.') ju++;
				}
				now+=double(win)/ju;
				sum++;
			}
			owp[i]=now/sum;
		}
		
		for(i=1;i<=n;i++){
			now=0;sum=0;
			for(j=1;j<=n;j++)if(tu[i][j]!='.'){
				now+=owp[j];
				sum++;
			}
			oowp[i]=now/sum;
		}
		
		cout<<"Case #"<<l<<": "<<endl;
		for(i=1;i<=n;i++)
			cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
	}
	return 0;
}
