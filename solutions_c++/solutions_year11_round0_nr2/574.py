#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<string.h>

using namespace std;
#define cout fout
int T,C,D,N;
string baselist;

char combine[200][200];
bool oppose[200][200];

ifstream fin("testin.txt");
ofstream fout("out.txt");

vector<char> list;

void checkCombine()
{
    if(list.size() <= 1)
        return;
    int n = list.size();
    char t = combine[(int)list[n - 1]][(int)list[n - 2]];
    if(t == 0)
        return;
    list.pop_back();
    list.pop_back();
    list.push_back(t); 
}

void checkOppose()
{
    for(int i = 0;i < list.size() - 1;++i)
        if(oppose[(int)list[i]][(int)list[list.size() - 1]])
        {
            list.clear();
            return;
        }
}

void solve(int num)
{
    list.clear();
    for(int i = 0;i < N;++i)
    {
        list.push_back(baselist[i]);
        checkCombine();
        checkOppose();
    }   
    if(list.size() > 0)
    { 
        cout << "Case #" << num << ": [";
        for(int i = 0;i < list.size() - 1;++i)
            cout << list[i] << ", ";
        cout << list[list.size() - 1] << "]" << endl;
    }else{
        cout << "Case #" << num << ": []" << endl;    
    }
}

int main()
{
    fin >> T;
    for(int i = 1;i <= T;++i)
    {
        memset(combine,0,sizeof(combine));
        memset(oppose,false,sizeof(oppose));
        fin >> C;
        for(int i = 1;i <= C;++i)
        {
            string temp;
            fin >> temp;
            combine[(int)temp[0]][(int)temp[1]] = temp[2];
            combine[(int)temp[1]][(int)temp[0]] = temp[2];
        }
        fin >> D;
        for(int i = 1;i <= D;++i)
        {
            string temp;
            fin >> temp;
            oppose[temp[0]][temp[1]] = true;
            oppose[temp[1]][temp[0]] = true;
        }
        fin >> N;
        fin >> baselist;
        solve(i);
    }
    return 0;    
}
