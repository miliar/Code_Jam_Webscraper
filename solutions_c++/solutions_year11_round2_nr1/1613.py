#include<iostream>
using namespace std;
const int N =105;
int main(){
	char a[N][N];
	//freopen("A-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int n;
	double wp[N],owp[N],oowp[N],rpi[N];
	int T;
	int i,j,k;
	int cas=1;
	double tmp,count,tc;
	cin>>T;
	while(T--){
		cin>>n;
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));

		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				cin>>a[i][j];
		tmp=0;
		count=0;
		for(i=0;i<n;i++){
			tmp=count=0;
			for(j=0;j<n;j++){
				if(a[i][j]!='.')
					tmp++;
				if(a[i][j]=='1')
					count++;
			}
			wp[i]=count/tmp;
		}
		for(i=0;i<n;i++){
			count=0;
			for(j=0;j<n;j++){
				if(a[i][j]=='.')
					continue;
				tmp=tc=0;
				for(k=0;k<n;k++){
					if(k==i||a[j][k]=='.')
						continue;
					tmp++;
					if(a[j][k]=='1')
						tc++;
				}
				tc/=tmp;
				owp[i]+=tc;
				count++;
			}
			owp[i]/=count;
		}
		for(i=0;i<n;i++){
			count=0;
			for(j=0;j<n;j++){
				if(a[i][j]=='.')
					continue;
				oowp[i]+=owp[j];
				count++;
			}
			oowp[i]/=count;
		}
		cout<<"Case #"<<cas++<<":"<<endl;
		for(i=0;i<n;i++){
			rpi[i]=0.25*wp[i]+owp[i]*0.5+oowp[i]*0.25;
			cout<<rpi[i]<<endl;
		}
		
	}
	return 0;
}