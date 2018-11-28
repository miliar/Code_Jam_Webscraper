#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<list>

using namespace std;
struct Card{
    int c,s,t;
};

class Hand{
public:
    Hand(Card** deck, int cardsLeft)
        : m_deck(deck), m_left(cardsLeft)
    {
        S=0;
        T=1;
        solved = false;
    }

    Hand(const Hand& other)
        : m_deck(other.m_deck), m_left(other.m_left), S(other.S), T(other.T)
    {
        cs[0] = other.cs[0];
        cs[1] = other.cs[1];
        cs[2] = other.cs[2];
        ts = other.ts;//Shouldn't do a thing
        solved = false;
    }

    bool draw(){
        if(!m_left)
            return false;
        Card* c = m_deck[0];
        m_deck++;
        m_left--;
        if(c->t > 0){
            ts.insert(ts.begin(), c);
        }else{
            bool placed = false;
            for(list<Card*>::iterator iter=cs[c->c].begin(); iter != cs[c->c].end(); iter++){
                if((*iter)->s <= c->s){
                    cs[c->c].insert(iter,c);
                    placed = true;
                    break;
                }
            }
            if(!placed)
                cs[c->c].insert(cs[c->c].end(), c);
        }
        return true;
    }

    int solve(){
        //Play t>0s
        if(solved || !T)
            return S;
        while(!ts.empty()){
            Card* cur = ts.front();
            ts.pop_front();
            play(cur);
        }
        //Play best of three draw classes
        int best = S;
        if(T){
            for(int i=0; i<3; i++){
                if(!cs[i].empty()){
                    Hand trial(*this);
                    Card* cur = trial.cs[i].front();
                    trial.cs[i].pop_front();
                    trial.play(cur);
                    best = max(best, trial.solve());
                    //fprintf(stdout, "Debug %d %d\n", best, trial.S);
                }
            }
        }
        S = best;
        solved = true;
        return best;
    }

private:
    void play(Card* c){//used inside solve only
        if(!T)
            fprintf(stderr,"Bugger!\n");
        T -= 1;
        S += c->s;
        T += c->t;
        int draws = c->c;
        while(draws--)
            draw();
    }

    Card** m_deck;
    int m_left;
    int S;
    int T;
    list<Card*> cs[3];
    list<Card*> ts;
    bool solved;
};

int solve(Card** cards, int deckStart, int cardCount){
    Hand starter(cards, cardCount);
    for(int i=0; i<deckStart; i++)
        starter.draw();//init
    return starter.solve();//plays t>0s too
}

int main(int argc, char* argv[]){
    if(argc < 3)
        return 1;
    FILE* in = fopen(argv[1], "r");
    FILE* out = fopen(argv[2], "w");
    int T,N,M;
    fscanf(in, "%d", &T);
    Card** cards = (Card**)malloc(80*sizeof(Card*));
    for(int t=1; t<=T; t++){
        int deckStart = 0;
        int cardCount = 0;
        fscanf(in ,"%d", &N);
        for(int i=0; i<N; i++){
            cards[cardCount] = new Card;
            fscanf(in, "%d %d %d", &(cards[cardCount]->c), &(cards[cardCount]->s), &(cards[cardCount]->t));
            cardCount++;
            deckStart++;
        }
        if(deckStart == 0)
            fprintf(stderr, "Bugger\n");
        fscanf(in ,"%d", &M);
        for(int i=0; i<M; i++){
            cards[cardCount] = new Card;
            fscanf(in, "%d %d %d", &(cards[cardCount]->c), &(cards[cardCount]->s), &(cards[cardCount]->t));
            cardCount++;
        }
        fprintf(out, "Case #%d: %d\n", t, solve(cards, deckStart, cardCount));
        for(int i=0; i<cardCount; i++){
            delete cards[i];
        }
    }
    return 0;
}
