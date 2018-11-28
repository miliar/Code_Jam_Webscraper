#include <iostream>
#include <vector>

using namespace std;

int main ()
{

	int T, N;
    vector<int> O, B;
    vector<char> turns;
    char bot, cur;
    int num;
    int posO, posB;
    long long time;
    bool lock;
    
    cin>> T;
    
    for (int i=0; i<T; i++) {
        cin>> N;
        O.clear();
        B.clear();
        turns.clear();
        
        for (int j=0; j<N; j++) {
            cin>> bot >> num;
            
            if (bot == 'O') {O.push_back(num); turns.push_back('O');}
            else {B.push_back(num); turns.push_back('B');}
        }
        
        posO = 1; 
        posB = 1;
        time = 0;
        do {
            lock = false;
            if (O.size() != 0) {
                if (posO < O[0]) posO++;
                else if (posO > O[0]) posO--;
                else {
                    if (turns[0] == 'O') {O.erase(O.begin()); turns.erase(turns.begin()); lock = true;}
                }
            }
            if (B.size() != 0) {
                if (posB < B[0]) posB++;
                else if (posB > B[0]) posB--;
                else {
                    if (turns[0] == 'B' && !lock) {B.erase(B.begin()); turns.erase(turns.begin());}
                }
            }
            time++;
        } while (turns.size() != 0);
            
        
        cout<<"Case #"<<i+1<<": "<<time<<endl;
    }

	return 0;

}
