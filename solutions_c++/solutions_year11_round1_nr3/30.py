#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

struct Card
{
    int c, s, t;
    int real_c;
};


inline bool operator<(const Card& c1, const Card& c2)
{
    if (c1.c != c2.c) return c1.c > c2.c;
    if (min(c1.t, 1) != min(c2.t, 1)) return min(c1.t, 1) > min(c2.t, 1);
    return c1.s > c2.s;
}

int not_take(vector<Card>& h, int turns)
{
    vector<Card> hand = h;
    forv(i, hand) hand[i].c = 0;

    sort(all(hand));

    int score = 0;

    forv(i, hand)
    {
        turns += hand[i].t;    
        score += hand[i].s;

        turns--;

        if (turns == 0) break;
    }
    return score;
}

void solve(int test)
{
    printf("Case #%d: ", test);
        
    int n, m;
    cin >> n;
    vector<Card> hand(n);

    forn(i, n)
    {
        cin >> hand[i].c >> hand[i].s >> hand[i].t;        
        hand[i].real_c = hand[i].c;
    }

    cin >> m;
    queue<Card> deck;

    forn(i, m)
    {
        Card c; cin >> c.c >> c.s >> c.t;
        c.real_c = c.c;
        deck.push(c);
    }

    int score = 0;
    int turns = 1;

    int ans = 0;
    
    for (int it = 0; turns > 0 && !hand.empty(); it++, turns--)
    {
        forv(i, hand) hand[i].c = hand[i].real_c;

        ans = max(ans, score + not_take(hand, turns));

        if (deck.empty())
        {
            forv(i, hand)
            {
                hand[i].c = 0;
            }
        }        
        
        sort(all(hand));

        int id = -1;
        forv(i, hand)
        {
            if (turns == 1 && hand[i].t == 0) continue;

            id = i;
            break;
        }

        if (id == -1)
        {
            forv(i, hand) hand[i].c = 0;
            sort(all(hand));
            id = 0;
        }
        score += hand[id].s;
        turns += hand[id].t;

        if (hand[id].c) 
        {
            hand.pb(deck.front());
            deck.pop();
        }

        hand.erase(hand.begin() + id, hand.begin() + id + 1);
    } 

    cout << ans << endl;
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}