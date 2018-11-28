#include <fstream>
#include <vector>
#define B -1
#define O +1
using namespace std;
bool push;
bool robot(vector<int> &moves,vector<int> &event,int id,bool refresh)
{
    static int opos=1;
    static int bpos=1;
    static int epos=0;
    if(refresh==true)
    {
        opos=1;
        bpos=1;
        epos=0;
        return false;
    }
    if(epos==event.size())
    {
        return true;
    }
    if(moves.size()==0)
    return false;
    if(id==O)
    {
        if(event[epos]==opos&&push)
        {
            push=false;
            epos++;
            moves.erase(moves.begin());
        }
        else
        {
            if(moves[0]>opos)
            {
                opos++;
            }
            else if(moves[0]<opos)
            {
                opos--;
            }
        }
    }
    else
    {
        if(event[epos]==-bpos&&push)
        {
            push=false;
            epos++;
            moves.erase(moves.begin());
        }
        else
        {
            if(moves[0]>bpos)
            {
                bpos++;
            }
            else if(moves[0]<bpos)
            {
                bpos--;
            }
        }
    }
    return false;

}

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.in");
    int test;
    fin>>test;
    for(int j=1;j<=test;j++)
    {
        int n;
        fin>>n;
        vector<int> o;
        vector<int> b;
        vector<int> event;
        for(int i=0;i<n;i++)
        {
            char ch;
            int pos;
            fin>>ch>>pos;
            if(ch=='O')
            {
                o.push_back(pos);
                event.push_back(pos);
            }
            else
            {
                b.push_back(pos);
                event.push_back(-pos);
            }
        }
        long long counter=0;
        robot(o,event,O,true);
        while(true)
        {
            push=true;
            counter++;
            if(robot(o,event,O,false))
            {
                break;
            }
            if(o.size()==0&&b.size()==0)
            break;
            if(robot(b,event,B,false))
            {
                break;
            }
            if(o.size()==0&&b.size()==0)
            break;

        }
        fout<<"Case #"<<j<<": "<<counter<<endl;
    }
}
