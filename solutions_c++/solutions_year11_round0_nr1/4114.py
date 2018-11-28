
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <string>
#include <cassert>
#include <vector>

#include <boost/algorithm/string.hpp>


enum Color
{
    Blue, 
    Orange
};

enum MoveType 
{
    MOVE,
    PRESS,
    PASS
};


class Bot
{
public:

    Bot() : position(1), pendingMove(PASS), next(0)
    {
    }
    
    void move(int turn)
    {
        if ( next == buttonTurnList.size() )
        {
            pendingMove = PASS;
            return;
        }
        int nextPos = buttonTurnList[next].first;
        if ( position != nextPos)
        {
//            std::cerr << "moving from " << position << " to " << nextPos << std::endl;
            if ( position < nextPos)
                ++position;
            else
                --position;
            pendingMove = MOVE;
            return;
        }
        else 
        {
            //          std::cerr << "at position on turn " << turn << " waiting for " << buttonTurnList[next].second << std::endl;
            if ( buttonTurnList[next].second == turn)
            {
                pendingMove = PRESS;
                ++next;
            }
            else 
                pendingMove = PASS;
            return;
        }
    }
    std::vector<std::pair<int, int> > buttonTurnList;
    int position;
    MoveType pendingMove;
    int next;
    
};

typedef std::vector<std::pair<Color, int> > InputVec;

class Sim
{
public:

    Sim(const InputVec& sequence)
        : m_sequence (sequence)
    {
    }

    int solve()
    {
        Bot bBot;
        Bot oBot;
        int order = 0;
        for ( InputVec::const_iterator i = m_sequence.begin(); i != m_sequence.end();
              ++i, ++order)
        {
            if (i->first == Blue)
            {
//                              std::cerr << " telling blue to push " << i->second << " on turn " << order << std::endl;
                bBot.buttonTurnList.push_back(std::pair<int, int> (i->second, order));
            }
            else 
            {
                //                            std::cerr << "  telling orange to push " << i->second << " on tur " << order << std::endl;
                oBot.buttonTurnList.push_back(std::pair<int, int> ( i->second, order));
            }
        }

        int turn = 0;
        int moves = 0;

        while (true)
        {
            ++moves;
//            std::cerr << "blue move " << std::endl;
            bBot.move(turn);
//            std::cerr << " orange move " << std::endl;
            oBot.move(turn);
            if (bBot.pendingMove == PRESS)
            {
//                std::cerr << "blue pushed increasing turn " << std::endl;
                ++turn;
            }
            else if (oBot.pendingMove == PRESS)
            {
//                std::cerr << "blue pushed increasing turn " << std::endl;
                ++turn;
            }
            if (turn == m_sequence.size())
                return moves; 
        }
        

        return 0;
    }

private:
    const InputVec& m_sequence;

};

int main()
{
    std::ifstream file("A-large.in");
    char buf[512];
    file.getline(buf, 512);
    int cases = std::atoi(buf);
//    std::cerr << "handling " << cases << " cases " << std::endl;
    
    for ( int i = 0; i < cases; ++i)
    {
//        std::cerr << "starting case 1 " << std::endl;
        file.getline(buf, 512);
        std::vector<std::string> tokens;
        boost::split(tokens, buf, boost::is_any_of(" "));
        assert(tokens.size() != 0);
       
        assert( ( tokens.size() % 2) == 1);
            
        bool num = false;
        int button;
        Color color;
        std::vector < std::pair<Color, int> > sequence;
        for ( std::vector<std::string>::iterator t = tokens.begin() + 1;
              t != tokens.end();
              ++t)
        {
            if (num)
            {
                button = std::atoi(t->c_str());
                assert(button <= 100);
                sequence.push_back(std::pair<Color, int>(color, button));
            }
            else
            {
                if (*t == "B")
                    color = Blue;
                else if ( *t == "O")
                    color = Orange;
                else
                    assert(false);
            }
            num = !num;
        }
        Sim sim(sequence);
        int value = sim.solve();
        std::cout << "Case #" << (i+1)<< ": " << value << std::endl;
    }
    

}
