#include <iostream>
#include <string>

using namespace std;

int main(){
	int TEST; cin >> TEST;
	static long long m[512][513];
	long long wsum[513];
	long long sum[513];
	bool ok[512][512];
	for(int test=1;test<=TEST;test++){
		int R, C, D; cin >> R >> C >> D;
		for(int i=0;i<R;i++){
			string str; cin >> str;
			for(int j=0;j<C;j++) m[i][j] = str[j]-'0';
		}
		int res = 0;
		for(int size=min(R,C);size>2;size--){
			for(int i=0;i+size-1<R;i++){
				for(int j=0;j+size-1<C;j++){
					long long hsum = 0, vsum = 0;
					for(int x=0;x<size;x++){
						for(int y=0;y<size;y++){
							if(x%(size-1)==0&&(y%(size-1)==0)) continue;
							hsum += (2*x-size+1)*m[i+x][j+y];
							vsum += (2*x-size+1)*m[i+y][j+x];
						}
					}
					if(hsum == 0 && vsum == 0) res = size;
				}
			}
			if(res != 0) break;
		}
		/*
		int res = 0;
		for(int size=min(R,C);size>2;size--){
			memset(ok, false, sizeof(ok));
			for(int i=0;i<R;i++){
				wsum[i] = sum[i] = 0;
				for(int j=0;j<size;j++){
					wsum[i] += (2*j-size+1)*m[i][j];
					sum[i]  += m[i][j];
				}
			}
			for(int i=0;i+size-1<C;i++){
				long long cur = 0;
				for(int j=0;j<size-1;j++)
					cur += wsum[j];
				for(int j=0;j+size-1<R;j++){
					cur += wsum[j+size-1];
					if(cur-(-size+1)*(m[i][j]+m[i+size-1][j])-(size-1)*(m[i][j+size-1]+m[i+size-1][j+size-1]) == 0)
						ok[i][j] = true;
					cur -= wsum[j];
				}
				for(int j=0;j<R;j++){
					wsum[j] -= 2*sum[j];
					wsum[j] += (size+1)*m[j][i];
					wsum[j] += (size-1)*m[j][i+size];
					sum[j] += m[j][i+size] - m[j][i];
				}
			}

			for(int i=0;i<C;i++){
				wsum[i] = sum[i] = 0;
				for(int j=0;j<size;j++){
					wsum[i] += (2*j-size+1)*m[j][i];
					sum[i]  += m[j][i];
				}
			}
			for(int i=0;i+size-1<R;i++){
				long long cur = 0;
				for(int j=0;j<size-1;j++)
					cur += wsum[j];
				for(int j=0;j+size-1<C;j++){
					cur += wsum[j+size-1];
					if(ok[j][i]){
						if(cur-(-size+1)*(m[j][i]+m[j][i+size-1])-(size-1)*(m[j+size-1][i]+m[j+size-1][i+size-1])==0){
							res = size;
						}
					}
					cur -= wsum[j];
				}
				for(int j=0;j<C;j++){
					wsum[j] -= 2*sum[j];
					wsum[j] += (size+1)*m[i][j];
					wsum[j] += (size-1)*m[i+size][j];
					sum[j] += m[i+size][j] - m[i][j];
				}
			}

			if(res!=0) break;
		}
		*/
		if(res == 0)
			printf("Case #%d: IMPOSSIBLE\n", test);
		else
			printf("Case #%d: %d\n", test, res);

	}
}
