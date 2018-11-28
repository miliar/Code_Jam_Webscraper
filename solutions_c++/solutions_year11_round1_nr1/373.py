#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int T;
double N;
int Pd,Pg;
int cno = 0;
bool ff;
int ak;

int get(int x, int y)
{
    if(x>y) return get(y,x);
    if(x==0) return 0;
    if(y%x == 0) return x; else return get(x,y%x);
}

bool process()
{

            ak = get(Pd,100);
            //cout << ak<<endl;
            if(ak!=0 && 100/ak>N) return 0;
            if((Pd>0 && Pg == 0) ||(Pd<100 && Pg==100)) return 0;
            return 1;

}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    while(T--)
    {
        cin >> N;
        cin >> Pd >> Pg;
    //    cout << N << " " << Pd<< " "<< Pg<<endl;
        cno++;
        ff = process();
        if(ff)
        {
            cout << "Case #" << cno <<": Possible" << endl;

        }
        else
        {
            cout << "Case #" << cno <<": Broken" << endl;

        }
    }
    return 0;
}
