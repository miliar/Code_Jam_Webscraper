#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

bool match(string strDict, string strLost)
{
    vector<string> letters;
    int i,j;
    for(i=0;i<strLost.size();i++)
    {
        string temp;
        if(strLost[i] == '(')
        {
            for(j=i+1;strLost[j]!=')';j++)temp.push_back(strLost[j]);
            i = j;
        }
        if(temp.size()!=0) letters.push_back(temp);
        if(strLost[i] != '(' && strLost[i] != ')')
        {
            string temper;
            temper.push_back(strLost[i]);
            letters.push_back(temper);
        }
    }
    int flag;
    for(i=0;i<letters.size();i++)
    {
        flag = 0;
        for(j=0;j<letters[i].size();j++)
        {
            if(letters[i][j] == strDict[i])
            {
                flag = 1;
                continue;
            }
        }
        if(flag == 0) return 0;
    }
    return 1;
}

int main()
{
	int l,d,n;
	cin >> l >> d >>n;
	vector<string> dict;
	for(int i=0;i<d;i++)
	{
		string str;
		cin >> str;
		dict.push_back(str);
	}
	for(int i=0;i<n;i++)
	{
		int count = 0;
		string str;
		cin >> str;
                for(int j=0;j<dict.size();j++)
                    if (match(dict[j],str)) count++;
		cout << "Case #" << i+1 <<": "<<count<<endl;
	}
}
