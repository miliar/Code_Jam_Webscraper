#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <stdio.h>
#include <set>
#include <string>
#include <boost/algorithm/string.hpp>
#include <boost/shared_ptr.hpp>

using namespace std;
using namespace boost;


void fatal(string msg, int line)
{
    cout << "Fatal error: " << msg << " on line: " << line << "\n";
    exit(-1);
}

struct DT
{
    string name;
    double weight;
    shared_ptr<DT>  left, right;
    
    DT(int n_lines)
    {
        char buf[10240];
        string all; 
        for (int i = 0; i < n_lines; ++i)
        {
            cin.getline(buf, sizeof(buf));
            all += string(buf) + " ";
        }
        replace_all(all, "(", " ( ");
        replace_all(all, ")", " ) ");
        
        // cout << "Parsing: " << all << "\n---\n";
        istringstream iss(all);
        
        *this = DT(iss);
    }
    
    
    DT(istringstream & iss)
    {
        weight = 0;
        string s;
        
        iss >> s;
        
        if (s != "(")
            fatal("Expecting '(', got \"" + s + "\"", __LINE__);
        // cout << "( " ; 
        iss >> weight;
        
        // cout << weight << " ";
        iss >> s;
        
        if (s == ")")
        {
            // cout << ")\n";
            return;
        }
        else
        {
            name = s;
            // cout << name << " ";
            
            if (s.empty())
                fatal("Empty feature name", __LINE__);
            
            left.reset(new DT(iss));
            right.reset(new DT(iss));
            
            iss >> s;
            if (s != ")")
                fatal("Expecting ).", __LINE__);
            // cout << ")";            
        }
    }
    
    double calc(const set<string> & features) 
    {
        double p = 1.0;
        
        DT * ptr = this;
        
        while (ptr)
        {
            p *= ptr->weight;
//            cout << "using weight " << ptr->weight << ", p = " << p << "\n";
            
            if (ptr->name.empty())
                return p;
//            cout << "count(" << ptr->name << ")= " << features.count(ptr->name) << "\n";
            if (features.count(ptr->name))
                ptr = ptr->left.get();
            else
                ptr = ptr->right.get();
#if 0
            if (! ptr)
            {
                fatal("ptr is not supposed to be NULL.", __LINE__);
            }
#endif            
        }
       return p;
    }
    
    void print(ostream & os)
    {
        os << "( " << weight << " " ;
        if (! name.empty())
            os << name << " ";
        if (left)
            left->print(os);
        if (right)
            right->print(os);
        os << ")\n";
    }
};

int main()
{
    int n_tests;
    char buf[1024];
    
    cin >> n_tests;
    
    for (int i = 0; i < n_tests; ++i)
    {
        int n_lines, n_animals;
        cin >> n_lines;
        
        cin.getline(buf, sizeof(buf));
        
        DT dt(n_lines);
        cout << "Case #" << i + 1 << ":\n";
        // dt.print(cout);
        
        cin >> n_animals;
        
        // cout << "n_animals = " << n_animals << "\n";        
        // 
        for (int k = 0; k < n_animals; ++k)
        {
            string animal_name;
            int n_features;
            cin >> animal_name >> n_features;
            set<string> features;
            
            // cout << "animal= " << animal_name << " n_features=" << n_features << endl;
            
            for (int ni = 0; ni < n_features; ++ni)
            {
                string s;
                cin >> s;
                features.insert(s);
            }
            printf("%.7lf\n",  dt.calc(features));
        }
        
    }
}
