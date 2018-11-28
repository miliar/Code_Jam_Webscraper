#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <complex>
#include <list>
#include <functional>
#include <utility>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;

#define READ freopen("input.txt", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)
#define PI acos(-1)
#define F(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define C cout<<
#define E <<endl

typedef vector<int> vi;

template <class T> inline bool isPwr2(T x){return (x != 0) && ((x & (x - 1)) == 0);}
template <class T> inline double D2R(T x){return (PI*x)/180;}

int main()
{
    READ;
    WRITE;
    int N,tc=1;
    cin>>N;

    while(N--)
    {
        string str[5];

        //if(N!=0)
        F(i,0,3) cin>>str[i];
        //else
        //F(i,0,3) cin>>str[i];

//
//        for(int i=0;i<=3;i++)
//        {
//            for(int j=0;j<=3;j++)
//            cout<<str[i][j];
//
//            cout<<endl;
//        }

        bool stop = false,incm=false;

        for(int i=0;i<=3;i++)
        {
            int cnt_o=0,cnt_x=0;
            int t = 0;
            for(int j=0;j<=3;j++)
            {
                if(cnt_x >=1 && cnt_o >=1) break;

                if(str[i][j]=='O') cnt_o++;
                else if(str[i][j]=='X') cnt_x++;
                else if(str[i][j]=='T') t = 1;
                //else if(str[i][j]=='.') {incomplete = true;break;}
            }

            if(cnt_o+t==4 && cnt_x==0) {cout<<"Case #"<<tc++<<": O won"<<endl;stop=true;break;}
            if(cnt_x+t==4 && cnt_o==0) {cout<<"Case #"<<tc++<<": X won"<<endl;stop=true;break;}

            //if(incomplete) break;
        }

        if(stop) continue;

        for(int j=0;j<=3;j++)
        {
            int cnt_o=0,cnt_x=0;
            int t = 0;
            for(int i=0;i<=3;i++)
            {
                if(cnt_x >=1 && cnt_o >=1) break;

                if(str[i][j]=='O') cnt_o++;
                else if(str[i][j]=='X') cnt_x++;
                else if(str[i][j]=='T') t = 1;
                //else if(str[i][j]=='.') {incomplete = true;break;}
            }

            if(cnt_o+t==4 && cnt_x==0) {cout<<"Case #"<<tc++<<": O won"<<endl;stop=true;break;}
            if(cnt_x+t==4 && cnt_o==0) {cout<<"Case #"<<tc++<<": X won"<<endl;stop=true;break;}
        }

        if(stop) continue;

        int cnt_o=0,cnt_x=0;
        int t = 0;


        for(int i=0;i<=3;i++)
        {
            if(cnt_x >=1 && cnt_o >=1) break;

            if(str[i][i]=='O') cnt_o++;
            else if(str[i][i]=='X') cnt_x++;
            else if(str[i][i]=='T') t = 1;

        }

        if(cnt_o+t==4 && cnt_x==0) {cout<<"Case #"<<tc++<<": O won"<<endl;stop=true;}
        if(cnt_x+t==4 && cnt_o==0) {cout<<"Case #"<<tc++<<": X won"<<endl;stop=true;}

        if(stop) continue;

        cnt_o=0,cnt_x=0;
        t = 0;

        for(int i=0,j=3;i<=3&&j>=0;i++,j--)
        {
            if(cnt_x >=1 && cnt_o >=1) break;

            if(str[i][j]=='O') cnt_o++;
            else if(str[i][j]=='X') cnt_x++;
            else if(str[i][j]=='T') t = 1;


        }

        if(cnt_o+t==4 && cnt_x==0) {cout<<"Case #"<<tc++<<": O won"<<endl;stop=true;}
        if(cnt_x+t==4 && cnt_o==0) {cout<<"Case #"<<tc++<<": X won"<<endl;stop=true;}

        if(stop) continue;

        for(int i=0;i<=3;i++)
        {
            for(int j=0;j<=3;j++)
            if(str[i][j]=='.'){incm=true;break;}

            if(incm) break;
        }

        if(incm) {cout<<"Case #"<<tc++<<": Game has not completed"<<endl;continue;}
        else {cout<<"Case #"<<tc++<<": Draw"<<endl;continue;}




        //if(incomplete) cout<<""<<endl;


    }




    return 0;
}
