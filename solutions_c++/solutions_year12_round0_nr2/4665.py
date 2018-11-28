#include <iostream>
#include <vector>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t=1; t<=T; t++){
            int N, S, p;
            cin >> N >> S >> p;
            vector<int> n(N);
            for(int i=0;i<N;i++) cin >> n[i];
            
            int tot = 0;
            for(int i=0;i<N;i++){
                    if(n[i] % 3 == 0){
                            if(n[i] / 3 >= p) tot++;
                            else if(n[i]/3 + 1 >= p && S && n[i] != 0){
                                 tot++;
                                 S--;
                            }
                    }
                    else if(n[i] % 3 == 1){
                            if(n[i] / 3 + 1 >= p) tot++;
                    }
                    else {
                            if(n[i] / 3 + 1 >= p) tot++;
                            else if(n[i]/3 + 2 >= p && S){
                                 tot++;
                                 S--;
                            }
                    }
            }
            cout << "Case #" << t << ": ";
            cout << tot << endl;
    }
}
