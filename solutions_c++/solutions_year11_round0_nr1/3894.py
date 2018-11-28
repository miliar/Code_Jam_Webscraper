#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <fstream>

using namespace std;

int p(vector<int> blue,vector<int> orange,vector<char> seq)
{
    int time;
    int res=0;
    int b_pos,o_pos;
    b_pos=o_pos=1;
    int b_b,o_b;
    b_b=o_b=0;
    
    for(int t=0;t<seq.size();t++)
    {
        if(seq[t]=='B')
        {
            time=abs( b_pos - blue[b_b] )+1;
            res+=time;
            
            if(b_pos-blue[b_b]<=0) b_pos+= abs(b_pos-blue[b_b]);
            else b_pos-=abs(b_pos-blue[b_b]);
           
            b_b++;
            
            if(o_pos-orange[o_b]<=0) o_pos+= min(time, abs(o_pos-orange[o_b]) );
            else o_pos-= min(time, abs(o_pos-orange[o_b]) );
            
        }
        else
        {
            
            time=abs( o_pos - orange[o_b] )+1;
            res+=time;
           
            if(o_pos-orange[o_b]<=0) o_pos+= abs(o_pos-orange[o_b]);
            else o_pos-= abs(o_pos-orange[o_b]);
            
            o_b++;
            
            if(b_pos-blue[b_b]<=0) b_pos+= min(time, abs(b_pos-blue[b_b]) );
            else b_pos-= min(time, abs(b_pos-blue[b_b]) );
        }
        
    }
    
    return res;
}

int main()
{
    ifstream in("A-large.in");
    ofstream out("A-small-attempt0.out");
    int c,q,w;
    char ch;
    
    in>>c;
    int t,tt;
    
    vector<int> res;
    
    for(t=0;t<c;t++)
    {
        vector<int> o;
        vector<int> b;
        vector<char> seq;
        
        in>>q;
        
        for(tt=0;tt<q;tt++)
        {
            in>>ch;
            in>>w;
            if(ch=='O') {o.push_back(w);seq.push_back('O');}
            if(ch=='B') {b.push_back(w);seq.push_back('B');}
        }
        
       res.push_back( p(b,o,seq) );
    }
    
    for(t=0;t<res.size();t++)
    {
        out<<"Case #"<<t+1<<": "<<res[t]<<endl;
    }
    
  //  system("PAUSE");
}
