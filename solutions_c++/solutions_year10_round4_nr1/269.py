#include<iostream>

using namespace std;

#define a1(j,l) s[(j)-(l)][l]
#define b1(j,l) s[k-1-(l)][(j)+(l)]

#define a2(j,l) s[l][(j)-(l)]
#define b2(j,l) s[(j)+(l)][k-1-(l)]

#define a3(j,l) s[k-1-(j)+(l)][l]
#define b3(j,l) s[l][(j)+(l)]

#define a4(j,l) s[k-1-(l)][(j)-(l)]
#define b4(j,l) s[k-1-(j)-(l)][k-1-(l)]

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int k;
		int s[51][51];
		cin>>k;
		for(int j=0;j<k;j++)
			for(int l=0;l<=j;l++)
				cin>>a1(j,l);
		for(int j=1;j<k;j++)
			for(int l=0;l+j<k;l++)
				cin>>b1(j,l);
		int h=10000,v=10000;
		for(int t=0;t<k;t++){
			try{
				for(int j=t;j<k;j++)
					for(int l=0;l+l<j-t;l++)
						if(a1(j,l)!=a1(j,j-t-l))
							throw 0;
				for(int j=1;j<k-t;j++)
					for(int l=0;l+l+j<k-t;l++)
						if(b1(j,l)!=b1(j,k-1-j-t-l))
							throw 0;
			}catch(int x){
				continue;
			}
			h=t;
			break;
		}
		for(int t=0;t<k;t++){
			try{
				for(int j=t;j<k;j++)
					for(int l=0;l+l<j-t;l++)
						if(a2(j,l)!=a2(j,j-t-l))
							throw 0;
				for(int j=1;j<k-t;j++)
					for(int l=0;l+l+j<k-t;l++)
						if(b2(j,l)!=b2(j,k-1-j-t-l))
							throw 0;
			}catch(int x){
				continue;
			}
			if(h>t)h=t;
			break;
		}
		for(int t=0;t<k;t++){
			try{
				for(int j=t;j<k;j++)
					for(int l=0;l+l<j-t;l++)
						if(a3(j,l)!=a3(j,j-t-l))
							throw 0;
				for(int j=1;j<k-t;j++)
					for(int l=0;l+l+j<k-t;l++)
						if(b3(j,l)!=b3(j,k-1-j-t-l))
							throw 0;
			}catch(int x){
				continue;
			}
			v=t;
			break;
		}
		for(int t=0;t<k;t++){
			try{
				for(int j=t;j<k;j++)
					for(int l=0;l+l<j-t;l++)
						if(a4(j,l)!=a4(j,j-t-l))
							throw 0;
				for(int j=1;j<k-t;j++)
					for(int l=0;l+l+j<k-t;l++)
						if(b4(j,l)!=b4(j,k-1-j-t-l))
							throw 0;
			}catch(int x){
				continue;
			}
			if(v>t)v=t;
			break;
		}
		cout<<"Case #"<<i<<": "<<(k+h+v)*(k+h+v)-k*k<<endl;
	}
}

