#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

ifstream fin("input.txt");
#define cin fin

ofstream fout("output.txt");
#define cout fout

//triplets 3adeyeen
int t[31][3];
//surprising triplets :)
int s[31][3];

void init()
{
    int i, j;
    
    int tt[3] = {0, 0, 0};
    int ss[3] = {-1, 0, 1};
    
    for(i=0; i<31; i++)
    {
        if(i && !(i % 3))
        {
            tt[2] = tt[1] = ++tt[0];
            ss[1]++;
        }
        if(i % 3 == 1)
        {
            tt[2]++;
            ss[1]++;
        }
        if(i % 3 == 2)
        {
            tt[1]++;
            ss[2] = ss[1] = ++ss[0];
            ss[2] += 2;
        }
        
        for(j=0; j<3; j++)
        {
            t[i][j] = tt[j];
            s[i][j] = ss[j];
        }
        
        //cout<<i<<"\t"<<t[i][0]<<" "<<t[i][1]<<" "<<t[i][2]<<"\t"<<s[i][0]<<" "<<s[i][1]<<" "<<s[i][2]<<endl;
        
        s[0][2] = s[0][1] = s[0][0] = 0;
        s[1][2] = s[1][1] = s[1][0] = 0;
        s[1][2] = 1;
        
        s[30][2] = s[30][1] = s[30][0] = 10;
        s[29][2] = s[29][1] = s[29][0] = 10;
        s[29][0] = 9;
    }
}

int main()
{
    init();
    int i, j, c;
    cin>>c;
    for(i=0; i<c; i++)
    {
        //n = 3adad el nas
        //m = kam wa7ed surprising
        //p = el score elly ha7seb kam wa7ed gab a3la menno
        //v = scorat el nas
        int n, m, p;
        vector<int> v;
        cin>>n>>m>>p;
        
        v.resize(n);
        for(j=0; j<n; j++)
        {
            cin>>v[j];
        }
        
        sort(v.rbegin(), v.rend());
        
        int ret = 0;
        
        for(j=0; j<n; j++)
        {
            if(p <= t[v[j]][2])
            {
                ret++;
            }
            else if(p <= s[v[j]][2])
            {
                if(m)
                {
                    ret++;
                    m--;
                }
            }
        }
        cout<<"Case #"<<i + 1<<": "<<ret<<endl;
    }
    return 0;
}
