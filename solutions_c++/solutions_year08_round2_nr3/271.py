#include <iostream>
#include <algorithm>
#include <deque>

int T, K, n,
    prints[1000002],
    deck[1000002];
std::deque<int> cards;

int main() {
    for (int i=0; i<1000002; i++) prints[i] = i+1;
    std::cin >> T;
    for (int t=0; t<T; t++) {
        std::cin >> K;
        cards.assign(prints, prints+K);
        int n_cards = K,
            ind = 0;
        for (int i=1; i<=K; i++) {
            ind = (ind+i-1) % n_cards;
            deck[cards[ind]] = i;
            //printf("drawing card %i from index %i\n", r, ind);
            cards.erase(cards.begin()+ind);
            n_cards--;
        }
        std::cin >> n;
        printf("Case #%d:", t+1);
        for (int i=0; i<n; i++) {
            std::cin >> K;
            std::cout << ' ' << deck[K];
        }
        std::cout << '\n';
    }
}
