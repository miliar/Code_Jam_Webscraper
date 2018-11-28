#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;



string nextNumber(string num)
{
    int digits = 0;
    
    if (num.size() == 1)
        return num;
    
    char tmp = num[0];
        
    num.erase(num.begin());
    num += tmp;
    
    return num;
    
}

string numToString(int num)
{
    int i;
    int digits = 0;
    char buffer[100];
    itoa(num, buffer, 10);
    while (num > 0)
    {
       num = num / 10;
       digits++;  
    }
          
    string temp = "";
    for (i = 0; i < digits; i++)
        temp += buffer[i];
   
    return temp;
}

int main()
{
    ifstream fin;
    ofstream fout;
    
    int T;    
    fin.open("C-large.in");
    fout.open("out.txt");   
    
    fin >> T;
    int tcase = 0;
    while (T--)
    {
        tcase++;
        
        int a, b;
        fin >> a >> b;
        
        int ans = 0;
        int currNumber;
        for (currNumber = a; currNumber <= b; currNumber++)
        {
            int tmp = currNumber;
            string curr = numToString(currNumber);
            string temp = curr;            
                        
            while (1)
            {
                string next = nextNumber(temp);
                // cout << "curr = " << curr << " next = " << next << endl;
                //system("pause");
                if (next == curr)
                    break;
                
                int nextNumber = atoi(next.c_str());
                    
                if (nextNumber >= a && nextNumber <= b && nextNumber > currNumber)
                {
                    ans++;   
                    // cout << "curr = " << temp << " next = "<< next << endl;
                    // system("pause");
                }          
                temp = next;
            }        
        }
        fout << "Case #" << tcase << ": " << ans << endl;  
    }
    
    
    fin.close();
    fout.close();
    system("pause");
    return 0;
}
