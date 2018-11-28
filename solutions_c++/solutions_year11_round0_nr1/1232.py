#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <sstream>
#include <string>

const char outfile[] = "BotTrust.out";

std::vector<std::string> Split(const std::string& input, char splitter)
{
    size_t curr = 0;
    std::vector<std::string> result;
    while (true)
    {
        size_t next = input.find(splitter, curr);
        if (next == std::string::npos)
        {
            result.push_back(input.substr(curr));
            break;
        }
        result.push_back(input.substr(curr,next-curr));
        curr = next + 1;
    }
    return result;
}

class Robot
{
public:
    Robot(unsigned int& dM) : doneMoves(dM), curr(1) {}
    void pushMove(unsigned int m, unsigned int n);
    unsigned int Next();
private:
    std::queue<int> nextMove;
    std::queue<int> nextMoveNo;
    unsigned int& doneMoves;
    unsigned int curr;
};

void Robot::pushMove(unsigned int m, unsigned int n)
{
    nextMove.push(m);
    nextMoveNo.push(n);
}

unsigned int Robot::Next()
{
    if (nextMove.empty())
        return 0;
    else if (curr == nextMove.front())
    {
        if (doneMoves == nextMoveNo.front())
        {
            nextMove.pop();
            nextMoveNo.pop();
            return 1;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        int next = nextMove.front();
        int seq = nextMoveNo.front();
        if (next > curr)
            curr += 1;
        else
            curr -= 1;
        return 0;
    }
    return 0;
}

class RobotSystem
{
public:
    RobotSystem() : doneMoves(1), robot(2, Robot(doneMoves)) {}
    void SetSequence(const std::string& moves);
    unsigned int ExecuteSequence();

private:
    void SetTarget(unsigned int t) {target = t;}

    std::vector<Robot> robot;
    unsigned int doneMoves;
    unsigned int target;
};

void RobotSystem::SetSequence(const std::string& moves)
{
    std::stringstream seq(moves);
    int target;
    seq >> target;
    SetTarget(target);
    for (int i = 0; i < target; i++)
    {
        char r;
        int move;
        seq >> r >> move;
        unsigned int robotNo = (r == 'O') ? 0 : 1;
        robot[robotNo].pushMove(move, i + 1);
    }
}

unsigned int RobotSystem::ExecuteSequence()
{
    unsigned int result = 0;
    while (doneMoves <= target)
    {
        int i = robot[0].Next();
        int j = robot[1].Next();
        if (i | j)
            doneMoves++;
        result++;
    }
    return result;
}

int main(int argc, char** argv)
{
    if (argc != 2)
    {
        return 1;
    }
    std::string text = "";
    std::ifstream file(argv[1]);
    while (file.good())
    {
        char ch = static_cast<char>(file.get());
        if ( ch != EOF)
        text += ch;
    }
    std::vector<std::string> lines = Split(text, '\n');
    std::stringstream inStr(lines[0]);
    int nCases;
    inStr >> nCases;
    std::ofstream res(outfile);
    for (int i = 1; i <= nCases; ++i)
    {
        RobotSystem rs;
        std::string nextCase = lines[i];
        rs.SetSequence(nextCase);
        unsigned int reqrdMoves = rs.ExecuteSequence();
        res << "Case #" << i << ": " << reqrdMoves << std::endl;
    }
    return 0;
}

