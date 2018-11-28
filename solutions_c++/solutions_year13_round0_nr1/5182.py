#include <iostream>
#include <vector>
#include <cstdio>
#define FOR(i,a)    for(int i = 0;i<a;i++)
#include <string>

using namespace std;

int main(){
    freopen("ip.txt","r",stdin);
    freopen("op.txt","w",stdout);
    int t;
    int caseno = 1;
    cin>>t;
    FOR(i,t){
        vector<string>v(4);
        cin>>v[0]>>v[1]>>v[2]>>v[3];
        cout<<"Case #"<<caseno<<": ";
        int x = 0,o = 0;
        int g = 0;
        int x3 = 0,y3 = 0,t3 = 0,t4 = 0,y4 = 0,x4 = 0;
        FOR(j,4){
            int x1 = 0,y1 = 0,t1 = 0,x2 = 0,y2 = 0,t2 = 0;
            FOR(k,4){
                if(v[j][k] == '.')  g = 1;
                if(v[j][k] == 'X')  x1++;
                else if(v[j][k] == 'O')  y1++;
                else if(v[j][k] == 'T') t1++;
                if(v[k][j] == 'X')  x2++;
                else if(v[k][j] == 'O')  y2++;
                else if(v[k][j] == 'T') t2++;
                if(k == j){
                    if(v[j][k] == 'X')  x3++;
                    else if(v[j][k] == 'O')  y3++;
                    else if(v[j][k] == 'T') t3++;
                }
                if(k + j == 3){
                    if(v[j][k] == 'X')  x4++;
                    else if(v[j][k] == 'O')  y4++;
                    else if(v[j][k] == 'T') t4++;
                }
            }
            if(x1 + t1 == 4) x++;
            if(y1 + t1 == 4) o++;
            if(x2 + t2 == 4) x++;
            if(y2 + t2 == 4) o++;
        }
        if(x3 + t3 == 4) x++;
        if(y3 + t3 == 4) o++;
        if(x4 + t4 == 4) x++;
        if(y4 + t4 == 4) o++;
        if(x == o){
            if(g)   cout<<"Game has not completed";
            else    cout<<"Draw";

        }
        else if(x > o){
            cout<<"X won";
        }
        else    cout<<"O won";
        cout<<"\n";
        caseno++;
    }
    return 0;
}
