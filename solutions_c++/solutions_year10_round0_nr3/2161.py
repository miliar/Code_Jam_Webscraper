#include<iostream>
#include<vector>
using namespace std;

int main(){
	long n,R,k,N,tmp;
	vector<long>g;
	
	
	cin >> n;
	
	for(int i=0;i<n;i++){
		cin >> R >> k >> N;
		g.clear();
		for(int j=0;j<N;j++){
			cin >> tmp;
			g.push_back(tmp);
		}
		
		long result = 0;
		long num    = 0;
		long tmp_sum = 0;
		long prev_num = 0;
		
		for(int j=0;j<R;j++){
			
			while(tmp_sum + g[num] <= k){
				//cout << g[num] << " ";
				tmp_sum += g[num];
				num ++;
				if(g.size() <= num){
					num = 0;
				}
				if(num == prev_num){
					break;
				}
			}
			//cout << tmp_sum << "add\n";
			result += tmp_sum;
			prev_num = num;
			tmp_sum = 0;
		}
		cout << "Case #" << i+1 << ": " << result << endl;
	}
	return 0;
}
