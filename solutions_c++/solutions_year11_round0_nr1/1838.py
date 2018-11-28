#include<fstream>
#include<algorithm>
#include<vector>
#include<math.h>

using namespace std;

ifstream cin("a.in");
ofstream cout("a.out");

struct point
{
    char R;
    int P;
};

struct new_point
{
    int P, n;
};

int solve(vector<point>& a)
{
    int res=0,i,last_pushed=-1;
    vector<new_point> O,B;
    vector<new_point>::iterator itO;
    vector<new_point>::iterator itB;
    new_point temp;
    temp.n=-1;temp.P=1;
    O.push_back(temp);
    B.push_back(temp);
    for(i=0;i<a.size();i++)
    {
        temp.n=i;temp.P=a[i].P;
        if(a[i].R=='O')
        {
            O.push_back(temp);
        }
        if(a[i].R=='B')
        {
            B.push_back(temp);
        }
    }
    itO=O.begin()+1;
    itB=B.begin()+1;
    while(!(itO==O.end()&&itB==B.end())&&last_pushed<int(a.size()-1))
    {
        if(itO->n<=last_pushed)itO++;
        if(itB->n<=last_pushed)itB++;
        if(itO->n==last_pushed+1)
        {
            res+=1+abs(itO->P-(itO-1)->P);
            if(itB->P>(itB-1)->P)
            {
                (itB-1)->P+=(1+abs(itO->P-(itO-1)->P));
                if((itB-1)->P>itB->P)(itB-1)->P=itB->P;
            }
            else
            {
                (itB-1)->P-=(1+abs(itO->P-(itO-1)->P));
                if((itB-1)->P<itB->P)(itB-1)->P=itB->P;
            }
        }
        if(itB->n==last_pushed+1)
        {
            res+=1+abs(itB->P-(itB-1)->P);
            if(itO->P>(itO-1)->P)
            {
                (itO-1)->P+=(1+abs(itB->P-(itB-1)->P));
                if((itO-1)->P>itO->P)(itO-1)->P=itO->P;
            }
            else
            {
                (itO-1)->P-=(1+abs(itB->P-(itB-1)->P));
                if((itO-1)->P<itO->P)(itO-1)->P=itO->P;
            }
        }
        last_pushed++;
    }
    return res;
}

int main()
{
    int T,I,n,i;
    vector<point> a;
    cin>>T;
    for(I=1;I<=T;I++)
    {
        cin>>n;
        a.resize(n);
        for(i=0;i<n;i++)
        {
            cin>>a[i].R>>a[i].P;
        }
        cout<<"Case #"<<I<<": "<<solve(a)<<endl;
    }
    return 0;
}
