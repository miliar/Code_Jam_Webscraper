#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector<int> stack;
vector<bool> check;
int graph[100][100];
int n, m;
int best_solution;

void backtracking(int t)
{
    if(t == n)
    {
        if(best_solution > stack.size())
        {
            best_solution = stack.size();
        }
        return;
    }
    for(int i = 0; i < n; i++)
    {
        if(check[i] == true) continue;
        bool flag = true;
        for(int j = 0; j < n; j++)
        {
            if(check[j] == true) continue;
            if(graph[j][i] == 1)
            {
                flag = false;
                break;
            }
        }
        if(flag)
        {
            // insert to fit
            check[i] = true;
            for(int j = 0; j < stack.size(); j++)
            {
                if(graph[stack[j]][i] == 1)
                {
                    int tmp = stack[j];
                    stack[j] = i;
                    backtracking(t + 1);
                    stack[j] = tmp;
                }
            }
            
            if(stack.size() + 1 < best_solution)
            {
                stack.push_back(i);
                backtracking(t + 1);
                stack.pop_back();
            }
            
            check[i] = false;
            break;
        }
    }
}

int main()
{
    ifstream fin("c.in");
    ofstream fout("c.out");
    int N;
    fin >> N;
    for(int i = 1; i <= N; i++)
    {
        int v[100][25];
        fin >> n >> m;
        for(int j = 0; j < n; j++)
        {
            for(int k = 0; k < m; k++)
            {
                fin >> v[j][k];
            }
        }
        
        // make graph
        for(int j = 0; j < n; j++)
        {
            for(int k = 0; k < n; k++)
            {
                graph[j][k] = 1;
                for(int l = 0; l < m ;l++)
                {
                    if(v[j][l] >= v[k][l]) 
                    {
                        graph[j][k] = 0;
                        break;
                    }
                }
            }
        }
        
        stack.clear();
        check.clear();
        
        check.resize(n);
        for(int j = 0; j < n; j++) check[j] = false;
        best_solution = n;
        backtracking(0);
        
        
        fout << "Case #" << i << ": " << best_solution << endl;
        
    }
    fin.close();
    fout.close();
    return 0;
}