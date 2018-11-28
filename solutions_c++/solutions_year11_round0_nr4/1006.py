#include <iostream>

using namespace std;

int main(){
    
	int max;
	cin >> max;
	
	for(int i = 0; i < max; i++){
        
        int sum = 0, temp, num;
        cin >> num;
        //input
        for(int j = 0; j < num; j++){
            cin >> temp;
            if(temp != j + 1){
                sum++;
            }
        }

        cout << "Case #" << i+1 << ": " << sum << ".000000" << endl;
	}
	
	return 0;
}