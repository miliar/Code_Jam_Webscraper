#include <iostream>

using namespace std;

static const int maxB = 256;
static const int maxC = 9;
static const int maxL = 100;
int code[maxB];
int testNum;
int testIndex;
char com[maxC][maxC];
int opp[maxC][maxC];
int countC[maxC];

int len;
char elems[maxL];

char list[maxL];
int listLen;


void initCode()
{
    for (int i = 0; i < maxB; ++i) code[i] = 0;
    code['Q'] = 1;
    code['W'] = 2;
    code['E'] = 3;
    code['R'] = 4;
    code['A'] = 5;
    code['S'] = 6;
    code['D'] = 7;
    code['F'] = 8;      
}


void init()
{
    memset( com, 0, sizeof( com ) );
    memset( opp, 0, sizeof( opp ) );
    memset( countC, 0 ,sizeof( countC ) );
    listLen = 0;
}

void readInput()
{
    int m, n;
    char c1, c2, c3, c;
    cin >> m;
    //cout << "Test " << testIndex << ":\n";
    //cout << m;
    for (int i = 0; i < m; ++i)
    {
        cin >> c1 >> c2 >> c3;   
        //cout << " " << c1 << c2 << c3;
        com[code[c1]][code[c2]] = c3;
        com[code[c2]][code[c1]] = c3;
    }
    
    cin >> n;
    //cout << " " << n;
    for (int i = 0; i < n; ++i)
    {
        cin >> c1 >> c2;
        //cout << " " << c1 << c2;
        opp[code[c1]][code[c2]] = 1;
        opp[code[c2]][code[c1]] = 1;
    }
    
    cin >> len;
    //cout << " " << len << " ";
    for (int i = 0; i < len; ++i)
    {
        cin >> c;
        elems[i] = c;
        //cout << c;
    }
    //cout << "\n";
    
    //for (int i = 0; i < maxC; ++i)
    //{
        //for (int j = 0; j < maxC; ++j)        
            //cout << (com[i][j] ? com[i][j] : '.') << " ";
        //cout << "\n";
    //}    
    //cout << "\n";
    //for (int i = 0; i < maxC; ++i)
    //{
        //for (int j = 0; j < maxC; ++j)        
            //cout << opp[i][j] << " ";
        //cout << "\n";
    //}    
}

void compute()
{
    for (int i = 0; i < len; ++i)
    {
        int next = elems[i];
        int nextCode = code[next];
        char last = '\0';        
        int lastCode = 0;        
        if (listLen > 0) 
        {
            last = list[listLen-1];
            lastCode = code[last];
        }
        if (com[lastCode][nextCode])
        {
           list[listLen-1] = com[lastCode][nextCode];
           --countC[lastCode];
        }
        else 
        {
            list[listLen] = next;
            ++listLen;            
            for (int j = 1; j < maxC; ++j)
                if (countC[j] && opp[j][nextCode])        
                {
                    listLen = 0;
                    memset( countC, 0, sizeof( countC ) );
                    ////cout << "opp: " << j << " " << countC[j] << " ";
                    break;
                }
            ++countC[nextCode];
        }
        ////cout << "Result = ";
        //for (int i = 0; i < listLen; ++i)
            //cout << list[i];
        //cout << "- count = ";
        //for (int i = 0; i < maxC; ++i)    
        //{
            //cout << countC[i] << " ";
        //}
        //cout << "\n";
    }
    cout << "Case #" << testIndex << ": [";
    if (listLen > 0) 
    {
        cout << list[0];
        for (int i = 1; i < listLen; ++i)
            cout << ", " << list[i];
    }
    cout << "]\n";    
}

int main()
{
    initCode();
    cin >> testNum;    
    for (testIndex = 1; testIndex <= testNum; ++testIndex)
    {
        init();    
        readInput();  
        compute();      
    }
}
