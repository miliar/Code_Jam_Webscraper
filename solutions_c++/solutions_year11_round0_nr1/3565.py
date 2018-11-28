#include<fstream>
using namespace std;

int main()
{
    ifstream fin("c:\\codejam\\A-large.in");
    ofstream fout;
    
    fout.open("c:\\codejam\\output.txt",ios::out);
    
    int t,n,v,i;
    int o,b,po,pb;
    char c;
    fin>>t;
    for(i=0;i<t;i++)
    {
        fin>>n;
        o=b=0;
        po=pb=1;
        while(n--)
        {
            fin>>c>>v;
            if(c=='O')
            {
                o+= abs(v-po);
                if(o<b)
                    o=b;
                po=v;
                o++;
            }
            else
            {
                b+= abs(v-pb);
                if(o>b)
                    b=o;
                pb=v;
                b++;
            }
        }
        fout<<"Case #"<<i+1<<": "<<(o>b?o:b)<<endl;
    }
    fout.close();
}
