#include <iostream>
#include <string>
#include <fstream>
using namespace std;

/*



*/

int n;
int m[1001];
bool xored[1001] = {0};
int seanMax = 0;
int oPile = 0;

void dfs(int upto)
{
    if( upto==n )
    {
        int txor = 0;
        int seanPile = 0;
        for(int i=0; i<n; i++)
        {
            if( !xored[i] )
            {
                seanPile += m[i];
                txor ^= m[i];
            }
        }

        //cout<<seanPile<<' '<<txor<<' '<<oPile<<endl;
        if( txor==oPile && txor!=0 )
        {
            if( seanMax < seanPile )
            {
                seanMax = seanPile;
                //cout<<"WIN!!!\n";
            }
        }
        return;
    }
    oPile ^= m[upto];
    xored[upto] = 1;
    dfs(upto+1);
    oPile ^= m[upto];
    xored[upto] = 0;
    dfs(upto+1);
}


int main()
{
    ifstream a("accc.in");
    ofstream b("bccc.out");
    #define cin a
    #define cout b
    int t;
    cin>>t;
    for(int tt=0; tt<t; tt++)
    {

        cin>>n;
//cout<<n<<endl;

        for(int i=0; i<n; i++)
        {
            cin>>m[i];
        }

        oPile = 0;
        seanMax = 0;
        dfs(0);



        if(seanMax) cout<<"Case #"<<tt+1<<": "<<seanMax<<endl;
        else cout<<"Case #"<<tt+1<<": NO"<<endl;
    }
}
