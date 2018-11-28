#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int **  load ( int inputNr )
{
    int ** array = new int * [ inputNr ];
    
    for ( int i = 0; i < inputNr ; i++ )
        array[i] = new int [ 2 ];
        
    for ( int i = 0; i < inputNr; i++ )
        cin >> array[i][0] >> array[i][1];
        
    return array;
}

int     getLength( int i )
{
    return 1 + log10(i);
}

char    getChar(int i)
{
    switch(i)
    {
        case 0: return '0';
        case 1: return '1';
        case 2: return '2';
        case 3: return '3';
        case 4: return '4';
        case 5: return '5';
        case 6: return '6';
        case 7: return '7';
        case 8: return '8';
        case 9: return '9';
    }
    return '0';
}

int     getNum(char c)
{
    switch(c)
    {
        case '0': return 0;
        case '1': return 1;
        case '2': return 2;
        case '3': return 3;
        case '4': return 4;
        case '5': return 5;
        case '6': return 6;
        case '7': return 7;
        case '8': return 8;
        case '9': return 9;
    }
    return 0;
}

int     shift(int m, int shift, int length)
{
    int num = 0;
    
    char *o_arr = new char [ length + 1 ];
    char *n_arr = new char [ length + 1 ];
    o_arr [length] = 0;
    n_arr [length] = 0;

    
    int tmp = length - 1;
    while (m)
    {
        o_arr[tmp--] = getChar(m%10);
        m/=10;
    }
    
    
    for (int i = 0; i < length; i++)
        n_arr[i] = o_arr[(i+shift)%(length)];
    /*
    for (int i = 0; i < length ; i++)
    {
        cout << o_arr[i];
    }
    
    cout << " ----- ";
    
    for (int i = 0; i < length ; i++)
    {
        cout << n_arr[i];
    }
    
    cout << " ----- ";
    */
    num = atoi(n_arr);
    
    delete [] o_arr;
    delete [] n_arr;
    
    //cout << num << endl;
    return num;
}

bool    isRecycledPair(int m, int n)
{
    //cout << "---" << endl << m << " " << n << endl;
    
    int length = getLength(m);
    //cili budeme shiftovat (length - 1) cifer
    
    for (int i = 0; i < length ; i++)
        if (shift(m, i, length) == n)
            return true;
    
    return false;
}

int     main()
{
    int inputNr;
    cin >> inputNr;
    
    int ** table = load(inputNr);
    
    for (int k = 0; k < inputNr; k++)
    {
        int cnt = 0;
        
        for (int i = table[k][0]; i <= table[k][1]; i++ )
        {
            for (int j = i + 1 ; j <= table[k][1]; j++ )
                if (isRecycledPair(i,j))    cnt++;
        }
        
        cout << "Case #" << k+1 << ": " << cnt << endl;
    }
    
    //cout << inputNr << endl;
    //for (int i = 0; i < inputNr; i++)
    //    cout << table[i][0] << " " << table[i][1] << endl;
    
    
    
    for (int i = 0; i < inputNr; i++)
        delete[]table[i];
    delete[]table;
    
    return 0;
}
