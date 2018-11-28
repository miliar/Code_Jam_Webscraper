#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(void)
{
    string s;
    getline(cin,s);
    stringstream ss(s);
    int n;
    ss >> n;
    for (int i = 0; i<n; i++)
    {
        getline(cin,s);
        int arr[11];
        int space = 0;
        for (int j = 0; j < s.length(); j++)
        {
            if (s[j]==' ') { space ++; }
        }
        stringstream sss(s);
        for (int j = 0; j<= space; j++)
        {
            sss >> arr[j];
        }
        bool found = false;
        int k = 0;
        for (k = 2; found == false; k++)
        {
            cout << k;
            found = true;
            for (int j = 0; j<= space; j++)
            {
            //    if (k<arr[j])
            //    {
             //       found = false;
              //      break;
              //  }                
                int num = k;
                int abc[100000];
                for (int xxx=0; xxx<100000; xxx++)
                { abc[xxx] = 0; }
                while ((num!=-1)&&(num!=1))
                {
                    int tempnum = 0;
                    abc[0] ++;
                    abc[abc[0]] = num;
                    while (num >0) 
                    {  tempnum += (num%arr[j]) * (num%arr[j]);  num = num / arr[j]; }
                    for (int yyy=1; yyy<=abc[0]; yyy++)
                    {
                        if (abc[yyy]==tempnum) { num = -1; break;}
                    }
                    if (num != -1)
                    {num = tempnum; }
                }
                if (num != 1)
                {
                    found = false;
                    break;
                }
            }
        }
        cout << "Case #" << i+1 << ": " << k-1 <<endl;
    }
}
