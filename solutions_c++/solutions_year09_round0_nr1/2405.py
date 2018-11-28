#include <iostream>
#include <string>

using namespace std;

struct processedInput
{
    int start;
    int end;
    bool single;
};

/*int countSections(string input)
{
    int count = 0;
    int previous = -1;
    
    previous = input.find_first_of('(', previous + 1);
    while(previous != -1)
    {    
        count++;
        previous = input.find_first_of('(', previous + 1);
    }
    
    return count;
}*/

processedInput *preprocessInput(string input, int L, int D, int N)
{
    processedInput *pIn = new processedInput[L];
    int currentPosition = 0;

    for(int x = 0; x < L; x++)
    {
        if(input.at(currentPosition) == '(')
        {
            pIn[x].single = false;
            pIn[x].start = currentPosition + 1;
            currentPosition = input.find_first_of(')', currentPosition) + 1;
            pIn[x].end = currentPosition - 2;
        }
        else
        {
            pIn[x].single = true;
            pIn[x].start = currentPosition;
            pIn[x].end = currentPosition;
            currentPosition++;
        }
    }

    return pIn;
}

void handleTestCase(string input, string **m, int L, int D, int N, int caseNum, processedInput *pIn)
{
    int possibilityCount = 0;
    /*string testCase(L, ' ');
    int index = 0;
    
    for(int x = 0; x < L; x++)
    {
        if(input[0] == '(')
        {
            
        }
        else
        {
            testCase[x] = input[index];
        }
    }*/

    for(int x = 0; x < D; x++)
    {
        bool possible = true;
        
        for(int y = 0; y < L; y++)
        {
            if(pIn[y].single)
            {
                if(input.at(pIn[y].start) != m[x]->at(y))
                {
                    possible = false;
                    break;
                }
            }
            else
            {
                bool subPossible = false;
                
                for(int z = pIn[y].start; z <= pIn[y].end; z++)
                {
                    if(input.at(z) == m[x]->at(y))
                    {
                        subPossible = true;
                        break;
                    }
                }
                
                if(!subPossible)
                {
                    possible = false;
                    break;
                }
            }
        }
        
        if(possible)
        {
            possibilityCount++;
        }
    }

    cout << "Case #" << caseNum << ": " << possibilityCount << endl;
}

int main(int argc, char *argv[])
{
    string input;
    int L, D, N;
    
    cin >> L >> D >> N;
    
    string *m[D];
    
    getline(cin, input);
    for(int x = 0; x < D; x++)
    {
        getline(cin, input);
        m[x] = new string(input.c_str());
    }
    
    int caseNum = 1;
    
    for(int x = 0; x < N; x++)
    {
        getline(cin, input);
        handleTestCase(input, m, L, D, N, caseNum, preprocessInput(input, L, D, N));
        caseNum++;
    }
    
    return 0;
}
