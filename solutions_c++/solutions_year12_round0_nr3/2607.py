#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <set>

using namespace std;

int main()
{
    string in("C-large.in");
    ifstream infile;
    infile.open(in.c_str(), ifstream::in);
    
    size_t found = in.find_last_of(".in");
    string out = in.replace(found-1, 2, "out");    
    ofstream outfile;
    outfile.open(out.c_str(), ofstream::out);
    
    int t = 0;
    infile >> t;
    //cout << t << endl;
    
    int a = 0;
    int b = 0;
    int cnt = 0;
    
    for (int i = 1; i < t+1; i++)
    {
        cnt = 0;
        
        infile >> a;
        infile >> b;
        //cout << a << "\t" << b << "\t";
        
        int tmp = a;
        int j = 0;
        while (tmp > 0)
        {
              tmp = tmp / 10;
              j++;              
        }        
        //cout << j << "\t";

        for (int n = a; n < b; n++)
        {
            set<int> mset;
            for (int k = 1; k < j; k++)
            {
                int tail = n % (int)floor(pow(10,k));
                int front = n / (int)floor(pow(10,k));
                int m = tail * (int)floor(pow(10,j-k)) + front;
                if (m > n && m <= b)
                {
                   //cout << "(" << a1 << " " << a2 << ")\t";
                   //outfile << "(" << a1 << " " << a2 << ")\t";
                   mset.insert(m);
                }
            }
            cnt += mset.size();
        }
        //cout << cnt << endl;
        outfile << "Case #" << i << ": " << cnt << endl;
    }
    //cin.get();
    infile.close();
    outfile.close();
    return 0;
}
