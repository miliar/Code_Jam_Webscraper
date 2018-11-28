/*#include<iostream>
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
}*/


/*
#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;

struct node{
	int num;
	double p;
	friend bool operator <(node nd1, node nd2){
		return nd1.p<nd2.p;
	}
};

int main(){
	int r,n,m,i,j,k,cases;
	double d,t,s;
	node nd[25];
	bool f;
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	cin>>r;
	cout.setf(ios::fixed);
	cout.precision(1);
	for(cases=1;cases<=r;cases++){
		cin>>m>>d;
		for(i=0;i<m;i++)
			cin>>nd[i].p>>nd[i].num;
		sort(nd,nd+m);
		for(t=0;;t+=0.5){
			s=-1000000;
			for(i=0;i<m;i++){
				f=true;
				for(j=0;j<nd[i].num;j++){
					if(nd[i].p-t+j*d>s+d)
						s=nd[i].p-t+j*d;
					else{
						s=s+d;
						if(s>nd[i].p+t){
							f=false;
							break;
						}
					}
				}
				if(!f)
					break;
			}
			if(f){
				printf("Case #%d: ",cases);
				cout<<t<<endl;
				break;
			}
		}
	}

}*/


#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;

struct node{
	int num;
	double p;
	friend bool operator <(node nd1, node nd2){
		return nd1.p<nd2.p;
	}
};

int main(){
	int r,n,m,i,j,k,cases;
	long long inc;
	double d,t,s;
	node nd[205];
	bool f;
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	cin>>r;
	cout.setf(ios::fixed);
	cout.precision(1);
	for(cases=1;cases<=r;cases++){
		cin>>m>>d;
		t=0;
		for(i=0;i<m;i++){
			cin>>nd[i].p>>nd[i].num;
			if((nd[i].num-1)*d/2>=t)
				t=(nd[i].num-1)*d/2;
		}
		sort(nd,nd+m);
		for(;;){
			s=-10e14;
			for(i=0;i<m;i++){
				f=true;
//				for(j=0;j<nd[i].num;j++){
					if(nd[i].p-t+(nd[i].num-1)*d>s+d*nd[i].num)
						s=nd[i].p-t+(nd[i].num-1)*d;
					else{
						s=s+d*nd[i].num;
						if(s>nd[i].p+t){
							inc=(long long)((s-nd[i].p-t)*2);
							inc/=4;
							if(inc==0)
								t+=0.5;
							else
								t+=inc;
							f=false;
							break;
						}
					}
				if(!f)
					break;
			}
			if(f){
				printf("Case #%d: ",cases);
				cout<<t<<endl;
				break;
			}
		}
	}

}