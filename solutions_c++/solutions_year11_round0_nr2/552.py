#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
using namespace std;

int code(char C)
{
    return C-'A';
}
char decode(int C)
{

    return 'A'+C;
}

int combo[38][38];
vector<int> oppose[38];
int contains[38];
int ans[1111];
int anslen;

void clear()
{
    int i;
    for(i=0;i<38;i++) contains[i]=false;
    anslen=0;
}
void reset()
{
    int i,j;
    for(i=0;i<38;i++)
    {
        oppose[i].clear();
        for(j=0;j<38;j++)
        {
            combo[i][j]=-1;
        }
    }
    clear();
}

void add(int x)
{
    contains[x]++;
    ans[anslen]=x;
    anslen++;
}
void pop()
{
    int x=ans[anslen-1];
    contains[x]--;
    anslen--;
}
bool checkCombo()
{
    if(anslen<2) return false;
    if(combo[ans[anslen-2]][ans[anslen-1]]!=-1)
    {
        int x=combo[ans[anslen-2]][ans[anslen-1]];
        pop();
        pop();
        add(x);
        checkCombo();
        return true;
    }
    else return false;
}
void join(int x)
{
    add(x);
    if(checkCombo()) return;
    int i,I=oppose[x].size();
    for(i=0;i<I;i++)
        if(contains[oppose[x][i]])
        {
            clear();
            return;
        }

}
void test()
{

    reset();
    int C,D,i,x,y,z,N;
    string S;
    cin>>C;
    for(i=0;i<C;i++)
    {
        cin>>S;
        x=code(S[0]);
        y=code(S[1]);
        z=code(S[2]);
        combo[x][y]=combo[y][x]=z;
    }
    cin>>D;
    for(i=0;i<D;i++)
    {
        cin>>S;
        x=code(S[0]);
        y=code(S[1]);
        oppose[x].push_back(y);
        oppose[y].push_back(x);
    }
    cin>>N>>S;
    for(i=0;i<N;i++)
    {
        x=code(S[i]);
        join(x);
    }

    cout<<"[";
    for(i=0;i<anslen;i++)
    {
        if(i) cout<<", ";
        cout<<decode(ans[i]);
    }
    cout<<"]";

}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,T;
    cin>>T;
    for(i=0;i<T;i++)
    {
      cout<<"Case #"<<i+1<<": ";
      test();
      cout<<endl;
    }
    return 0;
}
