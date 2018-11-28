#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>

#define all(v) (v).begin(), (v).end()

using namespace std;

int N, M;
vector <string> v;

bool match(string word, string pattern, string L, int p)
{
    if(word.size() != pattern.size()) return false;
    
    for(int i=0; i<word.size(); i++)
    {
        if(pattern[i]!='_' && pattern[i]!=word[i])
            return false;
    
        if(pattern[i]=='_')
        {
            for(int j=0; j<p; j++)
                if(word[i]==L[j])
                    return false;
        }
    } 
    
    return true;
}

void doit()
{
    string L;
    cin>>L;
    
    int maxP = -1, ind = -1;
    for(int i=0; i<v.size(); i++) // diccionario
    {
        int P = 0;
        
        string pattern = string((int)v[i].size(), '_');
        
        bool puede[N];
        for(int j=0; j<N; j++)
            puede[j] = 1;
        
        for(int j=0; j<L.size(); j++)
        {
            bool posible[26];
            memset(posible, 0, sizeof(posible));
            
            int nMatch = 0;
            for(int k=0; k<v.size(); k++)
            {
                if(match(v[k], pattern, L, j) && puede[k])
                {
                    nMatch++;
                    for(int w=0; w<v[k].size(); w++)
                        if(pattern[w]=='_') posible[v[k][w]-'a'] = 1;
                }
            }
            
            if(nMatch == 0) cout<<"ERROR";
            else if(nMatch == 1) break;
            else if (posible[L[j]-'a'])
            {
                bool ok = 0;
                for(int k=0; k<v[i].size(); k++)
                {
                    if(v[i][k]==L[j])
                    {
                        ok = 1;
                        pattern[k] = L[j];
                    }
                }
                if(!ok)
                {
                    P++;
                    
                    for(int k=0; k<v.size(); k++)
                    {
                        if(puede[k])
                        {
                            for(int w=0; w<v[k].size(); w++)
                            {
                                if(v[k][w]==L[j])
                                {
                                    puede[k]=0;
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }
        
        if(P > maxP)
        {
            maxP = P;
            ind = i;
        }
    }
    cout<<" "<<v[ind];
}

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    cin>>T;
    
    for(int caso=1; caso<=T; caso++)
    {
        cout<<"Case #"<<caso<<":";
        
        v.clear();
        
        cin>>N>>M;
        
        for(int i=0; i<N; i++)
        {
            string s;
            cin>>s;
            v.push_back(s);
        }
        
        for(int i=0; i<M; i++) // listas
            doit();

        cout<<endl;
    }
    
    return 0;
}
