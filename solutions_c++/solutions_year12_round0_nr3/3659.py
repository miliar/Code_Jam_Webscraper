// code_jam2012-3.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;

int RecycledNumbers(int start, int end)
{
    set<int> table;
    char buf[20];
    int count(0);
    char * p = buf;
    for (int num=start; num <=end; num++) {
        memset(buf, '\0', 20);
        p = buf;
         _itoa(num, p, 10);
         int m = strlen(p);
         for (unsigned j = 0; j < m-1; j++) {
             p[m] = p[0];
            // p[m+1] = '\0';
             p++;
             if (p[0] == '0' )
                 continue;
             int pair_num = atoi(p);
             if (table.find(pair_num) != table.end())
                 continue;
             if (pair_num > num && pair_num <= end) 
                 count++;
             table.insert(pair_num);
         }
        table.clear();
    }
    return count;
}

int main(int argc, char* argv[])
{
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    clock_t start_clock = clock();

    int n;
    fin >> n;

    int case_no = 0;
    for (int i=0; i<n; i++) {
        int start,end;
        fin >> start >> end;
        int ans = RecycledNumbers(start, end);
        fout << "Case #" << ++case_no << ": " << ans << endl;
    }
    clock_t end_clock = clock();
    // cout << (end_clock - start_clock) / double(CLOCKS_PER_SEC) << endl;

	return 0;
}

