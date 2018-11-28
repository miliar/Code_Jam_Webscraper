#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile("in.txt");
    ofstream outfile("output.txt");
    int t,r,k,n;
    int data[1000];
    int sum[1000];
    int num[1000];
    infile>>t;
    for (int i=0;i<t;++i)
    {
        infile>>r>>k>>n;
        int total=0;
        long long result=0;
        for (int j=0;j<n;++j)
        {
            infile>>data[j];
            total+=data[j];
        }
        if (total<=k)
        {
            result=total*r;
        }
        else
        {
            for (int j=0;j<n;++j)
            {
                int jj=j;
                int sumPeople=0;
                int numPeople=0;
                do 
                {
                    sumPeople+=data[jj];
                    ++numPeople;
                    ++jj;
                    jj=jj%n;
                } while (sumPeople+data[jj]<=k);
                sum[j]=sumPeople;
                num[j]=numPeople;
            }
            int begin=0;
            int number=0;
            while (number<r)
            {
                result=result+sum[begin];
                begin+=num[begin];
                begin=begin % n;
                ++number;
            }
        }
        outfile<<"Case #"<<i+1<<": "<<result<<endl;
    }
    infile.close();
    outfile.close();
    return 0;
}