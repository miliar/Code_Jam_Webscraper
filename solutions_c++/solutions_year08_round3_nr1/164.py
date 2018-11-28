#include <iostream>
#include <algorithm>

using namespace std;

class Letter
{
    public:
        int number;
        int frequency;
        
        bool operator<(const Letter& k) const
        {
            return frequency < k.frequency;
        }
};

int N; // cases
int P; // max letters on a key
int K; // keys available
int L; // letters in alphabet

Letter letters[10000];

int presses[10000]; // Number of presses required for this letter.

int assigned[10000]; // Number of letters assigned to this key

int main()
{
    cin >> N;
    
    for(int i = 1; i <= N; ++i)
    {
        cin >> P >> K >> L;
        
        for(int j = 0; j < L; ++j)
        {
            cin >> letters[j].frequency;
            letters[j].number = j;
        }
        
        sort(letters, letters+L);
        reverse(letters, letters+L);
        
        unsigned long long times = 0;
        
       for(int j = 0; j < K; ++j)
           assigned[j] = 0;
        
        for(int j = 0; j < L; ++j)
        {
            presses[letters[j].number] = ++assigned[j%K];
        }
        
        for(int j = 0; j < L; ++j)
        {
            times += letters[j].frequency*presses[letters[j].number];
        }
        
        cout << "Case #" << i << ": " << times << endl;
    }
}

