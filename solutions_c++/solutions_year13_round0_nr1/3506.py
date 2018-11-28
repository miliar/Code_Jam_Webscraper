#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>

using namespace std;


int main() {
    int T;
    cin>>T;
    for(int caseno=1;caseno<=T;caseno++)
    {
        int board[4][4];
        char ch;
        int rowsum[4]={0,0,0,0};
        int colsum[4]={0,0,0,0};
        int diasum[2]={0,0};
        int flagdraw=0, flatincomplete=0, flagwon=0;

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>ch;
                if(ch=='X')
                {
                    rowsum[i]+=1;
                    colsum[j]+=1;
                    if(i==j) diasum[0]+=1;
                    if(i==( 3-j)) diasum[1]+=1;
                }
                else if(ch=='O')
                {
                    rowsum[i]+=10;
                    colsum[j]+=10;
                    if(i==j) diasum[0]+=10;
                    if(i==( 3-j)) diasum[1]+=10;
                }
                else if(ch=='T')
                {
                    rowsum[i]+=5;
                    colsum[j]+=5;
                    if(i==j) diasum[0]+=5;
                    if(i==( 3-j)) diasum[1]+=5;
                }
                else if(ch=='.')
                {
                    rowsum[i]+=500;
                    colsum[j]+=500;
                    if(i==j) diasum[0]+=500;
                    if(i==( 3-j)) diasum[1]+=500;

                    flatincomplete=1;           //cout<<caseno<<" flatin "<<endl;
                }
            }
            //cin>>ch;
        }

        cout<<"Case #"<<caseno<<": ";

        for(int i=0;i<4 && !flagwon;i++)
        {
            if(rowsum[i]==4 || rowsum[i]==8) {cout<<"X won"<<endl; flagwon=1;}
            else if( rowsum[i]==40 || rowsum[i]==35 ) {cout<<"O won"<<endl; flagwon=1;}
        }
        for(int i=0;i<4 && !flagwon ;i++)
        {
            if(colsum[i]==4 || colsum[i]==8) {cout<<"X won"<<endl; flagwon=1;}
            else if( colsum[i]==40 || colsum[i]==35 ) {cout<<"O won"<<endl; flagwon=1;}
        }

        if(!flagwon)
        {


        if(diasum[0]==4 || diasum[0]==8) {cout<<"X won"<<endl; flagwon=1;}
        else if(diasum[0]==40 || diasum[0]==35) {cout<<"O won"<<endl; flagwon=1;}
        }

        if(!flagwon)
        {

        if(diasum[1]==4 || diasum[1]==8) {cout<<"X won"<<endl; flagwon=1;}
        else if(diasum[1]==40 || diasum[1]==35) {cout<<"O won"<<endl; flagwon=1;}
        }


        if(!flagwon )
        {
            if(flatincomplete) cout<<"Game has not completed"<<endl;
            else cout<<"Draw"<<endl;
        }

    }
}
