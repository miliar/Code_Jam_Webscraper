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
#include <boost/lexical_cast.hpp> //WWW.BOOST.ORG LIBRARY USED
//--------------------------------------------------------------------------------------------------

::std::ifstream inputFileStream("input.in");
::std::ofstream outputFileStream("output.txt");

struct Node
{
    double weight;
    ::std::string feature;    
    Node* trueNode;
    Node* falseNode;
};

void ignoreWhite()
{
    while (::isspace(inputFileStream.peek())) inputFileStream.ignore(1);
}
Node* parseTree()
{
    Node* root = new Node;
    root->falseNode = NULL;
    root->trueNode = NULL;
    ignoreWhite();
    char lala = inputFileStream.get();
    assert(lala == '(');
    ignoreWhite();
    inputFileStream >> root->weight;
    ignoreWhite();
    if (inputFileStream.peek() != ')')
    {
        ignoreWhite();
        inputFileStream >> root->feature;
        root->trueNode = parseTree();
        root->falseNode = parseTree();
    }
    ignoreWhite();
    char aefwa = inputFileStream.get();
    assert(aefwa == ')');
    return root;
}

int main(int /*argc*/, char* /*argv*/[])
{
    unsigned int totalCasesCount;
    inputFileStream >> totalCasesCount;
    for (unsigned int caseIndex = 1; caseIndex <= totalCasesCount; ++caseIndex)
    {
        outputFileStream << "Case #" << caseIndex << ": " << ::std::endl;
        int treeLines;
        inputFileStream >> treeLines;
        Node* tree = parseTree();
        int animalCount;
        inputFileStream >> animalCount;
        for (int i = 0; i < animalCount; ++i)
        {
            int attributesCount;
            ::std::string animalName;
            inputFileStream >> animalName;
            inputFileStream >> attributesCount;
            ::std::set< ::std::string > attributes;
            for (int j = 0; j < attributesCount; ++j)
            {
                ::std::string feature;
                inputFileStream >> feature;
                attributes.insert(feature);
            }
            Node* current = tree;
            double probability = 1;
            while (current != NULL)
            {
                probability *= current->weight;
                if (attributes.count(current->feature) != 0)
                {
                    current = current->trueNode;
                }
                else
                {
                    current = current->falseNode;
                }
            }
            
            char buffer[10000];
            sprintf(buffer, "%.10f",probability);
            outputFileStream << buffer  << ::std::endl;
            //::boost::lexical_cast< ::std:: string > (probability) << ::std::endl;
        }
    }
    return 0;
}
