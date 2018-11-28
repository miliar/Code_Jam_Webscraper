#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

struct Box
{
       unsigned long long num;
       int type;
       Box(unsigned long long num = 0, int type = 0): num(num), type(type) {}
};

struct Toy
{
       unsigned long long num;
       int type;
       Toy(unsigned long long num = 0, int type = 0): num(num), type(type) {}
};

unsigned long long run(vector<Box> vbox, vector<Toy> vtoy)
{
         unsigned long long num = 0;
         
         if (vbox.size() == 0 || vtoy.size() == 0)
         {
            num = 0;
            return num;
         }
         
         if (vbox[0].type == vtoy[0].type)
         {
            if (vbox[0].num < vtoy[0].num)
            {
               num += vbox[0].num;               
               vtoy[0].num -= vbox[0].num;
               vbox.erase(vbox.begin());
               num += run(vbox, vtoy);               
            }else
            {
               num += vtoy[0].num;
               vbox[0].num -= vtoy[0].num;
               vtoy.erase(vtoy.begin());
               num += run(vbox, vtoy);
            }            
         }else
         {
              unsigned long long num1 = 0;
              vector<Box> vbox_tmp;
              for (int ii = 1; ii < vbox.size(); ii++)
              {
                  vbox_tmp.push_back(vbox[ii]);
              }
              num1 = run(vbox_tmp, vtoy);
              
              unsigned long long num2 = 0; 
              vector<Toy> vtoy_tmp;
              for (int ii = 1; ii < vtoy.size(); ii++)
              {
                  vtoy_tmp.push_back(vtoy[ii]);
              }
              num2 = run(vbox, vtoy_tmp);
              
              if (num1 < num2)
              {
                 num = num2;
              }else
              {
                 num = num1;
              }
         }        
         
         return num;
}

int main()
{
    string in("C-small-attempt0.in");
    ifstream infile;
    infile.open(in.c_str(), ifstream::in);
    
    size_t found = in.find_last_of(".in");
    string out = in.replace(found-1, 2, "myout");    
    ofstream outfile;
    outfile.open(out.c_str(), ofstream::out);
    
    cout.precision(6);
    cout << fixed;
    outfile.precision(6);
    outfile << fixed;    
    
    int t = 0;
    infile >> t;
    cout << t << endl;
    
    for (int i = 1; i < t+1; i++)
    {
        int n = 0;
        infile >> n;
        int m = 0;
        infile >> m;
        cout << n << " " << m << endl;
        
        vector<Box> vbox;
        vector<Toy> vtoy;
        
        for (int ii = 0; ii < n; ii++)
        {
            unsigned long long num = 0;
            infile >> num;
            int type = 0;
            infile >> type;
            Box box(num, type);
            vbox.push_back(box);
            cout << vbox[ii].num << " " << vbox[ii].type << " ";
        }
        cout << endl;
        for (int ii = 0; ii < m; ii++)
        {
            unsigned long long num = 0;
            infile >> num;
            int type = 0;
            infile >> type;
            Toy toy(num, type);
            vtoy.push_back(toy);
            cout << vtoy[ii].num << " " << vtoy[ii].type << " ";            
        }
        cout << endl;
        
        unsigned long long num = run(vbox, vtoy);
        
        cout << "****" << "Case #" << i << ": " << num << endl;
        outfile << "Case #" << i << ": " << num << endl;         
    }    
    
    infile.close();
    outfile.close();
    cin.get();
    return 0;     
}    
