
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

struct tCharMap
{
    char a;
    char b;
};

tCharMap TCHARMAP[26] =
{
  {'a','y'},
  {'b','n'},
  {'c','f'},
  {'d','i'},
  {'e','c'},
  {'f','w'},
  {'g','l'},
  {'h','b'},
  {'i','k'},
  {'j','u'},
  {'k','o'},
  {'l','m'},
  {'m','x'},
  {'n','s'},
  {'o','e'},
  {'p','v'},
  {'q','z'},
  {'r','p'},
  {'s','d'},
  {'t','r'},
  {'u','j'},
  {'v','g'},
  {'w','t'},
  {'x','h'},
  {'y','a'},
  {'z','q'}
};

typedef enum EStatLine
{
   ELineNum,
   ELineText
}
EStatLine;

char getRealChar( char c )
{
    char ch = c;

    for(int i=0;i<26;i++)
    {
        if( c == TCHARMAP[i].b )
        {
            ch = TCHARMAP[i].a;
        }
    }

    return ch;
}

std::string translate( std::string g )
{
    char ch[g.length()+1];// = g.c_str();
    char len = g.length();
    std::string retStr;

    strcpy(ch,g.c_str());

    for(int i=0;i<len;i++)
    {
        if(ch[i] == ' ')
        {
           retStr.push_back(' ');
        }
        else
        {
           char a = getRealChar(ch[i]);
           retStr.push_back(a); 
        }
    }

    return retStr;
}

bool createOutput(std::string& filename, std::vector<std::string>& txts)
{
    std::ofstream outstream(filename.c_str());
    bool retValue = false;

    std::cout << "VECTOR SIZE = " << txts.size() << "\n";

    if( outstream.is_open() )
    {
        std::vector<std::string>::iterator iter;
        int sz = 1;

        for(iter=txts.begin();iter!=txts.end();iter++)
        {
            std::string result;

            std::stringstream sstr;
            sstr << "Case #" << sz << ": ";
 
            result = sstr.str();
            result.append(*iter);
            result.append("\n");

            outstream << result;
            sz++;
        }
        outstream.close();
        retValue = true;
    }

    return retValue;
}


int main(int argc, char** argv)
{
//    for(int a=0;a<26;a++)
//        std::cout << TCHARMAP[a].a << " " << TCHARMAP[a].b << "\n";

   if( argc <= 2 )
   {
       std::cout << "No param\n";
       return 0;
   }

   std::string iargc(argv[1]);
   std::string oargc(argv[2]);

   std::string line;
   std::ifstream instream(iargc.c_str());

   EStatLine startLine = ELineNum;
   
   std::vector<std::string> plainText;

   if(instream.is_open())
   {
       while(instream.good())
       {
           getline(instream,line);
           //std::cout << "LINE = " << line << "\n";
           switch(startLine)
           {
            case ELineNum:
                startLine = ELineText;
                break;
            case ELineText:
                //std::cout << translate(line) << "\n";
                if(!line.empty())
                {
                    plainText.push_back(translate(line));
                }
                break;
           };
       }
       instream.close();
   }
   else
   {
      std::cout << "File " << iargc << " can't open.\n";
      return 0;
   } 

   if( createOutput( oargc, plainText ) )
   {
      std::cout << "Create output successful!\n";
   }
   else
   {
      std::cout << "Create output failed\n";
   }

    return 0;
}


