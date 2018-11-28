#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T = 0;
    cin >> T;
    for (int c = 1; c <= T; c++)
    {
        int K = 0;
        cin >> K;
        
        vector<int> deck(K, 0);
        vector<int> cards(K, 0);
        for (int i = 1; i <= K; i++)
            deck[i - 1] = i;

        int pos = 0;
        int count = 0;
        for (int cur = 1; cur <= K; cur++)
        {
            count = 0;
            while (count != cur)
            {
                count++;
                if (count == cur)
                {
                    cards[deck[pos] - 1] = cur;
                    deck.erase(deck.begin() + pos);
                    if (deck.size())
                        pos %= deck.size();
                    continue;
                }
                pos = (pos + 1) % deck.size();
            }
        }
        
        int n = 0;
        cin >> n;
        int ind = 0;
        cout << "Case #" << c << ": ";
        for (int i = 0; i < n; i++)
        {
            cin >> ind;
            cout << cards[ind - 1];
            if (i != (n - 1))
                cout << " ";
        }
        cout << endl;
    }
    
    return 0;
}

