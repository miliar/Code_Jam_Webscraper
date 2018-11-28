#include<iostream>
#include<fstream>
using namespace std;
main()
{
    int t,cases=0;
    char ch;
    ifstream in;
    ofstream out;
    out.open("out_b.txt");
    in.open("in_b.txt");
    in>>t;
    while(t--)
    {
        cases++;
        int count=0,n,s,p,i,ti;
        in>>n>>s>>p;
        int temp=p*3;
        for(i=0; i<n; i++)
        {

            in>>ti;
            if(ti)
            {
                if(ti>=temp-2)
                    count++;
                else if(ti<temp-4)
                    continue;
                else
                {
                    if(s)
                    {
                        count++;
                        s--;
                    }
                }
            }

        }
        if(temp==0)
        out<<"Case #"<<cases<<": "<<n<<endl;
        else
        out<<"Case #"<<cases<<": "<<count<<endl;
    }
    in.close();
    out.close();

}
