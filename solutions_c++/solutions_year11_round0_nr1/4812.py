#include <string>
#include <vector>
#include <iostream>

using namespace std;

typedef struct move
{
    int origSeqIndx;
    int tempIndx;
    char robot; //'O'-orange & 'B'-blue
    int button;
    bool buttonPushed;
}Move;

typedef struct Moves
{
    vector<Move> moves;
    int sequenceSize;
}Sequence;


int curPosO = 1;
int curPosB = 1;

int nxtOMove = 0;
int nxtBMove = 0;

int seconds = 0;

Sequence readTestCase()
{
    Sequence sequence;
    cin >> sequence.sequenceSize;
    for(int i = 0; i < sequence.sequenceSize; i++)
    {
        Move mov;
        mov.origSeqIndx = i;
        mov.buttonPushed = false;
        cin >> mov.robot >> mov.button;
        sequence.moves.push_back(mov);
    }
    return sequence;
}

void processSeqB(Sequence& seqB)
{
    if(seqB.sequenceSize > 0)
    {
        if(curPosB > seqB.moves[nxtBMove].button)
            curPosB--;
        else if(curPosB < seqB.moves[nxtBMove].button)
            curPosB++;
    }
}
void processSeqO(Sequence& seqO)
{
    if(seqO.sequenceSize > 0)
    {
        if(curPosO > seqO.moves[nxtOMove].button)
            curPosO--;
        else if(curPosO < seqO.moves[nxtOMove].button)
            curPosO++;
    }
}


void processMove(Move move, Sequence& seqO, Sequence& seqB)
{
    bool moveDone = false;
    while(!moveDone)
    {
        if(move.robot == 'O')
        {
            if(move.button == curPosO)
            {
                move.buttonPushed = true;
                nxtOMove++;
                moveDone = true;
            }
            else if(move.button > curPosO)
            {
                curPosO++;
            }
            else
            {
                curPosO--;
            }
            //std::cout << "O Pos: " << curPosO << endl;
            processSeqB(seqB);
        }
        else
        {
            if(move.button == curPosB)
            {
                move.buttonPushed = true;
                nxtBMove++;
                moveDone = true;
            }
            else if(move.button > curPosB)
            {
                curPosB++;
            }
            else
            {
                curPosB--;
            }
            //std::cout << "B Pos : " <<curPosB << endl;
            processSeqO(seqO);
        }
        seconds++;
    }
}

void partitionSequence(Sequence origSeq, Sequence& seqO, Sequence& seqB)
{
    int seqOSize = 0;
    int seqBSize = 0;
    //std::cout << "Orig seq : " << origSeq.sequenceSize << endl;
    //std::cout << origSeq.moves[0].robot << " - " << origSeq.moves[0].button << std::endl;
    for(int i = 0; i < origSeq.sequenceSize; i++)
    {
        if(origSeq.moves[i].robot == 'O')
        {
            seqO.moves.push_back(origSeq.moves[i]);
            seqOSize++;
        }
        else
        {
            seqB.moves.push_back(origSeq.moves[i]);
            seqBSize++;
        }
    }
    seqO.sequenceSize = seqOSize;
    seqB.sequenceSize = seqBSize;
}

void resetState()
{
    seconds = 0;
    curPosO = 1;
    curPosB = 1;

    nxtOMove = 0;
    nxtBMove = 0;
}

void processTestCase(Sequence sequence, int caseNum)
{
    Sequence sequenceO;
    Sequence sequenceB;

    partitionSequence(sequence, sequenceO, sequenceB);
    for(int i = 0; i < sequence.sequenceSize; i++)
    {
        //std::cout << "Processing move : " << i << endl;
        processMove(sequence.moves[i], sequenceO, sequenceB);
    }
    std::cout << "Case #" << caseNum << ": " << seconds << endl;
    
    resetState();
}

int main()
{
    int numCases;
    vector<Sequence> testCases;

    cin >> numCases;
    for(int i = 0; i < numCases; i++)
    {
        testCases.push_back(readTestCase());
    }
    for(int i = 0; i < numCases; i++)
    {
        processTestCase(testCases[i], i+1);
    }
    return 0;
}
