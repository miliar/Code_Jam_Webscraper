#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdlib>

using namespace std;

void read_input(vector<int>* buttons, vector<int>& who){
    map<string,int> index;
    index["B"] = 0;
    index["O"] = 1;
    int n;
    cin >> n;
	
    for(int i=0;i<n;++i){
	string robot;
	cin >> robot;
	int button;
	cin >> button;
	who.push_back(index[robot]);
	buttons[index[robot]].push_back(button);
    }
    
    buttons[0].push_back(0);
    buttons[1].push_back(0);
}

int num_steps(const vector<int>* buttons, const vector<int>& who){  
    int pos[2] = {1,1};
    int ind[2] = {0,0};
    int ret = 0;
    
    for(int i=0;i<who.size();++i){
	int cur = who[i];
	int steps = 1 + abs(pos[cur] - buttons[cur][ind[cur]]);
	pos[cur] = buttons[cur][ind[cur]];
	ret += steps;
	++ind[cur];
	
	int stepsother = min(steps, abs(buttons[1-cur][ind[1-cur]] - pos[1-cur]));
	
	if(pos[1-cur] < buttons[1-cur][ind[1-cur]]){
	    pos[1-cur] += stepsother;
	}
	else{
	    pos[1-cur] -= stepsother;
	}
    }
    
    return ret;
}

int main(){
    int t;
    cin >> t;
    
    for(int lp=1;lp<=t;++lp){
	vector<int> buttons[2];
	vector<int> who;
	
	read_input(buttons,who);
	
	cout << "Case #" << lp << ": " << num_steps(buttons,who) << "\n";
    }
    
    return 0;
}
