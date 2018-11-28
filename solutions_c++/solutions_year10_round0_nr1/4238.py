#include <iostream>
using namespace std;

int snapper[30] = {0}, flag[30] ={0};

void init(void){
    for(int i=0; i<30; i++){
        snapper[i] = flag[i] = 0;
    }
    flag[0] = 1;
}

void clear(int begin, int end){
    for(int i=begin; i<end; i++){
        flag[i] = 0;
    }
}

void snap(int n){
    for(int i=0; i<n; i++){
        if(flag[i])
            snapper[i] = snapper[i] ? 0 : 1;
    }

    for(int i=0; i<n; i++){
        if(flag[i] && snapper[i]){
            flag[i+1] = 1;
        }else{
            clear(i+1, n);
        }

    }
}
void view(int n){
    cout << "s ";
    for(int i=0; i<n; i++){
        cout << snapper[i] << " ";
    }
    cout << endl;
    
    cout << "f ";
    for(int i=0; i<n; i++){
        cout << flag[i] << " ";
    }
    cout << endl << endl;
}

int main(void){
    int t;
    cin >> t;

    for(int i=0; i<t; i++){
        init();
        
        int n, k;
        cin >> n >> k;
        
        // view(n);
        for(; k--; ){
            snap(n);
            // view(n);
        }
        
        cout << "Case #" << i+1 << ": ";
        if(flag[n-1] && snapper[n-1])
            cout << "ON" << endl;
        else
            cout << "OFF" << endl;
    }
    
    return 0;
}
