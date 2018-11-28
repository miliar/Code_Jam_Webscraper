#include<cstdio>
#define MX 1010
using namespace std;
typedef long long ll;
int fin[MX];
ll sum[MX];
ll data[MX];
int main(){
	int runs ;
	int R;
	int N;
	int k;
	int cont = 1;
	scanf("%d",&runs);
	while(runs--){
		scanf("%d%d%d",&R,&k,&N);
		for(int i = 0 ; i < N ; i++)
			scanf("%Ld",&data[i]);
		int point = 0;
		for(int i = 0 ; i < N ; i++){
			point = i;
			sum[i] = 0;
			while(sum[i] < k){
				sum[i] += data[point];
				point++;
				point%=N;
				if(point == i) break;
				if(sum[i] + data[point] > k) break;
			}
			fin[i] = point;
		}
		int next = 0;
		ll res = 0;
		for(int time = 0 ; time < R ; time++){
			res += sum[next];
			next = fin[next];
		}
		printf("Case #%d: %Ld\n",cont++,res);
	}
	return 0;
}
