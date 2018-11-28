#include<iostream>
#include <string>
#include <vector>

#define dout if(0) cout

using namespace std;

char nonbase[26][26];
bool oppose[26][26];

void init()
{
    for(int i=0;i<26;++i)
        for(int j=0; j<26;++j)
        {
            nonbase[i][j]='$';
            oppose[i][j]=false;
        }
}

void init_display()
{
    for(int i=0;i<26;++i)
    {
        cout << endl;
        for(int j=0; j<26;++j)
        {
            cout << nonbase[i][j] << "," << oppose[i][j] << " ";
        }
    }
    cout << endl;
}
    
int idx(char c)
{
    return c-'A';
}

void Create(string&);

int main()
{

    int T;
    cin >>T;
    dout << T << endl;
    for(int t=1; t<=T; ++t)
    {
        init();
        
        int C; cin >>C;
        dout << "-----------------------" << endl;
        dout << C << endl;
        string nb_str;
        for(int c=0; c<C; ++c)
        {
            cin >> nb_str;

            int i = idx(nb_str[0]);
            int j = idx(nb_str[1]);
            nonbase[i][j] = nb_str[2];
            nonbase[j][i] = nb_str[2];
        }

        int D; cin >>D;
        dout << D << endl;
        string op_str;
        for(int d=0; d<D; ++d)
        {
            cin >> op_str;
            int i = idx(op_str[0]);
            int j = idx(op_str[1]);
            oppose[i][j] = true;
            oppose[j][i] = true;
        }

//        init_display();

        int N; cin >> N;
        string str; cin >> str;
        dout << str << endl;

        cout << "Case #" << t << ": [";
        Create(str);
        cout << "]" << endl;

    }

}

void display(vector<char>&);

void Create(string &str)
{
    vector<char> res;
    for(int i=0; i<str.length(); ++i)
    {
        if(res.size() < 1)
        {
            res.push_back(str[i]);
            continue;
        }

        int x = idx(str[i]);
        
        //nonbase
        int y = idx(res.back());
        if(nonbase[x][y] != '$')
        {
            res.pop_back();
            res.push_back(nonbase[x][y]);
            continue;
        }

        res.push_back(str[i]);

        //clear
        for(int j=0; j<res.size()-1; ++j)
        {
            int y = idx(res[j]);
            if(oppose[x][y])
            {
                res.clear();
                break;
            }
        }
/*        cout << i << " ";
        display(res);
        cout << endl;
*/
    }
    display(res);
}

void display(vector<char> &res)
{
    if(res.size() > 0)
    {
        for(int j=0; j<res.size()-1; ++j)
        {
            cout << res[j] << ", ";
        }
        cout << res.back();
    }        
}
