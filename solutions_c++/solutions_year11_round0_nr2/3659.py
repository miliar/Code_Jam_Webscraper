#include <iostream>
#include <fstream>
#include <cstdlib>

#include <vector>
#include <string>

#include <map>
#include <list>

#include <boost/algorithm/string.hpp>

#define BUF_MAX 4096



struct Combo
{
    Combo(std::string _combo)
    {
        i1 = _combo[0];
        i2 = _combo[1];
        o = _combo[2];
    }

    bool contains(char i, char j) const
    {
        return (i1 == i && i2 == j) || (i1 == j && i2 == i);
    }
        
    char i1;
    char i2;
    char o;
};

struct Destro
{
    Destro(std::string _destro)
    {
        i1 = _destro[0];
        i2 = _destro[1];
    }


    
    char i1;
    char i2;
};

class Wizard
{
public:
    Wizard(const std::vector<Combo>& _combos, std::vector<Destro>& _destros): combos(_combos), destros(_destros) {}

    void invoke(char e)
    {
//        std::cerr << "invoking " << e << std::endl;
        elemList.push_back(e);
        occur[e]++;
        
        while (combo());
        
        char& c = elemList.back();
        int& o = occur[c];
        if ( o == 1 )
        {
            for ( std::vector<Destro>::iterator i = destros.begin();
                  i != destros.end();
                  ++i)
            {
                if (i->i1 == c)
                {

                    if (occur[i->i2] > 0)
                    {
                          clear();
                    }
                 }
                else if (i->i2 == c)
                {
                    if (occur[i->i1] > 0)
                    {

                          clear();
                    }
                 }
            }
        }
        
    }
    
    void clear()
    {
        elemList.clear();
        occur.clear();
    }

    void print()
    {
        std::cout << "[";
        for(int i = 0; i < elemList.size(); ++i)
        {
            std::cout << elemList[i];
            if (i != elemList.size() -1)
                std::cout << ", ";
        }
        std::cout << "]";
    }

    bool combo()
    {
        int size = elemList.size();
        if (size < 2)
            return false;
        char i1 = elemList[size-1];
        char i2 = elemList[size-2];
        for ( std::vector<Combo>::const_iterator i = combos.begin();
              i != combos.end();
              ++i)
        {
            if (i->contains(i1, i2))
            {
//                std::cerr << "comboing " << i1 << " " << i2 << " into " << i->o << std::endl;
                occur[elemList.back()]--;
                elemList.pop_back();
                occur[elemList.back()]--;
                elemList.pop_back();
                elemList.push_back(i->o);
                occur[elemList.back()]++;
                return true;
            }
        }
        return false;
    }

    private:
    const std::vector<Combo>& combos;
    std::vector<Destro>& destros;

    std::vector<char> elemList;

    std::map<char, int> occur;
    
};

int main()
{

    std::ifstream file("B-large.in");
    char buf[BUF_MAX];
    file.getline(buf, BUF_MAX);
    int cases = std::atoi(buf);
    
    for (int i = 0; i < cases; ++i)
    {
        file.getline(buf, BUF_MAX);
        std::vector<std::string> tokens;
        boost::split(tokens, buf, boost::is_any_of(" " ));
        assert(tokens.size() != 0);
        
        int tokNum = 0;
        int combineNum = std::atoi(tokens[tokNum++].c_str());
        std::vector<Combo> combos;
        for (int j = 0; j < combineNum; ++j)
        {
            combos.push_back(Combo(tokens[tokNum++]));
        }
        
        std::vector<Destro> destros;
        int destructNum = std::atoi(tokens[tokNum++].c_str());;
        for (int j = 0; j < destructNum; ++j)
        {
            destros.push_back(Destro(tokens[tokNum++]));
        }
        
        int elmNum = std::atoi(tokens[tokNum++].c_str());
        std::string& elements = tokens[tokNum++];
        assert(elmNum = elements.length());
        
        Wizard wizard(combos, destros);

        for (int c = 0; c < elements.length(); ++c)
        {
            wizard.invoke(elements[c]);
//            wizard.print();
            //          std::cout << std::endl;
        }

        std::cout << "Case #" << (i+1) << ": ";
        wizard.print();
        std::cout << std::endl;
        
    }
    
}
