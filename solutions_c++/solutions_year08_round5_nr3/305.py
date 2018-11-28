#include<iostream>
#include<fstream>
using namespace  std;

typedef long long ll;

ll F[2][2000];
ll G[100];
ll P[2000];

bool Map[1100][1100];

int C, M, N;
int tot;

int A[20], B[20];

int _calc(int k){
	int cnt = 0;
	for (int i=0;i<10;++i){
		A[i] = k % 2;
		k /= 2;
		
		if (A[i] == 1) cnt++;
		if ((i>0)&&(A[i]==1)&&(A[i-1]==1)) return -1;
	}
	
	return cnt;
}

bool _check(int k){
	int cnt = 0;
	for (int i=0;i<10;++i){
		B[i] = k % 2;
		k /= 2;
		
		if (B[i] == 1){
			if ((i>0)&&(A[i-1]==1)) return false;
			if ((i+1<10)&&(A[i+1]==1)) return false;
		}
	}
	
	return true;
}

int main(){
	ifstream cin("c1.in");
	ofstream cout("c1.ans");
	
	tot = (1<<10);
	for (int i=0;i<tot;++i){
		P[i] = _calc(i);
		for (int j=0;j<tot;++j)
			if (i>j)
				Map[i][j] = Map[j][i];
			else
				Map[i][j] = _check(j);
	}
	
	cin>>C;
	for (int Case=1; Case<=C; ++Case){
		cin>>M>>N;
		
		tot = (1<<N);
		
		char cc;
		for (int i=0;i<M;++i){
			int k=0;
			for (int j=0;j<N;++j){
				cin>>cc;
				k *= 2;
				if (cc=='x')k++;
			}
			G[i] = k;
		}
		
		memset(F, 0, sizeof(F));
		for (int i=0;i<M;++i){
			int now = i % 2;
			int pre = 1 - now;
			
			for (int ns=0;ns<tot;ns++)
				if ((P[ns] < 0)||((ns & G[i])!=0))
					F[now][ns] = 0;
				else {
					ll ret = 0;
					for (int ps=0;ps<tot;ps++)
						if (Map[ns][ps]) ret >?= F[pre][ps];
					F[now][ns] = ret + P[ns];
				}
		}
		
		ll ans = 0;
		int now = (M-1)%2;
		for (int ns=0;ns<tot;ns++)
			ans >?= F[now][ns];
		
		cout<<"Case #"<<Case<<": "<<ans<<endl;
	}
	
	return 0;
}
