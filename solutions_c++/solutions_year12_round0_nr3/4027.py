#include<iostream>
#include<vector>
#include<cmath>
#include<fstream>
using namespace std;

vector<int> rotate(int number, int low, int high)
{
    int length = ceil(log10(number));
    int digits[length], i=0;
    while(number!=0)
    {
        digits[i] = number%10;
        number /= 10;
        i++;
    }
    vector<int> combinations;
    combinations.reserve(length);
    for(int shift=0; shift<length; shift++)
    {
        int number = 0;
        for(int i=length-1; i>=0; i--)
            number = number*10 + digits[(i+shift)%length];
        int lengthNew = ceil(log10(number));
        if((length == lengthNew)&&(number>=low)&&(number<=high))
        {
            bool found = false;
            for(int i=0; i<combinations.size(); i++)
            {
                if(combinations[i]==number)
                {
                    found = true;
                    break;
                }
            }
            if(found==false)
                combinations.push_back(number);
        }
    }
    return combinations;
}

int factorial(int n)
{
  return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}

int main()
{
    ifstream in("C:/Users/Ansh/Desktop/C-small-attempt0.in");
    ofstream out("C:/Users/Ansh/Desktop/output.txt");
    int testcases;
    in>>testcases;
    for(int t=0; t<testcases; t++)
    {
        int a,b;
        in>>a>>b;
        int count=0;
        if(b>=10)
        {
            bool flags[b-a+1];
            for(int i=0; i<(b-a+1); i++)
                flags[i] = false;
            for(int i=a; i<=b; i++)
            {
                if(flags[i-a]==false)
                {
                    vector<int> values = rotate(i, a, b);
                    if(values.size()>1)
                    {
                        int inRangeValues = 0;
                        for(int j=0; j<values.size(); j++)
                        {
                                flags[(values[j]-a)] = true;
                                inRangeValues++;
                        }
                        count += factorial(inRangeValues)/(2*factorial(inRangeValues-2));
                    }
                }
            }
        }
        out<<"Case #"<<(t+1)<<": "<<count<<endl;
    }
}
