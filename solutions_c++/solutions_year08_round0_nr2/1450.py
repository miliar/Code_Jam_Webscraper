#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <sstream>
using namespace std;
void run(vector<pair<int,int> > &va,vector<pair<int,int> > &vb, int &ta, int &tb, int pos, int &time, int tren)
{
    if(pos)
    {
        for(int i=0;i<va.size();i++) 
        {
            if(time<=va[i].first) 
            {
                tren=i;
                if(va.size()) {time=va[tren].second; va.erase(va.begin()+tren,va.begin()+tren+1);}
                run(va,vb,ta,tb,0,time,tren); 
                break;
            }
        }
    }
    else
    {        
        for(int i=0;i<vb.size();i++) 
        {
            if(time<=vb[i].first) 
            {
                tren=i;
                if(vb.size()) {time=vb[tren].second; vb.erase(vb.begin()+tren,vb.begin()+tren+1);}
                run(va,vb,ta,tb,1,time,tren);
                break;
            }
        }
    }
    
}
int main()
{
    int n;
    cin >> n;
    for(int z=1;z<=n;z++)
    {
        int t,na,nb,xa,xb;
        string a,b;
        cin >> t >> na >> nb;
        vector<pair<int,int> > va(na,make_pair(0,0));
        vector<pair<int,int> > vb(nb,make_pair(0,0));
        for(int i=0;i<na;i++)
        {
            cin >> a >> b;
            stringstream ss;
            ss << a[0] << a[1] << ' ' << a[3] << a[4];
            ss >> xa >> xb;
            va[i].first=60*xa+xb;
            stringstream sc;
            sc << b[0] << b[1] << ' ' << b[3] << b[4];
            sc >> xa >> xb;
            va[i].second=60*xa+xb+t;
        }
        for(int i=0;i<nb;i++)
        {
            cin >> a >> b;
            stringstream ss;
            ss << a[0] << a[1] << ' ' << a[3] << a[4];
            ss >> xa >> xb;
            vb[i].first=60*xa+xb;
            stringstream sc;
            sc << b[0] << b[1] << ' ' << b[3] << b[4];
            sc >> xa >> xb;
            vb[i].second=60*xa+xb+t;
        }
        //END READ
        sort(va.begin(),va.end());
        sort(vb.begin(),vb.end());
        int time=0,ta=0,tb=0;
        while(va.size() || vb.size())
        {
            if(!va.size()) {tb+=vb.size(); break;}
            if(!vb.size()) {ta+=va.size(); break;}
            if(va[0]<=vb[0])    //perquè A i no B???????
            {
                ta++;
                time=va[0].second;
                va.erase(va.begin(),va.begin()+1);
                run(va,vb,ta,tb,0,time,0);
            }
            else
            {
                tb++;
                time=vb[0].second;
                vb.erase(vb.begin(),vb.begin()+1);
                run(va,vb,ta,tb,1,time,0);
            }
        }
        cout << "Case #" << z << ": " << ta << " " << tb << endl;
    }
}
