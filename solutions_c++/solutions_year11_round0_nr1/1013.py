#include <iostream>
#include <queue>
#include <math.h>

using namespace std;

const char O = 'O';

int main(){

	int max;
	cin >> max;
	
	queue<int> qO, qB;
    queue<bool> q;
	
	for(int i = 0; i < max; i++){
        
        int max2;
        cin >> max2;
        
        //input
        for(int j = 0; j < max2; j++){
            
            char temp;
            int num;  
            cin >> temp;
            cin >> num;
            
            if(temp == O){
                qO.push(num);
                q.push(true);
            }else{
                qB.push(num);
                q.push(false);
            }
        }
            int total_time = 0;
            int pO = 1; int pB = 1;
            bool type; bool last_type = q.front(); int current = 0;
            //solve
            while(true){
                type = q.front(); q.pop();
                if(type == last_type){
                    if(type){
                        int t = abs(qO.front() - pO) + 1;
                        total_time += t; current += t;
                        pO = qO.front();
                        qO.pop();
                    }else{
                        int t = abs(qB.front() - pB) + 1;
                        total_time += t; current += t;
                        pB = qB.front();
                        qB.pop();
                    }
                }else{
                    if(type){
                        int t = abs(qO.front() - pO) + 1;
                        if(current < t){
                            total_time += t - current;
                            current = t - current;
                        }else{
                            total_time++;
                            current = 1;
                        }
                        pO = qO.front();
                        qO.pop();
                    }else{
                        int t = abs(qB.front() - pB) + 1;
                        if(current < t){
                            total_time += t - current;
                            current = t - current;
                        }else{
                            total_time++;
                            current = 1;
                        }
                        pB = qB.front();
                        qB.pop();
                    }
                }
                
                last_type = type;
                
                if(q.size() == 0) break;
                
            }
                
            cout << "Case #" << i+1 << ": " << total_time << endl;
            
        
        
	}
	
	return 0;
}