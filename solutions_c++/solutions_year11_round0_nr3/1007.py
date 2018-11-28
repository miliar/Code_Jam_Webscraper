#include <iostream>
#include <string>
#include <vector>


using namespace std;

int main(){
    
	int max;
	cin >> max;
	
	for(int i = 0; i < max; i++){
        
        vector<int> candy_bag;
        int bags, answer; int sum = 0; int real = 0;
        
        cin >> bags;
        //input
        for(int j = 0; j < bags; j++){
            cin >> answer;
            candy_bag.push_back(answer);
            sum = sum ^ answer;
            real += answer;
        }
        if(sum == 0){
            answer = -1;
            for(int j = 0; j < bags; j++){
                if (answer > candy_bag[j] || answer < 0) {
                    
                    answer = candy_bag[j];
                }
            }
            cout << "Case #" << i+1 << ": " << real - answer << endl;
        }else{
            
            cout << "Case #" << i+1 << ": NO" << endl;
        }
	}
	
	return 0;
}