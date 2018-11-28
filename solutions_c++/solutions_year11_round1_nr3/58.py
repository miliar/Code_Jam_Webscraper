#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

int T, N, M;
int c[80];
int s[80];
int t[80];

struct State
{
    int turns;
    int score;
    int position;
    int value;
    vector<int> tCards;
    vector<int> draw2;
    vector<int> draw1;
    vector<int> sCards;
};
State dp[81][81];
bool possible[81][81];

void removeCard(vector<int>& vec, int id)
{
    for (int i = 0; i < vec.size(); ++i)
        if (vec[i] == id)
        {
            swap(vec[i], vec[vec.size()-1]);
            vec.pop_back();
            return;
        }
}

void deleteCard(State& state, int id)
{
    if (t[id] > 0)
        removeCard(state.tCards, id);
    else if (c[id] == 2)
        removeCard(state.draw2, id);
    else if (c[id] == 1)
        removeCard(state.draw1, id);
    else
        removeCard(state.sCards, id);
}

void insertCard(State& state, int id)
{
    if (id >= M+N)
        return;
    if (t[id] > 0)
        state.tCards.push_back(id);
    else if (c[id] == 2)
        state.draw2.push_back(id);
    else if (c[id] == 1)
        state.draw1.push_back(id);
    else
        state.sCards.push_back(id);
}

void playCard(State& state, int id)
{
    state.score += s[id];
    state.turns += t[id] - 1;
    deleteCard(state, id);
    for (int i = 0; i < c[id]; i++, state.position++)
        insertCard(state, state.position);
}

void playAllT(State& state)
{
    while (!state.tCards.empty())
        playCard(state, state.tCards[0]);
}

void calcValue(State& state)
{
    vector<int> cardsToPlay;
    for (int i = 0; i < state.sCards.size(); ++i)
        cardsToPlay.push_back(s[state.sCards[i]]);
    sort(cardsToPlay.begin(), cardsToPlay.end());
    reverse(cardsToPlay.begin(), cardsToPlay.end());
    
    int turnsToPlay = min(state.turns, int(state.sCards.size()));
    state.value = state.score;
    for (int i = 0; i < turnsToPlay; ++i)
        state.value += cardsToPlay[i];
}

void playBest2(State& state)
{
    int bestID = state.draw2[0];
    for (int i = 1; i < state.draw2.size(); ++i)
        if (s[bestID] < s[state.draw2[i]])
            bestID = state.draw2[i];
    playCard(state, bestID);
}

void playBest1(State& state)
{
    int bestID = state.draw1[0];
    for (int i = 1; i < state.draw1.size(); ++i)
        if (s[bestID] < s[state.draw1[i]])
            bestID = state.draw1[i];
    playCard(state, bestID);
}

int main()
{
    ifstream in("C.in");
    ofstream out("C.out");
    
    in >> T;
    for (int tc = 1; tc <= T; ++tc)
    {
        memset(possible, false, sizeof possible);
        in >> N;
        for (int i = 0; i < N; ++i)
            in >> c[i] >> s[i] >> t[i];
        in >> M;
        for (int i = 0; i < M; ++i)
            in >> c[N+i] >> s[N+i] >> t[N+i];
        
        dp[0][0] = State();
        dp[0][0].turns = 1;
        dp[0][0].score = 0;
        dp[0][0].position = N;
        for (int i = 0; i < N; ++i)
            insertCard(dp[0][0], i);
        playAllT(dp[0][0]);
        calcValue(dp[0][0]);
        possible[0][0] = true;
        int bestVal = dp[0][0].value;
        
        for (int i = 0; i < 81; ++i)
            for (int j = 0; j < 81; ++j)
            {
                if (i == 0 && j == 0)
                    continue;
                if (i > 0 && possible[i-1][j] && !dp[i-1][j].draw1.empty() && dp[i-1][j].turns > 0)
                {
                    dp[i][j] = dp[i-1][j];
                    playBest1(dp[i][j]);
                    if (dp[i][j].turns > 0)
                        playAllT(dp[i][j]);
                    calcValue(dp[i][j]);
                    possible[i][j] = true;
                }
                if (j > 0 && possible[i][j-1] && !dp[i][j-1].draw2.empty() && dp[i][j-1].turns > 0)
                {
                    State curState = dp[i][j-1];
                    playBest2(curState);
                    if (curState.turns > 0)
                        playAllT(curState);
                    calcValue(curState);
                    
                    if (possible[i][j] && dp[i][j].value < curState.value)
                        dp[i][j] = curState;
                    possible[i][j] = true;
                }
                if (possible[i][j])
                    bestVal = max(bestVal, dp[i][j].value);
            }
        
        out << "Case #" << tc << ": " << bestVal << endl;
    }
}
