#include <iostream>

using namespace std;

#define NONE 0 
#define OPPOSE -1

int main(){
    char S[26][26];
    bool O[26][26];

    int T;
    cin >> T;
    for( int i = 0; i < T; i++ ){
        for(int j = 0; j < 26; j++ )
            for(int k = 0; k < 26; k++ ){
                S[j][k] = NONE;
                O[j][k] = false;
            }
        int C;
        int D;
        int N;
        cin >> C;
        for( int j = 0; j < C; j++){
            char baseA;
            char baseB;
            char combined;
            cin >> baseA;
            cin >> baseB;
            cin >> combined;
            int idxA = baseA - 'A';
            int idxB = baseB - 'A';
            S[idxA][idxB] = combined;
            S[idxB][idxA] = combined;
        }
        
        cin >> D;
        for( int j = 0; j < D; j++){
            char baseA;
            char baseB;
            cin >> baseA;
            cin >> baseB;
            int idxA = baseA - 'A';
            int idxB = baseB - 'A';
            
            O[idxA][idxB] = true;
            O[idxB][idxA] = true;
        }

        cin >> N;
        char *word = new char[N];
        int length = 0;
        for( int j = 0; j < N; j++){
            char nc;
            cin >> nc;
            word[length++] = nc;
            if( length > 1 ){
                int last = length - 2;
                int idxA = word[last] - 'A';
                int idxB = nc - 'A';
                if( S[idxA][idxB] != NONE ) {
                    word[last] = S[idxA][idxB];
                    length--;
                }
            }

            
            for(int k = 0; k < length; k++){
                int idxA = word[k] - 'A';
                int idxB = word[length-1] - 'A';
                if ( O[idxA][idxB] )
                    length = 0;
            }
        }
        cout << "Case #" << i+1 << ": [";
        bool flag = false;
        for( int j = 0; j < length; j++){
            if(flag)
                cout << ", ";
            flag = true;
            cout << word[j];
        }
        cout << "]" << endl;
    }
}
