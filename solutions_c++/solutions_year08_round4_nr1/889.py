#include<iostream>
#include<fstream>
using namespace std;

int n,m,margin;
bool v;
bool t[15000];
bool c[15000]; // changable

int FIND(int pos, bool value)
{
    int tmp=0;
    int sum=15000;
    bool change=false;
    
    if(pos>margin)
    {
        if(t[pos]==value)
            return 0;
        else
            return -9999;
    }
    
    for(int i=0;i<2;i++)
    {
        if(t[pos]==1) // AND
        {
            if(value==0)
            {
                tmp = FIND(2*pos,0)+FIND(2*pos+1,0)+int(change);
                if(tmp>=0&&tmp<sum)
                    sum = tmp;
                tmp = FIND(2*pos,1)+FIND(2*pos+1,0)+int(change);
                if(tmp>=0&&tmp<sum)
                    sum = tmp;
                tmp = FIND(2*pos,0)+FIND(2*pos+1,1)+int(change);
                if(tmp>=0&&tmp<sum)
                    sum = tmp;                                                        
            }
            else
            {
                tmp = FIND(2*pos,1)+FIND(2*pos+1,1)+int(change);
                if(tmp>=0&&tmp<sum)
                    sum = tmp;                
            }
        }
        else
        {
            if(value==0)
            {
                tmp = FIND(2*pos,0)+FIND(2*pos+1,0)+int(change);
                if(tmp>=0&&tmp<sum)
                    sum = tmp;                                                 
            }
            else
            {
                tmp = FIND(2*pos,0)+FIND(2*pos+1,1)+int(change);
                if(tmp>=0&&tmp<sum)
                    sum = tmp;                
                tmp = FIND(2*pos,1)+FIND(2*pos+1,0)+int(change);
                if(tmp>=0&&tmp<sum)
                    sum = tmp;
                tmp = FIND(2*pos,1)+FIND(2*pos+1,1)+int(change);
                if(tmp>=0&&tmp<sum)
                    sum = tmp;       
            }            
        }
        if(c[pos])
            t[pos] = !t[pos];
        else
            break;
        change=true;
    }
    if(sum>10000)
        sum=-9999;
    return sum;
}

int main()
{
    ifstream FIN("input.txt");
    ofstream FOUT("output.txt");
    
    FIN >> n;
    for(int Case=1;Case<=n;Case++)
    {
        int sum=0;
        FIN >> m >> v;
        margin=(m-1)/2;
        for(int i=1;i<=(m-1)/2;i++)
            FIN >> t[i] >> c[i];
        for(int i=1;i<=(m+1)/2;i++)
            FIN >> t[i+margin];
            
        sum = FIND(1,v);
        if(sum==-9999)
            FOUT << "Case #" << Case << ": IMPOSSIBLE" << endl;
        else
            FOUT << "Case #" << Case << ": " << sum << endl;
    }
}
