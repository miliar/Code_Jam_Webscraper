#include <iostream>
#include <fstream>
using namespace std;

int T,R,N,k;
int Group[1500];
int ans;

int main()
{
    ifstream fin("Csmall.in");
    ofstream fou("Csmall.out");
    fin>>T;
    //cin>>T;
    for (int t=1;t<=T;t++)
    {
        //input part
        //cin>>R>>k>>N;
        fin>>R>>k>>N;
        for (int i=1;i<=N;i++)
        {
            //cin>>Group[i];
            fin>>Group[i];
        }
        ans = 0;
        int ptr;
        ptr = 1;
        for (int r=1;r<=R;r++)
        {
            int pk,tptr;
            tptr =ptr;
            pk = 0;
            while (pk<=k)
            {
                if (Group[ptr]+pk<=k) {pk=pk+Group[ptr];ptr++;if (ptr>N)ptr=1;}
                else break;
                if (tptr==ptr) break;
            }
            ans = ans + pk;
        }
//        cout<<"Case #"<<t<<": "<<ans<<endl;
fou<<"Case #"<<t<<": "<<ans<<endl;
        }
        fou.close();
        fin.close();
    return 0;
    }
