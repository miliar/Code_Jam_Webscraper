#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

const int _md = 10007;

int N, R;
int W, H;
int cnt[200][200];

int main(){
	ifstream cin("d2.in");
	ofstream cout("d2.an");
	
	cin>>N;
	
	for (int Case=1; Case<=N; Case++){
		cin>>H>>W>>R;
		
		memset(cnt, 255, sizeof(cnt));
		cnt[1][1] = 1;
		for (int k=0;k<R;++k){
			int i, j;
			cin>>i>>j;
			cnt[i][j] = 0;
		}
		
		for (int i=1; i<=H; ++i)
			for (int j=1; j<=W; ++j)
				if (cnt[i][j] < 0){
					cnt[i][j] = 0;
					
					if ((1<=i-1)&&(1<=j-2))
						cnt[i][j] += cnt[i-1][j-2];
					if ((1<=i-2)&&(1<=j-1))
						cnt[i][j] += cnt[i-2][j-1];
					
					cnt[i][j] %= _md;
				}
				
		cout<<"Case #"<<Case<<": "<<cnt[H][W]<<endl;
	}
	
	return 0;
}
