#include <fstream>

using namespace std;

long getRecyclingNumberCount2(long A, long B)
{
    long m;
    long count = 0;
    for (long n = A; n <= B;n++)
    {
        // ab - ba
        m = (n % 10) * 10 + (n / 10);
        if (A <= m && m <= B && n < m)
            count++;
    }
    return count;
}

long getRecyclingNumberCount3(long A, long B)
{
    long m;
    long count = 0;
    for (long n = A; n <= B; n++)
    {
        // abc - cab
        m = (n % 10) * 100 + (n / 10);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abc - bca
        m = (n % 100) * 10 + (n / 100);
        if (A <= m && m <= B && n < m)
            count++;
    }
    return count;
}

long getRecyclingNumberCount4(long A, long B)
{
    long m;
    long count = 0;
    for (long n = A; n <= B; n++)
    {
        // abcd - dabc
        m = (n % 10) * 1000 + (n / 10);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcd - cdab
        m = (n % 100) * 100 + (n / 100);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcd - bcda
        m = (n % 1000) * 10 + (n / 1000);
        if (A <= m && m <= B && n < m)
            count++;
    }
    return count;
}

long getRecyclingNumberCount5(long A, long B)
{
    long m;
    long count = 0;
    for (long n = A; n <= B; n++)
    {
        // abcde - eabcd
        m = (n % 10) * 10000 + (n / 10);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcde - deabc
        m = (n % 100) * 1000 + (n / 100);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcde - cdeab
        m = (n % 1000) * 100 + (n / 1000);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcde - bcdea
        m = (n % 10000) * 10 + (n / 10000);
        if (A <= m && m <= B && n < m)
            count++;
    }
    return count;
}

long getRecyclingNumberCount6(long A, long B)
{
    long m;
    long count = 0;
    for (long n = A; n <= B; n++)
    {
        // abcdef - fabcde
        m = (n % 10) * 100000 + (n / 10);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcdef - efabcd
        m = (n % 100) * 10000 + (n / 100);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcdef - defabc
        m = (n % 1000) * 1000 + (n / 1000);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcdef - cdefab
        m = (n % 10000) * 100 + (n / 10000);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcdef - bcdefa
        m = (n % 100000) * 10 + (n / 100000);
        if (A <= m && m <= B && n < m)
            count++;
    }
    return count;
}

long getRecyclingNumberCount7(long A, long B)
{
    long m;
    long count = 0;
    for (long n = A; n <= B; n++)
    {
        // abcdefg - gabcdef
        m = (n % 10) * 1000000 + (n / 10);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcdefg - fgabcde
        m = (n % 100) * 100000 + (n / 100);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcdefg - efgabcd
        m = (n % 1000) * 10000 + (n / 1000);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcdefg - defgabc
        m = (n % 10000) * 1000 + (n / 10000);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcdefg - cdefgab
        m = (n % 100000) * 100 + (n / 100000);
        if (A <= m && m <= B && n < m)
            count++;
        
        // abcdefg - bcdefga
        m = (n % 1000000) * 10 + (n / 1000000);
        if (A <= m && m <= B && n < m)
            count++;
    }
    return count;
}

long getRecyclingNumberCount(long A, long B)
{
    if (A < 10)
        return 0;
    if (A < 100)
        return getRecyclingNumberCount2(A, B);
    if (A < 1000)
        return getRecyclingNumberCount3(A, B);
    if (A < 10000)
        return getRecyclingNumberCount4(A, B);
    if (A < 100000)
        return getRecyclingNumberCount5(A, B);
    if (A < 1000000)
        return getRecyclingNumberCount6(A, B);
    if (A < 10000000)
        return getRecyclingNumberCount7(A, B);
}

int main()
{
    short T;
    long A, B;
    
    ifstream fin ("C_small_input.txt");
    ofstream fout ("C_small_output.txt");
    
    fin >> T;
    
    for (int i = 1; i <= T; i++)
    {
        fin >> A >> B;
        fout << "Case #" << i << ": " << getRecyclingNumberCount(A, B) << "\n";
    }
    
    fin.close();
    return 0;
}
