#include <iostream>
#include <vector>


using namespace std;
struct Produccion
{
    char base1;
    char base2;
    char nonbase;
};

struct Opuestos
{
    char a;
    char b;
};

int main()
{
    
    int t;
    cin >> t;
    
    for(int i=0;i < t; ++i)
    {
        int c;
        cin >> c;
        vector<char> elements;
        Produccion prod;
        bool no_prod = c == 0;
        for(int j =0; j <c; ++j)
        {
            cin >> prod.base1 >> prod.base2 >> prod.nonbase;
        }
        int d;
        cin >> d;
        Opuestos op;
        bool no_op = d == 0;
        for (int j=0; j < d; ++j)
        {
            cin >> op.a >> op.b;
        }
        int n;
        cin >> n;
        int theres_a = 0;
        int theres_b = 0;
        for (int j=0; j < n; ++j)
        {
            char temp;
            cin >> temp;
            if(((temp != prod.base1 && temp != prod.base2) || no_prod) && ((temp!= op.a && temp!= op.b)|| no_op))
            {
                elements.push_back(temp);
            }
            else
            {
                if(elements.size()>0 && !no_prod && (temp == prod.base1 || temp == prod.base2))
                {
                    if(temp == prod.base1)
                    {
                        if(elements[elements.size()-1] == prod.base2)
                        {
                            if(!no_op && elements.back() == op.a)
                            {
                                --theres_a;
                            }
                            if(!no_op && elements.back() == op.b)
                            {
                                --theres_b;
                            }
                            elements.pop_back();
                            elements.push_back(prod.nonbase);
                        }
                        else
                        {
                            elements.push_back(temp);
                        }
                    }
                    else
                    {
                        if(elements[elements.size()-1] == prod.base1)
                        {
                            if(!no_op && elements.back() == op.a)
                            {
                                --theres_a;
                            }
                            if(!no_op && elements.back() == op.b)
                            {
                                --theres_b;
                            }
                            elements.pop_back();
                            elements.push_back(prod.nonbase);
                        }
                        else
                        {
                            elements.push_back(temp);
                        }
                    }
                }
                else
                {
                    elements.push_back(temp);
                }
                if(!no_op && (elements[elements.size()-1] == op.a || elements[elements.size()-1] == op.b) )
                {
                    if(elements[elements.size()-1]==op.a)
                    {
                        if(theres_b>0)
                        {
                            elements.clear();
                            theres_a = 0;
                            theres_b =0;
                        }
                        else
                        {
                            ++theres_a;
                        }
                    }
                    if(elements[elements.size()-1]==op.b)
                    {
                        if(theres_a > 0)
                        {
                            elements.clear();
                            theres_a = 0;
                            theres_b =0;
                        }
                        else
                        {
                            ++theres_b;
                        }
                    }
                }
                
            }
            
        }
        cout << "Case #" << i+1 << ": [";
        for(int j =0; j < elements.size(); ++j)
        {
            if(j!=0)
            {
                cout << ", ";
            }
            cout << elements[j];
        }
        cout << "]" << endl;
    }
    return 0;
}
