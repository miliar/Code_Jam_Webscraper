#include <iostream>
using namespace std;

int main(){
	int n, m, temp;
	char c;
	cin >> n;

	for(int i=0; i<n; i++){
		int o = 1, b = 1, result = 0, oBuff = 0, bBuff = 0;
		char curr = 'O';
		cin >> m;
		
	    for(int j=0; j<m; j++){
		    cin >> c >> temp;
		    
		    if(c=='O'){
				oBuff += abs(temp-o)+1;
				o = temp;
			}else{
                bBuff += abs(temp-b)+1;
				b = temp;
			}
			
			if(curr != c){
				if(c=='O' && oBuff <= bBuff){
					result += bBuff;
					oBuff = 1;
					bBuff = 0;
					curr = 'O';
				}else if(c=='B' && bBuff <= oBuff){
					result += oBuff;
					oBuff = 0;
					bBuff = 1;
					curr = 'B';
				}else if(oBuff > bBuff){
                    result += bBuff;
					oBuff -= bBuff;
					bBuff = 0;
					curr = 'O';
				}else if(bBuff > oBuff){
                    result += oBuff;
					bBuff -= oBuff;
					oBuff = 0;
					curr = 'B';
				}else{
					cerr << "Case #" << i+1 << ": " << "error" << endl;
				}
			}
		}
		result += max(oBuff,bBuff);
	
		cout << "Case #" << i+1 << ": " << result << endl;
	}
//	system("pause");
}
