#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> tokenize(string s)
{
	string temp;
	vector<string> out;
	int mode = 0;
	for(int counter=0; counter<s.length(); counter++)
	{
		if(mode == 0)
		{
			if(s[counter] != '(' && s[counter] != ')')
			{
				string temp1;
				temp1 +=s[counter];
				out.push_back( temp1);
			}
			else
			{
				mode = 1;
			}
		}
		else
		{
			if(s[counter] == ')')
			{
				out.push_back(temp);
				mode = 0;
				temp = "";
			}
			else
			{
				temp += s[counter];
			}
		}
	}
	//printf("begin token\n");
	//for(int counter=0; counter< out.size(); counter++)
	//{
	//	cout<<out[counter]<<endl;
	//}
	//printf("end token\n");
	return out;
}
int main()
{
	int l,d,n;
	cin>>l>>d>>n;
	char buff[10000][20];
	for(int counter = 0; counter< d; counter++)
	{
		cin.getline(buff[counter],l+1);
		if(strcmp(buff[counter],"")==0)
		{
			counter--;
			continue;
		}
		//printf("|%s|",buff[counter]);
	}

	for(int counter = 0; counter< n; counter++)
	{
		string s;
		char temp1[4500];
		cin.getline(temp1,5000);
		//printf("string |%s|\n", temp1);
		s = temp1;
		vector<string> tokens = tokenize(s);
		//cout<<tokens.size()<<" "<<l<<endl;
		int counts[20][30]; // L x 26
		memset(counts,0,sizeof(counts));
		for(int c2=0; c2<tokens.size(); c2++)
		{
			for(int c3 = 0;c3<tokens[c2].length(); c3++)
			{
				counts[c2][tokens[c2][c3]-'a'] = 1;
			}
		}
		int nums = 0;
		for(int c2 =0; c2<d; c2++)
		{
			char *p = &buff[c2][0];
			int c3;
			for(c3 = 0; c3<l;c3++)
			{
				if(counts[c3][*p-'a']==0)
					break;
				p++;
			}
			if(c3==l)
				nums++;
		}
		printf("Case #%d: %d\n",counter+1,nums);
	}
}