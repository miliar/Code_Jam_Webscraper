#include <iostream>
#define Cmax 1048576
#define REP(i, to) for(int i=0; i<to; i++)

using namespace std;

int C[2][Cmax];
        
int main()
{   
    int T;
    cin >> T;
    
    for(int t=1; t<=T; t++){
        cout << "Case #" << t << ": ";
            
        REP(a,2) REP(i, Cmax) C[a][i]=-1; 
        C[0][0]=0;
        
        int N;
        cin >> N;
        
        int I[N];
        REP(i, N) 
            cin >> I[i];
            
        int xor_all = 0;
        int sum_all = 0;
        int min = 123456789;
        REP(i, N){
            sum_all += I[i];
            xor_all ^= I[i];
            if(I[i] < min) min = I[i];
        }
            
        if(xor_all != 0){
            cout << "NO";
        }else{
            cout << sum_all - min;
        }
        cout << endl;
        
        /* //I`m such a fool :) 
        int best = -1;
            
        REP(i, N) {
            cout << "Round: " << i+1 << endl;
            int* A = ((i%2) == 0) ? C[0] : C[1];
            int* B = ((i%2) == 0) ? C[1] : C[0];  
            
            REP(c, Cmax){
                if(A[c] < 0) continue;
                int cx=c ^ I[i];
                if(cx <= 0){
                    B[i] = I[i];
                    continue;      
                }
            
                int cs=A[c] + I[i];
                if(I[i] > cs) 
                    cs = I[i];
            
                if(cs > B[cx]) {
                    B[cx] = cs; 
                    if(cs > best)
                        best = cs;
                }
              
                cout << "C["<<cx<<"] = " << cs << endl;
            }
            
            REP(c, Cmax){
                if(A[c]>B[c])
                    B[c]=A[c];       
            }
        }
        
        cout << best << endl;
        */
    }
    
    return 0;    
}
