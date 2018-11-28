#include<iostream>
#include<fstream>
#include<sstream>

using namespace std;
int main()
{
    int t;
        double n, s, p, a, count;
        ifstream infile;
        infile.open("qustn.in");

        infile>>t;
        ofstream myfile("results.txt");
        for(int j=1;j<t+1;j++)
        {
                count=0;
                infile>>n>>s>>p;
                for(int i=0;i<n;i++)
                {
                        infile>>a;
                        if(a<p)
                        {}
                        else if((a-p)/2 >= p-1)
                        {
                                count++;
                        }
                        else if((a-p)/2 >= p-2 && s>0)
                        {
                                count++;
                                s--;
                        }
                }
                
                
                myfile<<"Case #"<<j<<": "<<count<<"\n";
                cout<<"Case #"<<j<<": "<<count<<endl;
        }
        return 0;
}
