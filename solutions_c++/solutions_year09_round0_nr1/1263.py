#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
using namespace std;
int main()
{
    int l,d,n;
    ifstream in("in.in");
    in >> l >> d >> n;
    vector<string> dic;
    string input;
    for(int i = 0; i < d; i++)
    {
        in >> input;
        dic.push_back(input);
    }
    ofstream out("out.out");
    for(int i = 1; i <= n; i++)
    {
        in >> input;
        vector<string> temp;
        int j = 0;
        string y;
        while(1)
        {
            if(input[j] == '(')
            {
                y = "";
                j++;
                while(input[j] != ')')
                {
                    y += input[j];
                    j++;
                }
                temp.push_back(y);
                cout << y << endl;
                y = "";
                j++;
            }
            else
            {
                y += input[j];
                temp.push_back(y);
                cout << y << endl;
                y = "";
                j++;
            }
            if(j >= input.length()) break;
        }
        int cnt = 0;
        for(int k = 0; k < d; k++)
        {
            string indic = dic[k];
            for(int m = 0; m < l;m++)
            {
                bool flag = 0;
                for(int w = 0; w < temp[m].length(); w++)
                {
                    if(indic[m] == temp[m][w]) {flag = 1;  /*cout << indic[m] << endl;*/ break;}
                }
                if(!flag) break;
                if(m == l - 1)
                {
                    cnt++;
                    cout << indic << endl;
                }
            }
        }
        out << "Case #" << i << ": " << cnt << endl;
    }
    out.close();
    return 0;
}







