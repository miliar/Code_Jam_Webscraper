#include <iostream>

using namespace std;

int abs(int x)
{
    if (x<0) {return -x;} else {return x;}
}

int main()
{
    char c;
    int n,m,id;

    int acc,sum;
    int O,B;
    char act;

    cin >> n;

    for (int i=0; i<n;++i )
    {
        cin >> m;
        acc=0; sum=0;
        O=1; B=1;
        act='S';
        int spa;
        for (int j=0; j<m; ++j)
        {
            cin >> c >> id;
            spa=id;
            if (c!=act)
             {
                act=c;
                 if (c=='O') { id=abs(id-O); O=spa;}
                 if (c=='B') { id=abs(id-B); B=spa;}
                 //if (c=='S') {id=abs(id-1);}
                 id=id-acc;
                 if (id>0) {sum=id+sum+1; acc=id+1;} else {acc=1; sum++;}
            }
             else
             {
                 if (c=='O') { id=abs(id-O); O=spa;}
                 if (c=='B') { id=abs(id-B); B=spa;}
                 acc=id+acc+1;
                 sum=id+sum+1;
             }
        }
        cout << "Case #" <<i+1 <<": " << sum <<endl;
    }
    return 0;
}
