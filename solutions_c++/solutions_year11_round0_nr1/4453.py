#include <iostream>
#include <vector>
#include <list>


using namespace std;


void reportarV(const list< pair<char, int> >& v)
{
    list< pair<char, int> > v2(v);
    int i=0;

    for(i=0;i<v.size();i++)
    {
        cout<<v2.front().first<<"-"<<v2.front().second<<" ";
        v2.pop_front();
    }
    cout<<endl;

}

pair <char, int> eo_a;
pair <char, int> eb_a;
int c;
list< pair<char,int> > v,vO,vB;

void sigOrange()
{
    pair <char, int> eg=v.front();
    pair <char, int> eo=vO.front();

    if(eg.first=='B')
    {
        if(eo.second > eo_a.second)
        {
            eo_a.first='M';
            eo_a.second++;
        }
        else if(eo.second < eo_a.second)
        {
            eo_a.first='M';
            eo_a.second--;
        }
        else if(eo.second == eo_a.second)
        {
            eo_a.first='S';
        }
    }

    if(eg.first=='O')
    {
        if(eo.second > eo_a.second)
        {
            eo_a.first='M';
            eo_a.second++;
        }
        else if(eo.second < eo_a.second)
        {
            eo_a.first='M';
            eo_a.second--;
        }
        else if(eo.second == eo_a.second)
        {
            eo_a.first='P';
            v.pop_front();
            vO.pop_front();
        }
    }
}

void sigBlue()
{
    pair <char, int> eg=v.front();
    pair <char, int> eb=vB.front();

    if(eg.first=='O')
    {
        if(eb.second > eb_a.second)
        {
            eb_a.first='M';
            eb_a.second++;
        }
        else if(eb.second < eb_a.second)
        {
            eb_a.first='M';
            eb_a.second--;
        }
        else if(eb.second == eb_a.second)
            eb_a.first='S';
    }

    if(eg.first=='B')
    {
        if(eg.second > eb_a.second)
        {
            eb_a.first='M';
            eb_a.second++;
        }
        else if(eg.second < eb_a.second)
        {
            eb_a.first='M';
            eb_a.second--;
        }
        else if(eg.second == eb_a.second)
        {
            eb_a.first='P';
            v.pop_front();
            vB.pop_front();
        }
    }
}

void sigEstado()
{
    pair <char, int> eg=v.front();

    if(eg.first=='O')
    {
        sigBlue();
        sigOrange();
    }
    else
    {
        sigOrange();
        sigBlue();
    }
    c++;
}

int resolver()
{
    c=0;
    eo_a.first='S';
    eo_a.second=1;
    eb_a.first='S';
    eb_a.second=1;
    while(!v.empty())
        sigEstado();
    return c;
}

int main()
{
    int nc,i=0,j=0,n,resp;
    pair <char, int> par;

    cin>>nc;
    for(i=0;i<nc;i++)
    {
        cin>>n;
        v.clear();
        vO.clear();
        vB.clear();
        for(j=0;j<n;j++)
        {
            cin>>par.first;
            cin>>par.second;
            v.push_back(par);

            if(par.first == 'O')
                vO.push_back(par);
            if(par.first == 'B')
                vB.push_back(par);
        }
        resp=resolver();
        cout<<"Case #"<<(i+1)<<": "<<resp<<endl;
    }
    return 0;
}
