#include<iostream>
using namespace std;

int main(){
	int i,j,k,n,m,r,cases,ii,jj,kk;
	char a[105][105];
	double wp[105],owp[105],oowp[105],wp1[105];
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	cin>>r;
	cout.setf(ios::fixed);
	cout.precision(11);
	for(cases=1;cases<=r;cases++){
		cin>>n;
		for(i=0;i<n;i++){
			for(j=0;j<n;j++)
				cin>>a[i][j];
		}
		for(i=0;i<n;i++)
			wp[i]=owp[i]=oowp[i]=0;
		for(i=0;i<n;i++){
			k=0;
			for(j=0;j<n;j++){
				if(a[i][j]=='.')
					continue;
				if(a[i][j]=='1')
					wp[i]+=1;
				k++;
			}
			wp[i]/=k;
//			cout<<i<<"  "<<wp[i]<<endl;
		}
		for(i=0;i<n;i++){
			k=0;
			for(j=0;j<n;j++){
				if(a[i][j]!='.'){
					k++;
					kk=0;
					wp1[j]=0;
					for(ii=0;ii<n;ii++){
						if(ii==i)
							continue;
						if(a[j][ii]=='.')
							continue;
						kk++;
						if(a[j][ii]=='1')
							wp1[j]+=1;
					}
					owp[i]+=wp1[j]/kk;
				}
			}
			owp[i]/=k;
//			cout<<i<<"  "<<owp[i]<<endl;
		}
		for(i=0;i<n;i++){
			k=0;
			for(j=0;j<n;j++){
				if(a[i][j]!='.'){
					k++;
					oowp[i]+=owp[j];
				}
			}
			oowp[i]/=k;
//			cout<<i<<"  "<<oowp[i]<<endl;
		}
		printf("Case #%d:\n",cases);
		for(i=0;i<n;i++){
			cout<<wp[i]/4+owp[i]/2+oowp[i]/4<<endl;
		}
	}
}