#include <fstream>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

char co[26][26],ans[105];
bool op[26][26],b2[26];
int ti,ci,di,t,c,d,n,p;
string s;

inline void init()
{
    for(int i=0;i<=25;i++)
    {
        for(int j=0; j<=25;j++)
        {
            co[i][j]='a';
            op[i][j]=false;
        }
        b2[i]=false;
    }
}

int main()
{
    int i,j;
    fin>>t;
    for(ti=1;ti<=t;ti++)
    {
        init();
        fin>>c;
        for(ci=1;ci<=c;ci++) 
        { fin>>s; co[s[0]-'A'][s[1]-'A']=s[2]; co[s[1]-'A'][s[0]-'A']=s[2]; }
        fin>>d;
        for(di=1;di<=d;di++) 
        { fin>>s; op[s[0]-'A'][s[1]-'A']=true; op[s[1]-'A'][s[0]-'A']=true; b2[s[0]-'A']=true; b2[s[1]-'A']=true; }
        
        fin>>n; fin>>s; p=-1;
        for(i=0;i<n;i++)
        {
            ans[++p]=s[i];
            if(p>=1 && co[ans[p]-'A'][ans[p-1]-'A']!='a') { ans[p-1]=co[ans[p]-'A'][ans[p-1]-'A']; p--; }
            else if(b2[ans[p]-'A'])
            {
                for(j=0;j<=p;j++) if(op[ans[j]-'A'][ans[p]-'A']) { p=-1; break; }
            }
        }
        fout<<"Case #"<<ti<<": [";
        if(p!=-1)
        {
            fout<<ans[0];
            for(i=1;i<=p;i++) fout<<", "<<ans[i];
        }
        fout<<']'<<endl; 
    }
    
    return 0;
}
