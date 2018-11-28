#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

class Move {
public:
    Move(int pos, int num) 
    {
        position = pos;
        moveNum = num;
    }

    int getPosition() { return position; }
    int getMoveNum() { return moveNum; }

private:
    int position;
    int moveNum;
};

class Robot {
public:
    enum Color { ORANGE, BLUE};
    Robot(Color c)
    {
        color = c;
        position = 0;
    }

    int getPosition() 
    {
        return position;
    }

    void moveForward() 
    {
        position++;
    }

    void moveBack() 
    {
        position--;
    }

private:
    int position;
    Color color;
};

int findNumMoves(queue<Move> orange, queue<Move> blue, int numMoves);

int main() 
{
    int numLines = 0;
    ifstream data;
    data.open("data");
    data >> numLines;

    for (int i = 0; i < numLines; i++) 
    {
        queue<Move> orange, blue;
        cout << "Case #" << i + 1 << ": ";
        int numMoves = 0;
        data >> numMoves;
	    int curMove = 0;

        for (int j = 0; j < numMoves; j++)
        {
            int position;
            char robot;
            data >> robot >> position;
            Move move(position, j);

            if (robot == 'O') orange.push(move);
            else blue.push(move);
        }

        cout << findNumMoves(orange, blue, numMoves);
        cout << '\n';
    }

    data.close();
    return 0;
}


int findNumMoves(queue<Move> orangeMoves, queue<Move> blueMoves, int totalMoves)
{
    int total = 0;
    Robot orange(Robot::ORANGE), blue(Robot::BLUE);
    int currentMove = 0;
    bool keepGoing = true;    
    bool pushedOrange = false;
    while (currentMove < totalMoves)    
    {
        total++;
        pushedOrange = false;
        if (!orangeMoves.empty()) 
        {
            Move o = orangeMoves.front();
            if (o.getPosition() == orange.getPosition() && o.getMoveNum() == currentMove)
            {
                currentMove++;
                orangeMoves.pop();
                pushedOrange = true;
            }
            else if ( o.getPosition() > orange.getPosition())
            {
                orange.moveForward();
            }
            else if (o.getPosition() < orange.getPosition())
            {
                orange.moveBack();
            }
        }
        
        if (!blueMoves.empty()) 
        {
            Move b = blueMoves.front();
            if (!pushedOrange && 
                b.getPosition() == blue.getPosition() && 
                b.getMoveNum() == currentMove)
            {
                currentMove++;
                blueMoves.pop();
            }
            else if ( b.getPosition() > blue.getPosition())
            {
                blue.moveForward();
            }
            else if (b.getPosition() < blue.getPosition())
            {
                blue.moveBack();
            }
        }
    }
    return total - 1 ;
}

