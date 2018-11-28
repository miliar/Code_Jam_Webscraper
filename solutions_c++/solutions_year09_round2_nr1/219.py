#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <vector>
#include <string>
#include <set>

using namespace std;

vector< string > tt;
vector< int > l, r;
vector<bool> meta;


vector< set<string> > animal;

ifstream fin;

void read_tree()
{
    int n;
    vector<int> stack;
    string line;
    string total;
    char *ptr;
    char *buffer;
    vector<char*> tokens, new_tokens;
    fin >> n;
    
    for(int i = 0; i < n; i++)
    {
        do
        {
            getline(fin, line);
        } while(line.size() == 0);
        
        total += line;
    }
    
    buffer = new char[total.length() + 10];
    strcpy(buffer, total.c_str());
//    cout << buffer << endl;
    ptr = strtok(buffer, "( )");
    while(ptr != NULL)
    {
        if(strlen(ptr) > 0)
        tokens.push_back(ptr);
        ptr = strtok(NULL, "( )");
    }
    
    tt.clear();
    
    for(int i = 0; i < tokens.size(); i++)
    {
        tt.push_back(string(tokens[i]));
    }
}

void build_tree()
{
    vector<int> stack;
    
    l.clear();
    r.clear();
    meta.clear();
    
    l.resize(tt.size());
    r.resize(tt.size());
    meta.resize(tt.size());
    
    for(int i = 0; i < tt.size(); i++)
    {
        if(tt[i][0] >= 'a' && tt[i][0] <= 'z')
        {// feature
            meta[i - 1] = true;
        }
    }
    for(int i = 0; i < tt.size(); i++)
    {
        if(tt[i][0] >= 'a' && tt[i][0] <= 'z')
        {// feature
            continue;
        }
        else
        {// weight;
            stack.push_back(i);
            l[i] = r[i] = -1;

            if(meta[i] == false)
            {
                int cur_index;
                cur_index = stack.back();
                stack.pop_back();
                
                while(stack.size() > 0)
                {
                    int last_index = stack.back();
                    if(l[last_index] == -1)
                    {
                        l[last_index] = cur_index;
                        break;
                    }
                    else
                    {
                        r[last_index] = cur_index;
                        cur_index = last_index;
                        stack.pop_back();
                    }
                }
            }
        }
    }
}

void read_animal()
{
    int n, m;
    string name, f;
    animal.clear();
    fin >> n;
    animal.resize(n);
    for(int i = 0; i < n; i++)
    {
        fin >> name;
        fin >> m;
        for(int j = 0; j < m ; j++)
        {
            fin >> f;
            animal[i].insert(f);
        }
    }
}

double get_probability(set<string>& ani)
{
    int pos;
    double prob = 1.0;
    if(tt.size() == 0) return 1.0; // exception
    
    pos = 0;
    while(true)
    {
        prob *= atof(tt[pos].c_str());
        if(meta[pos] == true)
        {
            if(ani.count(tt[pos + 1]) > 0)
            {
                pos = l[pos];
            }
            else
            {
                pos = r[pos];
            }
        }
        else
        {
            return prob;
        }
    }
}

int main()
{
    ofstream fout("A.out");
    int N;
    fin.open("A.in");
    fin >> N;
    for(int i = 1; i <= N; i++)
    {
        read_tree();
        build_tree();
        read_animal();
        
        fout << "Case #" << i << ":" << endl;
        for(int j = 0; j < animal.size(); j++)
        {
            fout << get_probability(animal[j]) << endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}