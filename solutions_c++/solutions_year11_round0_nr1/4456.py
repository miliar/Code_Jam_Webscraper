#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

//#define DEBUG
//#define UNIT_TEST

// Algorithm:
// Need a data structure that holds the list of things to do and 
// returns the next thing to do for each robot.

class ButtonList
{
public:
    ButtonList(int size)
    {
        mList.reserve(size);
    }

    void addButton(bool orange, int pos)
    {
        mList.push_back(but_pos_t(orange, pos));
        if (orange)
            mOrangeList.push_back(pos);
        else
            mBlueList.push_back(pos);
    }

    int simulate()
    {
        int result = 0;

        bniter_t bni = mList.begin();
        iiter_t bluei = mBlueList.begin();
        iiter_t blueend = mBlueList.end();
        iiter_t orangei = mOrangeList.begin();
        iiter_t orangeend = mOrangeList.end();

        int blue_pos = 1;
        int orange_pos = 1;

        for (bniter_t bni = mList.begin(); bni != mList.end(); ++bni)
        {
            // Lots of redundancy here...to fix
#ifdef DEBUG
            std::cout << ((bni->orange) ? "O" : "B") << " " << bni->pos << " : nextO: " << ((orangei != orangeend) ? *orangei : -1) << " nextB: " << ((bluei != blueend) ? *bluei : -1) << std::endl; 
            
#endif
            if (bni->orange && bni->pos == orange_pos)
            {
                // orange presses button
                assert(*orangei == orange_pos);
                orangei++;
                result++; // takes 1 step

                if (bluei == blueend)
                    continue;

                if (*bluei > blue_pos)
                {
                    // blue can take 1 step
                    blue_pos++;
                }
                else if (*bluei < blue_pos)
                {
                    blue_pos--;
                }
            }
            else if (!bni->orange && bni->pos == blue_pos)
            {
                // blue presses button
                assert(*bluei == blue_pos);
                bluei++;
                result++; // takes 1 step

                if (orangei == orangeend)
                    continue;

                if (*orangei > orange_pos)
                {
                    orange_pos++;
                }
                else if (*orangei < orange_pos)
                {
                    orange_pos--;
                }
            }
            else if (bni->orange)
            {
                int steps = (bni->pos - orange_pos);
                if (steps < 0) steps = -steps;
                steps++; // don't forget the pushing step
                orange_pos = bni->pos;
                assert(*orangei == orange_pos); 
                orangei++;
                result += steps;

                if (bluei == blueend)
                    continue;

                if (*bluei > blue_pos)
                {
                    blue_pos += std::min(steps, *bluei - blue_pos); 
                }
                else if (*bluei < blue_pos)
                {
                    blue_pos -= std::min(steps, blue_pos - *bluei); 
                }
            }
            else if (!bni->orange)
            {
                int steps = (bni->pos - blue_pos);
                if (steps < 0) steps = -steps;
                steps++; // don't forget the pushing step
                blue_pos = bni->pos;
                assert(*bluei == blue_pos); 
                bluei++;
                result += steps;

                if (orangei == orangeend)
                    continue;

                if (*orangei > orange_pos)
                {
                    orange_pos += std::min(steps, *orangei - orange_pos); 
                }
                else if (*orangei < orange_pos)
                {
                    orange_pos -= std::min(steps, orange_pos - *orangei); 
                }
            }
            else
            {
                assert(0 && "can't get here");
            }
        }
        return result;
    }

private:
    struct but_pos_t
    {
        but_pos_t(bool o, int n) : orange(o), pos(n) {}
        bool orange;
        int pos;
    };

    typedef std::vector<but_pos_t>::iterator bniter_t;
    typedef std::vector<int>::iterator iiter_t;
    std::vector<but_pos_t> mList;
    std::vector<int> mBlueList;
    std::vector<int> mOrangeList;

};


void output(ButtonList& result, size_t line)
{
    std::cout << "Case #" << line + 1 << ": " << result.simulate() << std::endl;
}

int main()
{
#ifdef UNIT_TEST
#endif

    size_t numcases;
    std::cin >> numcases;
#ifdef DEBUG
    std::cout << numcases << " cases" << std::endl;
#endif
    for (size_t casex = 0; casex < numcases; ++casex)
    {
        size_t numsteps;
        
        std::cin >> numsteps;
#ifdef DEBUG
        std::cout << "numsteps: " << numsteps << std::endl;
#endif
        ButtonList buttonList(numsteps);

        while (numsteps--)
        {
            char bot;
            int button;
            std::cin >> bot >> button;
            buttonList.addButton(bot == 'O', button);
        }

        output(buttonList, casex);
    }

    return 0;
}
