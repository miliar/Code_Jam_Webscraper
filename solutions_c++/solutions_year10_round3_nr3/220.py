
#include<iostream>
#include<stdio.h>

using namespace std;

int T,M,N;
int mat[515][515];
int res,a[515],b[515];
char ch[515];

bool find(int r, int l, int n){
	int i,j;
	int flag=(mat[r][l]+1)%2;

	for(j=l; j<l+n; j++){
		if(mat[r][j]>1 || flag==mat[r][j]) return false;
		flag=(flag+1)%2;
	}

	for(i=r+1; i<r+n; i++){
		if(mat[i][l]>1 || mat[i-1][l]==mat[i][l]) return false;

		flag=(mat[i][l]+1)%2;
		for(j=l; j<l+n; j++){
			if(mat[i][j]>1 || flag==mat[i][j]) return false;
			flag=(flag+1)%2;
		}
	}

	return true;
}

void change(int r, int l, int n){
	int i,j;
	for(i=r; i<r+n; i++){
		for(j=l; j<l+n; j++){
			mat[i][j]=2;
		}
	}
}

void count(int n){
	int i,j;

	for(i=0; i<=M-n; i++){
		for(j=0; j<=N-n; j++){
			if(find(i,j,n)){
				change(i,j,n);
				b[res]++;
			}
		}		
	}
}

void deal(int c, int i, int j){
	for(int k=j*4+3; k>=j*4; k--){
		mat[i][k]=c%2;
		c>>=1;
	}
}

int numb(char ch){
	switch(ch){
		case 'F': return 15;
		case 'E': return 14;
		case 'D': return 13;
		case 'C': return 12;
		case 'B': return 11;
		case 'A': return 10;
		default: return ch-'0';
	}
}

int main(){
	freopen("C-large.in","r", stdin);
	freopen("C-large.in.out", "w", stdout);

	int cas=0,i,j,ans;
	cin>>T;

	while(cas++<T){
		cin>>M>>N;

		for(j=0; j<M; j++){
			scanf("%s", ch);
			for(i=0; i<N/4; i++){
				ans=numb(ch[i]);

				//cout<<ans<<" ......"<<endl;
				deal(ans,j,i);
			}
			//scanf("%ch", &ch);
		}

		/*for(i=0; i<M; i++){
			for()
		}*/

		int temp=M>N?N:M;
		res=0;

		for(i=temp; i>=1; i--){
			a[res]=i;
			b[res]=0;
			count(i);
			if(b[res]!=0) res++;

			//cout<<i<<"th:"<<endl;
		}

		cout<<"Case #"<<cas<<": "<<res<<endl;

		for(i=0; i<res; i++){
			cout<<a[i]<<" "<<b[i]<<endl;
		}
	}
	return 0;
}