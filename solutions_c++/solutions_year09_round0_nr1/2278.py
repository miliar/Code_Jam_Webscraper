#include <iostream>
#include <map>
#include <set>
#include <string>
#include <fstream>
#include <list>
#include <stack>
#include <vector>
using namespace std;

 set <string> wordSet;
 int count = 0;
 int len = 0;

/*int processWords(list <vector<char> > &words, list <vector<char> >::iterator iter, string temp)
{
	list<vector<char> >::iterator it;
	for (it = iter; it != words.end();)
	{
		vector<char> charVec = *it;
		vector<char>::iterator it1;
		for (it1 = charVec.begin(); it1 != charVec.end(); it1++)
		{
			string temp1 = temp;
			temp.push_back(*it1);
			if (temp.length() == 3)
			{
				cout << temp << endl;
				temp.clear();
				temp = temp1;
			}
			if (it != words.end())
			{
				it++;
				processWords(words, it, temp);
			}
		}
	}
	return 0;
}*/

/*int process(list <vector<char> > &words, list <vector<char> >::iterator iter, string temp = "")
{
	list<vector<char> >::iterator it;
	for (it = iter; it != words.end();)
	{
		vector<char> charVec = *it;
		vector<char>::iterator it1;
		for (it1 = charVec.begin(); it1 != charVec.end(); it1++)
		{
			string temp2 = temp;
			string temp1 = temp2;
			temp2.push_back(*it1);
			if (it != words.end())
				it++;
			if (temp2.size() == 3)
			{
				cout << temp2;
				temp2.clear();
				temp2 = temp1;
			}
			process(words, it, temp2);
		}
	}
	return 0;
}*/

int process(vector <vector<char> > &words, int pos, string temp = "")
{
	set <string>::iterator it;

	for (it = wordSet.begin(); it != wordSet.end(); it++)
	{
		bool flag = true;
		string temp = *it;
		for (int i = 0; i < temp.size(); i++)
		{
			char c = temp[i];
			vector<char> &chars = words[i];
			for (int j = 0; j < chars.size(); j++)
			{
				if (chars[j] == c)
				{
					flag = true;
					break;
				}
				else
				{
					flag = false;
				}
			}
			if (flag == false)
			{
				break;
			}
		}
		if (flag == true)
		{
			count++;
		}
	}
	return 0;
}
/*int process(vector <vector<char> > &words, int pos, string temp = "")
{
	for (int i = pos; i < words.size(); i++)
	{
		vector<char> charVec = words[i];
		vector<char>::iterator it1;
		for (it1 = charVec.begin(); it1 != charVec.end(); it1++)
		{
			string temp2 = temp;
			string temp1 = temp2;
			temp2.push_back(*it1);
			int j = i+1;
			if (temp2.size() == len)
			{
				//cout << temp2 << endl;
				if (wordSet.count(temp2))
				{
					count++;
				}
				temp2.clear();
				temp2 = temp1;
			}
			process(words, j, temp2);
		}
	}
	return 0;
}*/


int main(int argc, char **argv)
{
    ifstream ifstr("Input.txt");
	ofstream ofstr("Output.txt");
    char buffer[1000000];
    memset(buffer, 0, 1000000);
    ifstr.getline(buffer, 1000000, '\n');

    string first(buffer);
    cout << first << endl;
    len = atoi(first.substr(0, first.find_first_of(" ")).c_str());
    first.erase(0, first.find_first_of(" ")+1);
    cout << first << endl;
    int numOfWords = atoi(first.substr(0, first.find_first_of(" ")).c_str());
    first.erase(0, first.find_first_of(" ")+1);
    int numOfCases = atoi(first.substr(0, first.find_first_of(" ")).c_str());
    cout << len << " " << numOfWords << " " << numOfCases << endl;

   
    for (int i = 0; i < numOfWords; i++)
    {
        memset(buffer, 0, 1000000);
        ifstr.getline(buffer, 1000000, '\n');
        string line(buffer);
        wordSet.insert(line);
    }

    vector <vector<char> > words;
    for (int i = 0; i < numOfCases; i++)
    {
		/*if (i == 5)
		{
			int i = 0;
			cin >> i;
		}*/
		words.clear();
        memset(buffer, 0, 1000000);
        ifstr.getline(buffer, 1000000, '\n');
        string line(buffer);
        bool flag = false;
		
		for (int j = 0; j < line.length(); j++)
        {
            static vector<char> charSet;

			/*set <string>::iterator sit;
			for (sit = wordSet.begin(); sit != wordSet.end(); sit++)
			{
				string temp = *sit;
				int pos = temp.find(line[j]);
				if (pos == string::npos)
				{
					continue;
				}
			}*/
            if (line[j] == '(')
            {
                flag = true;
                continue;
            }
            else if (line[j] == ')')
            {
                flag = false;
                words.push_back(charSet);
                charSet.clear();
                continue;
            }

            if (flag)
            {
                charSet.push_back(line[j]);
                continue;
            }
            vector <char> charSet1;
            charSet1.push_back(line[j]);
            words.push_back(charSet1);
        }
        process(words, 0);
		cout << count;
		ofstr << "Case #" << (i+1) << ": " << count << endl;
		count = 0;
		cout << endl;
	}
    return 0;
}