//--------------------------------------------------------------------------------------------------
// Includes
//--------------------------------------------------------------------------------------------------
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <cassert>
#include <set>
#include <boost/foreach.hpp> //WWW.BOOST.ORG LIBRARY USED
//--------------------------------------------------------------------------------------------------


::std::ifstream inputFileStream("input.txt");
::std::ofstream outputFileStream("output.txt");

typedef int Number;
bool desiredValue;
unsigned int nodesCount;
unsigned int logicalNodesCount;
unsigned int valuesNodesCount;
struct Tree
{
    ::std::vector<bool> isChangeable;
    ::std::vector<bool> values;
};
Tree tree;

::std::vector<int> beSetToTrue;
::std::vector<int> beSetToFalse;

void setBestValue(int& current, int newValue)
{
    if (current == -1)
    {
        current = newValue;
    }
    else
    {
        if (newValue < current)
        {
            current = newValue;
        }
    }
}

int leftChild(int anIndex)
{
    return 2 * anIndex + 1;
}
int rightChild(int anIndex)
{
    return leftChild(anIndex) + 1;
}
void solveAll(void)
{
    beSetToTrue.clear();
    beSetToFalse.clear();
    beSetToTrue.resize(nodesCount, -1);
    beSetToFalse.resize(nodesCount, -1);
    for (unsigned int index = logicalNodesCount; index < nodesCount; ++index)
    {
        if (tree.values[index])
        {
            beSetToTrue[index] = 0;
            beSetToFalse[index] = -1;
        }
        else
        {
            beSetToTrue[index] = -1;
            beSetToFalse[index] = 0;
        }
    }
    for (int index = logicalNodesCount -  1; index >= 0; --index)
    {
            int leftToTrue = beSetToTrue[leftChild(index)];
            int rightToTrue = beSetToTrue[rightChild(index)];
            int leftToFalse = beSetToFalse[leftChild(index)];
            int rightToFalse = beSetToFalse[rightChild(index)];
            int myValueToTrue = -1;
            int myValueToFalse = -1;
            bool imChangable = tree.isChangeable[index];
        if (tree.values[index]) //AND
        {
            if ((leftToTrue != -1) && (rightToTrue != -1))
            {
                setBestValue(myValueToTrue, leftToTrue + rightToTrue);
            }
            if (imChangable && leftToTrue != -1)
            {
                setBestValue(myValueToTrue, leftToTrue + 1);
            }
            if (imChangable && rightToTrue != -1)
            {
                setBestValue(myValueToTrue, rightToTrue + 1);
            }

            if (leftToFalse != -1)
            {
                setBestValue(myValueToFalse, leftToFalse);
            }
            if (rightToFalse != -1)
            {
                setBestValue(myValueToFalse, rightToFalse);
            }
        }
        else //OR
        {
            if (leftToTrue != -1)
            {
                setBestValue(myValueToTrue, leftToTrue);
            }
            if (rightToTrue != -1)
            {
                setBestValue(myValueToTrue, rightToTrue);
            }

            if (imChangable && leftToFalse != -1)
            {
                setBestValue(myValueToFalse, leftToFalse + 1);
            }
            if (imChangable && rightToFalse != -1)
            {
                setBestValue(myValueToFalse, rightToFalse + 1);
            }
            if ((leftToFalse != -1) && (rightToFalse != -1))
            {
                setBestValue(myValueToFalse, leftToFalse + rightToFalse);
            }
        }
        beSetToTrue[index] = myValueToTrue;
        beSetToFalse[index] = myValueToFalse;
    }
}


Number solve()
{
    solveAll();
    if (desiredValue)
    {
        return beSetToTrue[0];
    }
    else
    {
        return beSetToFalse[0];
    }
}

int main(int /*argc*/, char* /*argv*/[])
{
    unsigned int numberOfCases;
    inputFileStream >> numberOfCases;
    for (unsigned int caseIndex = 1; caseIndex <= numberOfCases; ++caseIndex)
    {
        unsigned int integerDesiredValue;
        inputFileStream >> nodesCount >> integerDesiredValue;
        desiredValue = integerDesiredValue == 1;
        logicalNodesCount = (nodesCount - 1) / 2;
        valuesNodesCount = (nodesCount + 1) / 2;
        tree.isChangeable.clear();
        tree.values.clear();
        for (unsigned int nodeIndex = 0; nodeIndex < logicalNodesCount; ++nodeIndex)
        {
            unsigned int isAnd, isChangable;
            inputFileStream >> isAnd >> isChangable;
            tree.values.push_back(isAnd == 1 ? true : false);
            tree.isChangeable.push_back(isChangable ? true : false);
        }
        for (unsigned int nodeIndex = 0; nodeIndex < valuesNodesCount; ++nodeIndex)
        {
            unsigned int nodeValue;
            inputFileStream >> nodeValue;
            tree.values.push_back(nodeValue == 1 ? true : false);
        }
        Number solution = solve();
        if (solution == -1)
        {
            outputFileStream << "Case #" << caseIndex << ": " << "IMPOSSIBLE" << ::std::endl;
        }
        else
        {
            outputFileStream << "Case #" << caseIndex << ": " << solution << ::std::endl;
        }
    }
    return 0;
}
