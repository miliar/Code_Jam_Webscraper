#include <iostream>
#include <vector>

struct Combine
{
    char a, b, result;
};

struct Opposed
{
    char a, b;
};

char tryCombine(std::vector<Combine>& rules, char a, char b)
{
    for(int i = 0; i < rules.size(); i++)
    {
        Combine c = rules.at(i);
        if ((c.a == a && c.b == b) || (c.a == b && c.b == a)) { return c.result; }
    }

    return NULL;
}

bool areOpposed(std::vector<Opposed>& rules, char a, char b)
{
    for(int i = 0; i < rules.size(); i++)
    {
        Opposed c = rules.at(i);
        if ((c.a == a && c.b == b) || (c.a == b && c.b == a)) { return true; }
    }

    return false;
}

int main()
{
    int numCases;
    std::cin >> numCases;

    for (int i = 0; i < numCases; i++)
    {
        std::vector<Combine> combine;
        std::vector<Opposed> oppose;

        std::cout << "Case #" << (i+1) << ": ";

        int numCombine, numOppose;
        std::cin >> numCombine;

        for(int n = 0; n < numCombine; n++)
        {
            Combine c;
            std::cin >> c.a; 
            std::cin >> c.b; 
            std::cin >> c.result; 
            combine.push_back(c);
        }

        std::cin >> numOppose;

        for(int n = 0; n < numOppose; n++)
        {
            Opposed o;
            std::cin >> o.a;
            std::cin >> o.b;
            oppose.push_back(o);
        }

        int numElements;
        std::cin >> numElements;

        std::vector<char> elements;

        for(int n = 0; n < numElements; n++)
        {
            char c;
            std::cin >> c;

            char com;
            if (elements.size() > 0 && (com = tryCombine(combine, c, elements.back())))
            {
                elements.pop_back();
                elements.push_back(com);
            } else {
                elements.push_back(c);

                for (int j = 0; j < elements.size(); j++)
                {
                    if(areOpposed(oppose, c, elements.at(j)))
                    {
                        elements.clear();
                        break;
                    }
                }
            }
        }

        std::cout << "[";
        numElements = elements.size();
        for(int n = 0; n < numElements; n++)
        {
            std::cout << elements.at(n);
            if (n != numElements - 1) { std::cout << ", "; }
        }
        std::cout << "]";

        std::cout << std::endl;
    }

}
