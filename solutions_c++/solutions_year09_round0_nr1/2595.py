/* 
 * File:   main.cpp
 * Author: root
 *
 * Created on September 3, 2009, 11:31 AM
 */

//11:25

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;



class LetterSlot
{
public:
    char* letters;
    unsigned long letterCount;

    LetterSlot()
    {
        letterCount = 0;

        letters = (char*)malloc(letterCount + 1);
        strcpy(letters, "");
    }

    void addLetter(char letter)
    {
        letterCount++;
        letters = (char*)realloc(letters, letterCount + 1);
        letters[letterCount - 1] = letter;
        letters[letterCount] = 0;
    }

    void print()
    {
        cout<<"Letter Count: "<<letterCount;
        cout<<endl<<"Letters: "<<letters;
    }

    bool matches(char c)
    {
        for(unsigned long i = 0; i < letterCount; i++)
            if(c == letters[i])
                return true;

        return false;
    }

    ~LetterSlot()
    {
        free(letters);
    }
};

class WordPattern
{
public:
    char* pattern;
    LetterSlot* letterSlots;
    unsigned long letterSlotCount;

    void computeLetterSlotCount()
    {
        letterSlotCount = 0;
        bool bracketOpen = false;

        for(unsigned long i = 0; i < strlen(pattern); i++)
        {
            if(pattern[i] == '(')
                bracketOpen = true;

            if(pattern[i] == ')')
                bracketOpen = false;

            if(!bracketOpen)
                letterSlotCount++;
        }
    }

    WordPattern(fstream& fin)
    {
        char* tmp = new char[0xFFFFFF];

        fin>>tmp;

        pattern = new char[strlen(tmp) + 1];
        strcpy(pattern, tmp);

        delete[] tmp;

        computeLetterSlotCount();

        letterSlots = new LetterSlot[letterSlotCount];

        unsigned long letterSlotIndex = 0;
        bool bracketOpen = false;
        unsigned long bracketOpenIndex = 0;

        for(unsigned long i = 0; i < strlen(pattern); i++)
        {
            if(pattern[i] == '(')
            {
                bracketOpenIndex = i;
                bracketOpen = true;
            }

            if(pattern[i] != '(' && pattern[i] != ')')
                letterSlots[letterSlotIndex].addLetter(pattern[i]);

            if(pattern[i] == ')')
                bracketOpen = false;

            if(!bracketOpen)
                letterSlotIndex++;
        }
    }

    bool matches(char* word)
    {
        if(strlen(word) != letterSlotCount)
            return false;

        for(unsigned long i = 0; i < letterSlotCount; i++)
            if(!letterSlots[i].matches(word[i]))
                return false;

        return true;
    }

    void print()
    {
        cout<<"Pattern: "<<pattern;
        cout<<endl<<"Slots:";
        cout<<endl<<"{";

        for(unsigned long i = 0; i < letterSlotCount; i++)
        {
            cout<<endl;
            letterSlots[i].print();
        }

        cout<<endl<<"}";
    }

    ~WordPattern()
    {
        delete[] pattern;
        delete[] letterSlots;
    }
};

class Dictionary
{
public:
    unsigned long letterCount;
    unsigned long wordCount;
    char** words;

    Dictionary(fstream& fin, unsigned long letterCount, unsigned long wordCount)
    {
        this->letterCount = letterCount;
        this->wordCount = wordCount;

        words = new char*[wordCount];

        char* tmp = new char[0xFFFFFF];

        for(unsigned long i = 0; i < wordCount; i++)
        {
            fin>>tmp;
            words[i] = new char[strlen(tmp) + 1];
            strcpy(words[i], tmp);
        }

        delete[] tmp;

    }

    bool hasWord(char* word)
    {
        for(unsigned long i = 0; i < wordCount; i++)
            if(!strcmp(word, words[i]))
                return true;
        
        return false;
    }

    unsigned long getMatchingWordCount(WordPattern* wordPattern)
    {
        unsigned long result = 0;
        
        for(unsigned long i = 0; i < wordCount; i++)
            if(wordPattern->matches(words[i]))
                result++;

        return result;
    }

    ~Dictionary()
    {
        for(unsigned long i = 0; i < wordCount; i++)
            delete[] words[i];
            
        delete[] words;
    }

};

/*
 * 
 */
int main(int argc, char** argv)
{
    fstream fin("/tmp/alarge.in", ios::in | ios::binary);
    fstream fo("/tmp/alarge.out", ios::out | ios::binary);

    unsigned long letterCount;
    unsigned long dictionaryWordCount;
    unsigned long testCaseCount;

    fin>>letterCount;
    fin>>dictionaryWordCount;
    fin>>testCaseCount;

    Dictionary dictionary(fin, letterCount, dictionaryWordCount);

    for(unsigned long testCase = 0; testCase < testCaseCount; testCase++)
    {
        WordPattern wordPattern(fin);

        //wordPattern.print();

        unsigned long matchingWordCount = dictionary.getMatchingWordCount(&wordPattern);
        //cout<<endl<<"Matching Word Count: "<<matchingWordCount;

        //getchar();
        fo<<"Case #"<<(testCase + 1)<<": "<<matchingWordCount<<endl;
    }

    fin.close();
    fo.close();

    return (EXIT_SUCCESS);
}

