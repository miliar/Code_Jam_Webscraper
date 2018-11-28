#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

bool check(int N, int Pn, int Pg)
{
    if((Pg==100&&Pn!=100)||(Pg==0&&Pn!=0))return false;
    int i;
    for(i=1;i<=N;i++)
    {
        if(double(i*Pn)/100.==i*Pn/100)
            return true;
    }
    return false;
}

int main()
{
    int I,T,N,Pn,Pg;
    cin>>T;
    for(I=1;I<=T;I++)
    {
        cin>>N>>Pn>>Pg;
        cout<<"Case #"<<I<<": ";
        if(check(N,Pn,Pg))cout<<"Possible";
        else cout<<"Broken";
        cout<<endl;
    }
}
