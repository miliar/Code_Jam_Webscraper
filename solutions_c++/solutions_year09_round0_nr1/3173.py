#include <map>
#include <vector>
#include <string>
#include <iostream>

#if 0
#define DEBUG(x) std::cerr << x << std::endl;
#else
#define DEBUG(x)
#endif

typedef std::vector <unsigned short int> ValidChars;
typedef std::vector< ValidChars > PatternSearch;

class ValidWordsNode
{
      ValidWordsNode* _child[26];
public:
      static unsigned int treeDepth; 
      ValidWordsNode()
      {
            int iii = 0;
            while(iii < 26) _child[iii++] = NULL;
      }
      
      void createTree(const std::string &validWord, unsigned int childDepth)
      {
           unsigned short int idx = validWord[childDepth++] - 'a';
           if(_child[idx]==NULL) _child[idx] = new ValidWordsNode();
           if(childDepth < treeDepth)
                _child[idx]->createTree(validWord, childDepth);
      }
      
      void getWordsMatchingPatern(const PatternSearch &pattern, unsigned int &matchCount, unsigned int childDepth)
      {
                    DEBUG("patern childDepth="<<childDepth )
           const ValidChars &validChars = pattern[childDepth++];
           unsigned short iii = 0;
           const unsigned int jjj = validChars.size();
                    DEBUG("patern jjj="<<jjj )
           if(childDepth < treeDepth)
           {
                while(iii < jjj)
                {
                     if( _child[validChars[iii]] != NULL )
                         _child[validChars[iii]]->getWordsMatchingPatern(pattern, matchCount, childDepth);
                     iii++;
                }
           }
           else
           {
                while(iii < jjj)
                {
                     if( _child[validChars[iii]] != NULL )
                         matchCount++;
                     iii++;
                }
           }
      }
};

unsigned int ValidWordsNode::treeDepth=0;


int main()
{
    int l, d, n;
    std::cin >> l >> d >> n;
    ValidWordsNode::treeDepth = l;
    ValidWordsNode rootValidwords;
    std::string validWord, patternWord;
    while(d > 0)
    {
        std::cin >> validWord;
        rootValidwords.createTree(validWord,0);
        d--;
    }
    int num=0;
    while(n > 0)
    {
        std::cin >> patternWord;
        DEBUG("patternWord="<<patternWord)
        PatternSearch pattern;
        unsigned int matchCount=0;
        size_t pos=0,prevPos=0;
        while (pos < patternWord.length())
        {
            pos = patternWord.find('(',prevPos);
            DEBUG("prevPos="<<prevPos << ", pos="<<pos)
            if(pos==prevPos)
            {
                ValidChars validChars;
                pos = patternWord.find(')',prevPos);
                DEBUG("== prevPos="<<prevPos << ", pos="<<pos)
                for(size_t iii = prevPos+1; iii < pos; iii++)
                {
                    DEBUG("==== iii="<<iii << ", patternWord[iii]="<<patternWord[iii]<<
                     ",   patternWord[iii]-'a'="<<patternWord[iii]-'a')
                    validChars.push_back(patternWord[iii]-'a');
                }
                prevPos=pos+1;
                pattern.push_back(validChars);
            }
            else
            {
                if(pos == std::string::npos) pos = patternWord.length();
                DEBUG("!= prevPos="<<prevPos << ", pos="<<pos)
                for(size_t iii = prevPos; iii < pos; iii++)
                {
                    ValidChars validChars;
                    DEBUG("!!!= iii="<<iii << ", patternWord[iii]="<<patternWord[iii] <<
                     ",   patternWord[iii]-'a'="<<patternWord[iii]-'a')
                    validChars.push_back(patternWord[iii]-'a');
                    pattern.push_back(validChars);
                }
                prevPos=pos;
            }
        }
        DEBUG("getWordsMatchingPatern")
        rootValidwords.getWordsMatchingPatern(pattern, matchCount, 0);
        std::cout << "Case #" << ++num << ": " << matchCount << std::endl;
        n--;
    }
    
    return 0;
}
