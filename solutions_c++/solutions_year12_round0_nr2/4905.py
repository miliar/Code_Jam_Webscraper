#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    int t = 0; cin >> t;
    for(int c = 1; c <= t; c++){
        int count = 0; 
        int n,s,p; cin >> n >> s >> p;
        for(int i = 0; i  < n; i++){
            int x = 0; cin >> x;
            if(3*p-2 <= x) count++;
            else{
                int g = max(p-2,0);
                if (p+g+g <= x and s != 0){
                    count++;
                    s--;
                }
            } 
            
        }
        cout << "Case #" << c << ": " << count << endl;
    
    }

    return 0;
}
