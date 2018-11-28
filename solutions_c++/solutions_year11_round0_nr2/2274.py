#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

void solveCase(FILE *fp, int index);
void processLastElement(void);
void checkListForOpposition(void);
char getCombinationResult(char elem1, char elem2);
bool oppositionExists(char elem1, char elem2);

struct Combination
{
    char element1, element2;
    char result;
};

struct Opposed
{
    char element1, element2;
};

#define MAX_DICTIONARY (40)
struct Combination combinationDictionary[MAX_DICTIONARY];
int sizeOfCombinationDictionary = 0;

struct Opposed opposedDictionary[MAX_DICTIONARY];
int sizeOfOpposedDictionary = 0;

#define MAX_SPELL (110)
int numberOfElements;
char spell[MAX_SPELL];

int listSize;
char list[MAX_SPELL];

int main()
{
    FILE *fp = fopen("output.txt", "w");

    int numberOfCases;

    fscanf(stdin, "%d", &numberOfCases);

    for(int i = 0; i < numberOfCases; i++)
    {
        solveCase(fp, i);
    }

    fclose(fp);
    return 0;
}

void solveCase(FILE *fp, int index)
{
    //printf("Case #%d =============\n", index);

    char combination[10];
    fscanf(stdin, "%d", &sizeOfCombinationDictionary);
    for(int i=0; i < sizeOfCombinationDictionary; i++)
    {
        fscanf(stdin, "%s", combination);
        combinationDictionary[i].element1 = combination[0];
        combinationDictionary[i].element2 = combination[1];
        combinationDictionary[i].result = combination[2];
        //printf("Combination %d: %c + %c = %c\n", i, combinationDictionary[i].element1, combinationDictionary[i].element2, combinationDictionary[i].result);
    }

    fscanf(stdin, "%d", &sizeOfOpposedDictionary);
    for(int i=0; i < sizeOfOpposedDictionary; i++)
    {
        fscanf(stdin, "%s", combination);
        opposedDictionary[i].element1 = combination[0];
        opposedDictionary[i].element2 = combination[1];
        //printf("Opposition %d: %c & %c\n", i, opposedDictionary[i].element1, opposedDictionary[i].element2);
    }

    fscanf(stdin, "%d", &numberOfElements);
    fscanf(stdin, "%s", spell);

    //printf("Spell: %s\n", spell);

    listSize = 0;
    for(int i = 0; i < numberOfElements; i++)
    {
        list[listSize] = spell[i];
        listSize++;

        processLastElement();
    }

    fprintf(fp, "Case #%d: [", (index + 1));
    for(int i=0; i < listSize; i++)
    {
        fprintf(fp, "%c", list[i]);
        if(i + 1 < listSize)
        {
            fprintf(fp, ", ");
        }
    }
    fprintf(fp, "]\n");
}

void processLastElement(void)
{
    if(listSize > 1)
    {
        char combinationResult = getCombinationResult(list[listSize - 1], list[listSize - 2]);
        if(combinationResult != -1)
        {
            list[listSize - 2] = combinationResult;
            listSize--;
        }

        checkListForOpposition();
    }
}

void checkListForOpposition(void)
{
    for(int i=0; i < listSize - 1; i++)
    {
        if(oppositionExists(list[i], list[listSize - 1]))
        {
            listSize = 0; // clear list
        }
    }
}

char getCombinationResult(char elem1, char elem2)
{
    for(int i=0; i < sizeOfCombinationDictionary; i++)
    {
        if((combinationDictionary[i].element1 == elem1 && combinationDictionary[i].element2 == elem2) ||
           (combinationDictionary[i].element1 == elem2 && combinationDictionary[i].element2 == elem1))
       {
           return combinationDictionary[i].result;
       }
    }
    return -1;
}

bool oppositionExists(char elem1, char elem2)
{
    for(int i=0; i < sizeOfOpposedDictionary; i++)
    {
        if((opposedDictionary[i].element1 == elem1 && opposedDictionary[i].element2 == elem2) ||
           (opposedDictionary[i].element1 == elem2 && opposedDictionary[i].element2 == elem1))
       {
            return true;
       }
    }
    return false;
}
