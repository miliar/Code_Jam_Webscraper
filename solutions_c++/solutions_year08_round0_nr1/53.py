#include <iostream>
#include <fstream>
#include <map>
#include <string>

std::ifstream in("save.in");
std::ofstream out("save.out");

int cases;

int engine_count;
std::map< std::string, int > engines;
int query_count;
int queries[1000];

int best[1001][100];

int process()
{
    in >> engine_count;
    std::string s;
    std::getline(in, s);
    for (int i = 0; i < engine_count; i++) {
        std::getline(in, s);
        engines[s] = i;
    }
    
    in >> query_count;
    std::getline(in, s);
    for (int i = 0; i < query_count; i++) {
        std::getline(in, s);
        queries[i] = engines[s];
    }
    
    for (int i = 0; i <= query_count; i++)
    for (int j = 0; j < engine_count; j++)
        best[i][j] = 1001;

    for (int i = 0; i < engine_count; i++)
        best[0][i] = 0;

    for (int i = 0; i < query_count; i++)
    for (int j = 0; j < engine_count; j++) {
        if (queries[i] == j) continue;
        for (int k = 0; k < engine_count; k++)
            best[i+1][k] = std::min(best[i+1][k], best[i][j] + 1);
        best[i+1][j] = std::min(best[i+1][j], best[i][j]);
    }

    int min = 1001;
    for (int i = 0; i < engine_count; i++)
        min = std::min(min, best[query_count][i]);

    return min;
}

int main()
{
    in >> cases;

    for (int i = 0; i < cases; i++)
        out << "Case #" << i + 1 << ": " << process() << "\n"; 
    
    return 0;
}

