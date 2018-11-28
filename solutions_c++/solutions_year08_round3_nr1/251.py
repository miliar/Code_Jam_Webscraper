#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int n,p,k,l;
long long freq[2000];

int main()
{
    ifstream FIN("input.txt");
    ofstream FOUT("output.txt");
    
    FIN >> n;
    for(int Case=1;Case<=n;Case++)
    {
        FIN >> p >> k >> l;
        for(int i=0;i<l;i++)
        {
            FIN >> freq[i];
        }
        sort(freq,freq+l);
        int level=1;
        int left=k;
        bool possible=true;
        long long sum=0;
        for(int i=l-1;i>=0;i--)
        {
            sum+=level*freq[i];
            left--;
            if(left==0)
            {
                level++;
                left=k;
                if(level>p&&i!=0)
                {
                    possible=false;
                    break;
                }
            }
        }
        if(possible)
            FOUT << "Case #" << Case << ": " << sum << endl;
        else
            FOUT << "Case #" << Case << ": Impossible" << endl;
    }
}
