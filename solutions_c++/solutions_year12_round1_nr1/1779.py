#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

double func2(long a, long b, float* p, long q)
{
      double s = 0;
      if (a == 0)
      {
         s = b+1+q;
         return s;
      }        
      double exp1 = 0;
      double cp = 1;
      for (long j = 0; j < a; j++)
      {
          cp *= p[j];
      }
      exp1 += cp*(b-a+1+q) + (1-cp)*(b-a+1+b+1+q);
      s = exp1;
      return s;
}

double func(long a, long b, float* p)
{
      double s = 0;
      if (a == 0)
      {
         s = b+1;
         return s;
      }        
      double exp1 = 0;
      double cp = 1;
      for (long j = 0; j < a; j++)
      {
          cp *= p[j];
      }
      exp1 += cp*(b-a+1) + (1-cp)*(b-a+1+b+1);
      double exp2 = b+2;
      
      double *exp = new double[a+1];
      for (long j = 1; j < a+1; j++)
      {
          exp[j] = func2(a-j, b, p, j);
      }
      if (exp1 < exp2)
         s = exp1;
      else
         s = exp2;
      for (long j = 1; j < a+1; j++)
      {
          if (exp[j] < s)
             s = exp[j];
      }
      return s;
}

int main()
{
    string in("A-small-attempt4.in");
    ifstream infile;
    infile.open(in.c_str(), ifstream::in);
    
    size_t found = in.find_last_of(".in");
    string out = in.replace(found-1, 2, "myout_func2");    
    ofstream outfile;
    outfile.open(out.c_str(), ofstream::out);
    
    int t = 0;
    infile >> t;
    cout << t << endl;
    
    for (int i = 1; i < t+1; i++)
    {
        long a = 0;
        infile >> a;
        long b = 0;
        infile >> b;
        cout << a << " " << b << endl;
        
        float *p = new float[a];
        for (long j = 0; j < a; j++)
        {
            infile >> p[j];
        }
        for (long j = 0; j < a; j++)
        {
            cout << p[j] << " ";
        }        
        cout << endl;

        double s = 0;
        s = func(a, b, p);

        cout << "******************" << i << ":\t" << s << endl;
        outfile << "Case #" << i << ": " << s << endl;         
    }    
    
    infile.close();
    outfile.close();
    cin.get();
    return 0;     
}    
