#include <iostream>
#include <cstring>

using namespace std;

int a[1010];
int b[1010];
int used[1010]; //0 none - 1 - 1-star 2 - 2-star

int main(){
	ios::sync_with_stdio(false);
	int t, n;
	
	cin >> t;
	for(int tc = 1; tc <= t; tc++){
		cin >> n;
		for(int i = 0; i < n; i++){
			cin >> a[i] >> b[i];
			used[i] = false;
		}
		
		int stars = 0, level = 0;
		
		while(stars < 2*n){
			//2-star
			int p2 = -1;
			for(int i = 0; i < n; i++) if(used[i] != 2){
				if(b[i] <= stars){
					p2 = i;
					break;
				}
			}
			if(p2 != -1){
				level++;
				stars += 2 - used[p2];
				used[p2] = 2;
				continue;
			}
			
			//1-star
			int p1 = -1, best = -1;
			for(int i = 0; i < n; i++) if(!used[i]){
				if(a[i] <= stars && b[i] > best){
					p1 = i;
					best = b[i];
				}
			}
			
			if(p1 != -1){
				level++;
				stars++;
				used[p1] = 1;
			}
			else{
				break;	
			}
		}
		
		cout << "Case #" << tc << ": ";
		if(stars < 2*n){
			cout << "Too Bad\n";
		}
		else{
			cout << level << "\n";
		}
	}
	
	return 0;	
}
