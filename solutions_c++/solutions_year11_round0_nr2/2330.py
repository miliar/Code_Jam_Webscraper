// Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iosfwd>
#include <string>
#include <iostream>
#include <fstream>
#include <strstream>
#include <algorithm>


namespace{
    int CaseNum;
    bool isGetCaseNum = false;
    const char* caseFile = "D:\\My Documents\\Visual Studio 2010\\Projects\\GoogleJam\\Debug\\B-large.in";
    const char* resultFile = "D:\\My Documents\\Visual Studio 2010\\Projects\\GoogleJam\\Debug\\resultFile.txt";

    typedef std::vector<std::string > DissList;
    typedef std::vector<std::pair <std::string ,std::string> > CombinList;
    typedef std::string WORDS;
    std::string baseElementsList = "QWERASDF"; 
    //enum baseElemnt
    //{
    //    Q, W, E, R, A, S, D, F
    //};
}
bool getWords(std::string str,CombinList& cList,DissList& dList,WORDS& magikaWord);
bool CombineAndRemove(WORDS& magikaWord,CombinList& cList , DissList& dList);
int getElementID(char word);
int _tmain(int argc, _TCHAR* argv[])
{
    using namespace std;
    ifstream ifs;
    ifs.open(caseFile);
    string str;
    int crrentCaseNum = 1;

    while( getline(ifs,str) )
    {    
        if (!isGetCaseNum)
        {
            CaseNum = atoi( str.c_str() );
            isGetCaseNum = true;
            continue;
        }
        CombinList cList;
        cList.resize(8,make_pair("",""));
        DissList dList;
        dList.resize(8,"");
        WORDS word;
        getWords(str,cList,dList,word);
        CombineAndRemove(word,cList,dList);


        ofstream ofs;
        ofs.open(resultFile,ofstream::app);
        ofs<<"Case #"<<crrentCaseNum++<<": [";
        for (WORDS::iterator it = word.begin(); it != word.end() ; it++)
        {
            if (it != word.end()-1)
            { 
                ofs<<*it<<", ";
            }
            else
            {
                ofs<<*it;
            }
           
        }
        ofs<<"]"<<endl;
        ofs.clear();
        ofs.close();


    }
    return 0;
}

bool getWords( std::string str,CombinList& cList,DissList& dList,WORDS& magikaWord )
{
    using namespace std;
    istrstream is(str.c_str());
    string word;
    int kNumOfCList = 0;
    int kNumOfDList = 0;
    int kMagikaWordNum = 0;
    bool isGetCNum = false;
    bool isGetDNum = false;
    bool isGetMagikaWordNum = false;
    bool isGetCList = false;
    bool isGetDList = false;
    bool isGetMagikaWord = false;
    int itCList = 0;
    int itDList = 0;
    while(is>>word)
    {
        if (!isGetCNum)
        {
            kNumOfCList = atoi(word.c_str());
            isGetCNum = true;
            continue;
        }
        if(itCList++ < kNumOfCList)
        {
            string combinWord = word;
            char combinChar1 = combinWord[0];
            char combinChar2 = combinWord[1];
            char resultChar = combinWord[2];
            cList[getElementID(combinChar1)].first.push_back(combinChar2);
            cList[getElementID(combinChar1)].second.push_back(resultChar);
            cList[getElementID(combinChar2)].first.push_back(combinChar1);
            cList[getElementID(combinChar2)].second.push_back(resultChar);
            continue;
        }

        //if (cList.size() != numOfCList)
        //{
        //    cout<<"err!!C";
        //    return false;
        //}
        if (!isGetDNum)
        {
            kNumOfDList = atoi(word.c_str());
            isGetDNum = true;
            continue;
        }
        if(itDList++ < kNumOfDList)
        {
            string dissWord = word;
            char dissChar1 = dissWord[0];
            char dissChar2 = dissWord[1];
            dList[getElementID(dissChar1)].push_back(dissChar2);
            dList[getElementID(dissChar2)].push_back(dissChar1);
            continue;
        }

        //if (dList.size() != numOfDList)
        //{
        //    cout<<"err!!D";
        //    return false;
        //}

        if (!isGetMagikaWordNum)
        {
            kMagikaWordNum = atoi(word.c_str());
            isGetMagikaWordNum = true;
            continue;
        }
        magikaWord = word;

        if (magikaWord.size() != kMagikaWordNum)
        {
            cout<<"err!!M";
            return false;
        }
    }
   


    return true;
}

bool CombineAndRemove(WORDS& magikaWord,CombinList& cList , DissList& dList)
{
    using namespace std;
    string newMagikaWord;
    //vector <string> combineBlockList;
    for (WORDS::iterator it = magikaWord.begin(); it != magikaWord.end()  ; it++)
    {
        char currentMagikaChar = *it;
        int currentElementID = getElementID(currentMagikaChar);
        //combine
        if ( !cList[currentElementID].first.empty() && !newMagikaWord.empty() )
        {
            string test = cList[currentElementID].first;
            char testChar = newMagikaWord.back();
            string::size_type combinePos = test.find(testChar);
            if (combinePos < cList[currentElementID].first.size())
            {
                /*string blockStr1 , blockStr2;
                blockStr1.push_back(testChar);
                blockStr1.push_back(currentMagikaChar);
                vector<string>::iterator itOfBlock = find(combineBlockList.begin(),combineBlockList.end(),blockStr1);
                if( itOfBlock == combineBlockList.end())
                {*/
                    newMagikaWord.back() = cList[currentElementID].second[combinePos];
                  /*  blockStr2.push_back(currentMagikaChar);
                    blockStr2.push_back(testChar);
                    combineBlockList.push_back(blockStr1);
                    combineBlockList.push_back(blockStr2);*/
                    continue;
               // };
               
            }
        }
        
        //remove
        bool isRemoved = false;
        if (!dList[currentElementID].empty()  && !newMagikaWord.empty() )
        { 
            for (string::size_type i = 0; i < dList[currentElementID].size() ; i++)
            {
                char removeElement =  dList[currentElementID][i];
                string::size_type removePos = newMagikaWord.find_last_of(removeElement);
                if (removePos < newMagikaWord.size())
                {
                    newMagikaWord.clear();
                    isRemoved = true;
                    break;
                }
            }
        }
       
        if (!isRemoved)
        {
            newMagikaWord.push_back(currentMagikaChar);
        }

    }
    magikaWord = newMagikaWord;
    return true;
}

int getElementID( char word )
{
    return baseElementsList.find(word);
}