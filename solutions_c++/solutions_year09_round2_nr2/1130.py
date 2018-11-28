#include <iostream>
#include <algorithm>

#define DOUT(x) cout << #x << " = " << x << endl;

using namespace std;

string input;

static void solve_case(int i);

int main(void){
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        solve_case(i+1);
    }
    return 0;
}

void init(){
    input.clear();
}

void solve_case(int cn){
    init();
    cin >> input;

    int i = input.size()-1;
    for(;i > 0; --i){
        if(input[i] > input[i-1]){
            break;
        }
    }

    if(i == 0){
        input.insert(0,1,'0');
        i = 1;
    }
    
    int min_idx = i;
    for(int j = i+1; j < input.size(); j++){
        if(input[j] > input[i-1] && input[j] < input[min_idx])
            min_idx = j;
    }

    swap(input[i-1],input[min_idx]);
    sort(input.begin()+i,input.end()); 

    cout << "Case #" << cn << ": " << input << endl;
}
