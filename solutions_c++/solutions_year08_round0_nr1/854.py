#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class search1
{
public:
	int eng;
	int que;
	vector<string> engstr;
	vector<string> questr;
	vector<string> temp1;
	int count;
	search1();
	void run();
};

search1::search1()
{
	int eng1, que1;
	char c;
	cin >> eng1;
	eng = eng1;
	string temp, z;
	// 	cout<<"111111111111";
	getline(cin, z);
	cin.clear();

	for (int i = 0; i < eng1; i++)
	{
		//cout<<"2222222222222"; 
		getline(cin, temp);
		//cout<<"tttttttt"<<temp<<endl;
		engstr.push_back(temp);
		temp1.push_back(temp);

		temp = "";
		//cout<<temp<<endl;
	}

	cin >> que1;
	//cout<<"ttttttt"<<que1;
	que = que1;
	//cout<<"3333333333";
	getline(cin, z);
	for (int j = 0; j < que1; j++)
	{
		//cout<<"4444444444444";
		getline(cin, temp);
		//cout<<"zzzzzzzzz"<<temp<<endl;
		questr.push_back(temp);

		temp = "";
	}
}

void search1::run()
{
	count = 0;
	vector<string>::iterator pos;

	for (int i = 0; i < questr.size(); i++)
	{
		pos = find(temp1.begin(), temp1.end(), questr[i]);

		if (pos != temp1.end())
		{
			if (temp1.size() == 1)
			{
				//temp1.clear();
				count++; 
				temp1 = engstr;
				pos = find(temp1.begin(), temp1.end(), questr[i]);
				//cout << "aaaaa" << count;
			}
			temp1.erase(pos);
			//cout<<"find"<<endl;
		}
			

	}
}

int main()
{
	int number;
	cin >> number;
	search1* s = new search1[number];
	for (int i = 0; i < number; i++)
	{
		s[i].run();
		cout << "Case #" << i + 1 << ": " << s[i].count << endl;
	}


	return 1;
}