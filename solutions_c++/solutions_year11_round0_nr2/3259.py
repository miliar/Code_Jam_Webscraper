#include<iostream>
#include<vector>
#include<cmath>

using namespace std;


struct comb
{
    char e1;
    char e2;
    char res;
    
    comb()
    {
        e1 = ' ';
        e2 = ' ';
        res = ' ';
    }
    
    comb(char el1, char el2, char res1)
    {
        e1 = el1;
        e2 = el2;
        res = res1;
    }
    
    comb(char el1, char el2)
    {
        e1 = el1;
        e2 = el2;
        res = ' ';
    }
};

int main()
{

    int t, cont = 1;
    cin>>t;
    while(t--)
    {
        long long c;
        cin>>c;
        vector<comb> vec;
        for(long long i=0;i<c;++i)
        {
            char e1, e2, r;
            cin>>e1>>e2>>r;
            vec.push_back(comb(e1,e2,r));
        }
        
        long long op;
        cin>>op;
        vector<comb> vec2;
        for(long long i=0;i<op;++i)
        {
            char e1, e2;
            cin>>e1>>e2;
            vec2.push_back(comb(e1,e2));
        }
        long long tam;
        cin>>tam;
        string invoks, resp = "";
        //cin>>invoks;
        long long pos = 0;
        for(long long i=0;i<tam;++i)
        {
            char in;
            cin>>in;
            invoks += in;
            if(pos == 0)
            {
                resp = in;
                pos = 1;
            }
            else
            {
                bool band = false;
                for(long long j=0;j<c;++j)
                    if(resp[pos-1] == vec[j].e1 && in == vec[j].e2 || resp[pos-1] == vec[j].e2 && in == vec[j].e1)
                    {
                        resp[pos-1] = vec[j].res;
                        band = true;
                        break;
                    }
                if(!band)
                {
                    for(long long j=0;j<op;++j)
                        if(in == vec2[j].e1 || in == vec2[j].e2)
                        {
                            char sr;
                            if(in == vec2[j].e1)
                                sr = vec2[j].e2;
                            else
                                sr = vec2[j].e1;
                            string::size_type loc = resp.find( sr, 0 );
                            if( loc != string::npos) 
                            {
                                resp = "";
                                pos = 0;
                                band = true;
                                break;
                            }
                        }
                    if(!band)
                    {
                        resp += in;
                        pos++;
                    }
                }
            }
        }
        
        
        
        cout<<"Case #"<<cont<<": [";
        long long tam2 = resp.length();
        for(long long i=0;i<tam2;++i)
        {
            if(i!=0)
                cout<<", ";
            cout<<resp[i];
        }
        cout<<"]"<<endl;
        ++cont;
    }
    return 0;
}
