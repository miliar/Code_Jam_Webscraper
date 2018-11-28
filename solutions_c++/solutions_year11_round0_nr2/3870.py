#include<iostream>
#include<vector>
#include<string>
using namespace std;

string AllowedChars = "QWERASDF";

string GetList(string combine, string oppose, string input)
{
	string result = "";
	
	if(input.length()==0)
		return result;
	result += input[0];

	for(int i=1;i<input.length();i++)
	{
		char chCombines,chResult,chOpposes;
		if(combine.length() > 0)
		{
			if(input[i] == combine[0]) {
				chCombines = combine[1];
				chResult = combine[2];
			}
			else if(input[i] == combine[1]) {
				chCombines = combine[0];
				chResult = combine[2];
			}
			else
			chCombines = chResult = '#';

		}
		else
			chCombines = chResult = '#';

		if(oppose.length() > 0)
		{
			if(input[i] == oppose[0]) {
				chOpposes = oppose[1];			
			}
			else if(input[i] == oppose[1]) {
				chOpposes = oppose[0];			
			}
			else
			chOpposes = '#';
		}
		else
			chOpposes = '#';

		int len = result.length();
		if(len == 0)
		{
			result += input[i];
			continue;
		}
		// check if it combines with prev
		if(result[len-1] == chCombines)
		{
			result[len-1] = chResult;
		}
		else if(result.find_first_of(chOpposes) != -1)
		{
			result.clear();
		}
		else
			result += input[i];

	}
	return result;
}

void TestGetList()
{
	string result = GetList("","QW","QW");
}

int main()
{
	int n;
	cin >> n;
	for(int i=0;i<n;i++)
	{
		int C;
		string combines = "";
		cin >> C;
		if(C==1)
			cin >> combines;
		int D;
		string opposes = "";
		cin >> D;
		if(D==1)
			cin >> opposes;
		int N;
		string input;
		cin >> N;
		cin >> input;
		
		string result = GetList(combines,opposes,input);
		cout << "Case #"<<i+1<<": [";
		for(int j=0;j<result.length();j++)
		{
			cout << result[j];
			if(j<result.length()-1)
				cout << ", ";
		}
		cout << "]"<<endl;
	}
}