#include <iostream>

using namespace std;

int num[2000500];

int main(){
	int TEST; cin >> TEST;
	for(int test=1;test<=TEST;test++){
		int N; cin >> N;
		memset(num, 0, sizeof(num));
		int cur = 5000000;
		for(int i=0;i<N;i++){
			int a, b; cin >> a >> b;
			num[a+1000201] = b;
			if(b > 1) cur = min(cur, a+1000201); 
		}
		int ans = 0;
		while(cur<2000500){
			num[cur-1]++;
			num[cur  ]-=2;
			num[cur+1]++;
			if(num[cur-1] > 1) cur = cur-1;
			else if(num[cur] > 1) cur = cur;
			else if(num[cur+1] > 1) cur = cur+1;
			else{
				for(cur=cur+2;cur<2000500;cur++)
					if(num[cur]>1) break;
			}
//			bool flag = true;
//			for(int i=0;i<2000500;i++){
//				if(num[i]>1){
//					num[i-1]++;
//					num[i  ]-=2;
//					num[i+1]++;
//					flag = false;
//					break;
//				}
//			}
//			if(flag) break;
			ans++;
		}
		printf("Case #%d: %d\n", test, ans);
	}
}
