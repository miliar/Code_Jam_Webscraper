#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

//void replace (string &);
int searchpattern(string, vector<string> &);

int main()
{
	ifstream in("input.in");
	ofstream out("output.out");
	vector<string> knownstr, recstr ,brokenstr;
	int wrdlen, noswrd, testcase;	
    
    
	in >> wrdlen;
	in >> noswrd;
	in >> testcase;

	string str;
	for(int i = 0; i < noswrd; i++)
	{
		in >> str;
		knownstr.push_back(str);
	}
    	
	for (int i = 0; i < testcase; i++)
	{
		in >> str;
		recstr.push_back(str);
	}
	
	for(int i = 0; i < recstr.size(); i++)
	{
            int pos = 0;
            int result = 0;
            brokenstr.resize(0);
            for(int j = 0; j < recstr[i].length();)
            {
                    if(recstr[i][j] != '(')
                    {
                        string tmpstr = "";
                        tmpstr += recstr[i][j];
                        brokenstr.push_back(tmpstr);
                        j++;
                    }
                     else
                     {
                         pos = recstr[i].find("(",pos) + 1;
                         j =   recstr[i].find(")",pos);
                         brokenstr.push_back(recstr[i].substr(pos,j-pos));
                         j++;
                     }
            }
	        for (int j = 0; j < knownstr.size(); j++)
	        {
                result = result + searchpattern(knownstr[j],brokenstr);
            }
//            cout << "Case #" <<i+1 << ":" << result <<endl;
            out << "Case #" <<i+1 << ": " << result <<endl;
     }

//	system("pause");
	return 0;
}

int searchpattern(string str,vector<string> &s)
{
     int count = 0;
     int pos = 0;
     for (int i = 0; i < s.size(); i++)
     {
         pos = s[i].find(str[i]);
         if (pos == -1)
            return 0;
         else 
              count++;
     }
     if (count = s.size())
        return 1;
}


