#include<fstream>
using namespace std;
main()
{
    ifstream in("a.in");
    ofstream out("a.txt");
    int n,k,test;
    in>>test;
    for(int t1=1;t1<=test;t1++)
    {
        in>>n>>k;
        int t=1,i;
        for(i=0;i<n;i++)t*=2;
        out<<"Case "<<'#'<<t1<<": ";
        if(k+1<t)out<<"OFF"<<endl;
        else if(k%t==t-1)out<<"ON"<<endl;else out<<"OFF"<<endl;
    }    
}    
