#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
const char outfile[] = "Magicka.out";

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

class Combinator
{
public:
    Combinator(char c1, char c2, char r) : C1(c1), C2(c2), R(r) {}
    friend bool operator== (const Combinator&, std::pair<char,char>);
    char C1, C2, R;
};

bool operator ==(const Combinator& c, std::pair<char,char> chars)
{
    return ((chars.first == c.C1 && chars.second == c.C2) || (chars.first == c.C2 && chars.second == c.C1));
}

class Destroyer
{
public:
    Destroyer(char c1, char c2) : C1(c1), C2(c2) {}
    char GetPair(char ch) const;
    char C1, C2;
};

char Destroyer::GetPair(char ch) const
{
    if (ch == C1)
        return C2;
    if (ch == C2)
        return C1;
    return 0;
}

bool isCombining(const std::vector<Combinator>& combinators, std::vector<char>& elementString)
{
    if (elementString.size() < 2)
        return false;
    std::pair<char,char> tops(elementString.back(), elementString.at(elementString.size() - 2));
    for (std::vector<Combinator>::const_iterator it = combinators.begin();
            it != combinators.end(); ++it)
    {
        if ((*it) == tops)
        {
            elementString.erase(elementString.begin() + (elementString.size() - 2), elementString.end());
            elementString.push_back(it->R);
            return true;
        }
    }
    return false;
}

std::vector<char>::iterator Rfind(std::vector<char>::iterator it, std::vector<char>::iterator itr, char ch)
{
    std::vector<char>::iterator result = std::find(it, itr, ch);
    if (result != itr)
    {
        std::vector<char>::iterator next = std::find(result + 1, itr, ch);
        while(next != itr)
        {
            result = next;
            next = std::find(result + 1, itr, ch);
        }
    }
    return result;
}

bool tryDestroy(const std::vector<Destroyer>& destroyers, std::vector<char>& elementString)
{
    if (elementString.size() < 2)
        return false;
    char ch;
    for (std::vector<char>::iterator it = elementString.begin();
            it != elementString.end(); ++it)
    {
        ch = 0;
        int destroyerSize = destroyers.size();
        for (std::vector<Destroyer>::const_iterator dit = destroyers.begin();
                dit != destroyers.end(); ++dit)
        {
                ch = dit->GetPair(*it);
                if ( ch != 0)
                break;
        }
        if (ch != 0)
        {
            std::vector<char>::iterator found = std::find(it, elementString.end(), ch);
            /*std::vector<char>::iterator found = Rfind(it, elementString.end(), ch);
            std::vector<char>::iterator itd = Rfind(it, found, *it);*/
            if (found != elementString.end())
            {
                elementString.clear();
                break;
                /*if (itd == found)
                    elementString.erase(it, (found + 1));
                else
                    elementString.erase(itd, found + 1);
                it = elementString.begin();
                int sizeOfele = elementString.size();
                if ( it == elementString.end())
                    break;
                 */
            }
        }
    }
}

int main(int argc, char* argv[])
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
    int nCases;
    {
        std::stringstream inStr(lines[0]);
        inStr >> nCases;
    }

    std::ofstream res(outfile);
    for (int index = 1; index <= nCases; ++index)
    {
        if (index == 23)
            std::cout << "begin";
        std::vector<Combinator> combinator;
        std::vector<Destroyer> destroyer;
        std::stringstream inStr(lines[index]);
        int nCombs;
        inStr >> nCombs;
        for (int i = 1; i <= nCombs; ++i)
        {
            std::string combStr;
            inStr >> combStr;
            char c1 = combStr.at(0), c2 = combStr.at(1), r = combStr.at(2);
            combinator.push_back(Combinator(c1, c2, r));
        }

        int nDes;
        inStr >> nDes;
        for (int i = 1; i <= nDes; ++i)
        {
            std::string desStr;
            inStr >> desStr;
            char c1 = desStr.at(0), c2 = desStr.at(1);
            destroyer.push_back(Destroyer(c1, c2));
        }

        std::vector<char> elementString;
        int inLen;
        inStr >> inLen;
        std::string eleStr;
        inStr >> eleStr;
        for (int i = 0; i < inLen; ++i)
        {
            char ch = eleStr.at(i);
            elementString.push_back(ch);
            isCombining(combinator, elementString);
            tryDestroy(destroyer, elementString);
        }

        res << "Case #" << index << ": [";
        if (!elementString.empty())
        {
            for (int i = 0; i < elementString.size() -1; ++i)
                res << elementString[i] <<", ";
            res << elementString.back() << "]" << std::endl;
        }
        else
        {
            res << "]" << std::endl;
        }
        combinator.erase(combinator.begin());
        destroyer.erase(destroyer.begin());
    }
    return 0;
}

