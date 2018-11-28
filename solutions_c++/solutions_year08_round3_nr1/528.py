#include <iostream>



using namespace std;



int main()
{
    int N, P, K, L;
    
    int count_N;
    long long ans;
    int press;
    int freq[1001]={0};
    int tmp;
    
    int i, j, k;
    
    cin >> N;
    
    for(count_N=1; count_N<=N; count_N++) {
        
        ans=0;
        press=1;
        k=0;
        
        cin >> P >> K >> L;
        
        for(i=1; i<=L; i++)
            cin >> freq[i];
        
        for(i=1; i<=L; i++){
            for(j=i+1; j<=L; j++) {
                if(freq[i]<freq[j]) {
                    
                    tmp = freq[i];
                    freq[i] = freq[j];
                    freq[j] = tmp;
                }

                    
            }
        
        }
        
        //for(i=1; i<=L; i++)
        //    cout << freq[i]<< ' ';
        //cout << endl;
            
        for(i=1; i<=L; i++){
            ans += press * freq[i];
            k+=1;
            if(k==K) {
                k=0;
                press++;
            } 
        }
        
        
        cout << "Case #" << count_N << ": " << ans << endl;
    }
    
    
}

