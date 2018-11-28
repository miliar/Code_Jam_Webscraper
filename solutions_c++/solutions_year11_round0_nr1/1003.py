#include <iostream>
#include <vector>
#include <queue>
#include <cstdlib>

using namespace std;

int main(){
	int t, n, teste = 1;
	char c;
	int p;
	
	cin >> t;
	
	while(t--){
		queue<pair<int, char> >oper;
		queue<int> orange, blue;
		 
		cin >> n;
		for(int i = 0; i < n; i++){
			cin >> c >> p;
			oper.push(make_pair(p, c));
		
			if(c == 'O'){
				orange.push(p);
			}
			else{
				blue.push(p);
			}
		}
		
		int o_pos = 1, b_pos = 1;
		int sum = 0;
		
		while(!oper.empty()){
			pair<int, int> p = oper.front(); oper.pop();
			
			if(p.second == 'O'){
				orange.pop();
				int cost = abs(o_pos - p.first) + 1;
				sum += cost;
				o_pos = p.first;
				
				int b_dest = blue.front();
				if(abs(b_pos - b_dest) <= cost){
					b_pos = b_dest;
				}
				else{
					if(b_pos > b_dest) b_pos -= cost;
					else b_pos += cost;
				}
			}
			else{
				blue.pop();
				int cost = abs(b_pos - p.first) + 1;
				sum += cost;
				b_pos = p.first;
			
				int o_dest = orange.front();
				if(abs(o_pos - o_dest) <= cost){
					o_pos = o_dest;
				}
				else{
					if(o_pos > o_dest) o_pos -= cost;
					else o_pos += cost;
				}
			}
			//cout << "sum = " << sum << "orange " << o_pos << "blue " << b_pos << endl;
		}
							
		cout << "Case #" << teste++ << ": " << sum << "\n";
	}
	
	return 0;
} 		
			
			
