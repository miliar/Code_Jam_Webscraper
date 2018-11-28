#include<fstream>
using namespace std;

int main()
{
    ifstream fin("c:\\codejam\\C-large.in");
    ofstream fout;
    
    fout.open("c:\\codejam\\output.txt",ios::out);
    
    int t,i,min,n,pxor,v;
    unsigned val;
    
    fin>>t;
    for(i=0;i<t;i++)
    {
        fin>>n;
        fin>>v;
        min=v;
        pxor=v;
        n--;
        val=0;
        while(n--)
        {
            fin>>v;
            pxor^=v;
            if(v<min)
            {
                val+=min;
                min=v;
            }
            else
            {
                val+=v;
            }
        }
        if(pxor==0)
            fout<<"Case #"<<i+1<<": "<<val<<endl;
        else
            fout<<"Case #"<<i+1<<": NO"<<endl;
    }
}
