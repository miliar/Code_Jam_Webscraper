#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    long a,b,c,d,e,f,g,h,v,x,t;
    string s[4], s2;
    vector<string> vec;
    vector<string>::iterator i;

    cin>>t;
    while(t>0)
    {
        for(b=0; b<4; b++)
        {
            cin>>s[b];
        }

        d=0;
        if((s[0].at(0)=='X' || s[0].at(0)=='T') && (s[1].at(1)=='X' || s[1].at(1)=='T') && (s[2].at(2)=='X' || s[2].at(2)=='T') && (s[3].at(3)=='X' || s[3].at(3)=='T')){d++;}
        else
        {
        if((s[0].at(3)=='X' || s[0].at(3)=='T') && (s[1].at(2)=='X' || s[1].at(2)=='T') && (s[2].at(1)=='X' || s[2].at(1)=='T') && (s[3].at(0)=='X' || s[3].at(0)=='T')){d++;}
        else
        {
        for(b=0; b<4; b++)
        {
            if(s[b]=="XXXX" || s[b]=="TXXX" || s[b]=="XTXX" || s[b]=="XXTX" || s[b]=="XXXT"){d++; break;}
            else
            {
                if((s[0].at(b)=='X' || s[0].at(b)=='T') && (s[1].at(b)=='X' || s[1].at(b)=='T') && (s[2].at(b)=='X' || s[2].at(b)=='T') && (s[3].at(b)=='X' || s[3].at(b)=='T')){d++; break;}
            }
        }
        }
        }

        if(d>0){vec.push_back("X won");}
        else
        {

        e=0;
        if((s[0].at(0)=='O' || s[0].at(0)=='T') && (s[1].at(1)=='O' || s[1].at(1)=='T') && (s[2].at(2)=='O' || s[2].at(2)=='T') && (s[3].at(3)=='O' || s[3].at(3)=='T')){e++;}
        else
        {
         if((s[0].at(3)=='O' || s[0].at(3)=='T') && (s[1].at(2)=='O' || s[1].at(2)=='T') && (s[2].at(1)=='O' || s[2].at(1)=='T') && (s[3].at(0)=='O' || s[3].at(0)=='T')){e++;}
        else
        {
        for(b=0; b<4; b++)
        {
            if(s[b]=="OOOO" || s[b]=="TOOO" || s[b]=="OTOO" || s[b]=="OOTO" || s[b]=="OOOT"){e++; break;}
            else
            {
                if((s[0].at(b)=='O' || s[0].at(b)=='T') && (s[1].at(b)=='O' || s[1].at(b)=='T') && (s[2].at(b)=='O' || s[2].at(b)=='T') && (s[3].at(b)=='O' || s[3].at(b)=='T')){e++; break;}
            }
        }
        }
        }
        if(e>0){vec.push_back("O won");}
        else
        {
            for(b=0, f=0; b<4; b++)
            {
                if((s[0].at(b)=='.') || (s[1].at(b)=='.') || (s[2].at(b)=='.') || (s[3].at(b)=='.')){f++; break;}
            }
            if(f>0){vec.push_back("Game has not completed");}
            else{vec.push_back("Draw");}
        }

        }



        t--;
    }

        for(b=1, i=vec.begin(); i!=vec.end(); i++, b++)
        {
            cout<<"Case #"<<b<<": "<<*i<<endl;
        }

    return 0;
}
