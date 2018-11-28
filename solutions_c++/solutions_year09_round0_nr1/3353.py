#include <iostream>
#include <string>
#include <vector> 
#include <map>
#include <fstream>

using namespace std;

int cnt=0;
map<string,int> ms;
int len(string wrd);

bool findo(vector<string> &wrds , string txt)
{
	for(int i=0; i < wrds.size(); i++)
		if(wrds[i].substr(0, txt.length()) == txt)
			return true;		

	return false;

}
void func_genrt(string &word,string word1 ,int i, vector<string> &wrd)
{
		if( i >=  word.length())
		{
		//	cout << "Word Found! " << word1 << endl;
			if( ms[word1] == 1)
				cnt = cnt + 1;
			return;
		}

		int j;
		string tmp = "";
		for(j=i; j < word.length(); j++)
		{
		
			if( word[j] == '(' )
			{
				vector<char> temp;
				j++;
				while(word[j] != ')')
				{
					temp.push_back(word[j]);
					j++;
				}			
				for(int k=0; k < temp.size(); k ++)
				{
					if( findo(wrd , word1+tmp+temp[k]) == true)
						func_genrt(word , word1 +  tmp + temp[k] , j+1,wrd);
				
				}
				return;
			}
			else 
				tmp = tmp+word[j];
				
		}
		if(j >= word.length())
		    func_genrt(word , word1 + tmp , j, wrd);
	
		return;
	
}	



	
int main()
{

	int l,d,n;
	string str;
	ifstream if1("A-small.in");
	ofstream of1("output.out");

	if1 >> l >> d >> n ;
//ap<string ,int> ms;
	vector<string> wrd_list;

	for(int i=0; i < d; i++)
	{
		if1 >> str;
		wrd_list.push_back(str);
		ms[string(str)] = 1;
	}
	
	vector<int> result;
	vector<string> result1;
	
	for(int i=0; i < n; i++)
	{
		cnt=0;
		string wrd;
		if1 >> wrd;
		func_genrt(wrd , "" , 0, wrd_list);
		result.push_back(cnt);
	}
	
	for(int i=0; i < result.size(); i++)
		of1 << "Case #" << i+1 << ": " << result[i] << endl;

	if1.close();
	of1.close();
	return 0;
}

int len(string wrd)
{
	int l=0;
	for(int i=0; i < wrd.length(); i++)
	{
		if(wrd[i] == '(')
		{
			while(wrd[i] != ')')
				i++;
			l = l + 1;
		}
		else
			l = l + 1;
	}
	return l;
}	
