#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <set>

using namespace std;

int main()
{
    string in("C-small-attempt0.in");
    string out("output_3.txt");
    ifstream infile;
    infile.open(in.c_str(), ifstream::in);
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

        for (int a1 = a; a1 < b; a1++)
        {
            set<int>aset;
            for (int k = 1; k < j; k++)
            {
                int back = a1 % (int)floor(pow(10,k));
                int front = a1 / (int)floor(pow(10,k));
                int a2 = back * (int)floor(pow(10,j-k)) + front;
                if (a2 > a1 && a2 <= b)
                {
                   //cout << "(" << a1 << " " << a2 << ")\t";
                   //outfile << "(" << a1 << " " << a2 << ")\t";
                   aset.insert(a2);
                }
            }
            cnt += aset.size();
        }
        //cout << cnt << endl;
        outfile << "\nCase #" << i << ": " << cnt << endl;
    }
    //cin.get();
    infile.close();
    outfile.close();
    return 0;
}
