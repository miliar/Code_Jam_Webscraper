#include <iostream.h>

int main() {
    
    unsigned int T;

    cin >> T;
    
    unsigned int i;
    for (i = 0; i < T; i++) {
        
        unsigned int N;
        cin >> N;
        
        unsigned int j;
        unsigned int thissidewindow[1000];
        unsigned int othersidewindow[10000];
/*
        for (j = 0; j < 10000; j++) {
            othersidewindow[j] = 0;
        }
  */      
        for (j = 0; j < N; j++) {
            cin >> thissidewindow[j];
            cin >> othersidewindow[thissidewindow[j]];
        }

        unsigned long long intersection = 0;

        for (j = 0; j < N-1; j++) {
            unsigned int k;
            for (k = j+1; k < N; k++) {
                if (
                          (thissidewindow[j] < thissidewindow[k]) && 
                          (othersidewindow[thissidewindow[j]] > othersidewindow[thissidewindow[k]])
                   ) intersection++;
                else 
                if (
                          (thissidewindow[j] > thissidewindow[k]) && 
                          (othersidewindow[thissidewindow[j]] < othersidewindow[thissidewindow[k]])
                   ) intersection++;
            }
        }
        
        cout << "Case #" << i+1 << ": " << intersection << endl;
    }
}
