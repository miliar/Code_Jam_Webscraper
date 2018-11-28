#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<sstream>
#include<set>

using namespace std;

vector<int> digitize(int at, int cur)
{
	vector<int> retval;
	while(at!=0)
	{
		retval.push_back(at%cur);
		at/=cur;
	}
	return retval;
}

int summate(vector<int> & in)
{
	int retval = 0;
	for(int i=0;i<in.size();i++)
	{
		retval += in[i];
	}
	return retval;
}

bool attempt(int cur, int at, set<int> & fail)
{
	vector<int> tried;
	vector<int> digits = digitize(at,cur);

	for(int i=0;i<digits.size();i++)
	{
		digits[i]*=digits[i];
	}
	int next = summate(digits);

	while(next!=1)
	{

		if(
(find(fail.begin(),fail.end(),next)!=fail.end()) ||
(find(tried.begin(),tried.end(),next)!=tried.end())
			)
		{
			for(int i=0;i<tried.size();i++)
			{
				fail.insert(tried[i]);
			}
			return false;
		}

		tried.push_back(next);

		digits = digitize(next,cur);
		for(int i=0;i<digits.size();i++)
		{
			digits[i]*=digits[i];
		}
		next = summate(digits);


	}
	return true;
}

int main()
{
	int cases;
	cin >> cases;
	cin.ignore(1);

	vector<set<int> > fail(11,set<int>());

	for(int n=1;n<=cases;n++)
	{
		string temp;
		getline(cin,temp);
		stringstream parse(temp);

		vector<int> bases;
		while(parse.good())
		{
			int temp;
			parse >> temp;
			if(temp!=2)
			{
				bases.push_back(temp);
			}
		}

		sort(bases.begin(),bases.end());
		int retval = 2;
		if(bases.size()==8)
		{
			retval = 11814485;
		}
		if(bases.size()==7)
		{
			if(find(bases.begin(),bases.end(),3)==bases.end())
			{
				retval = 11814485;
			}
			if(find(bases.begin(),bases.end(),4)==bases.end())
			{
				retval = 11814485;
			}
			if(find(bases.begin(),bases.end(),5)==bases.end())
			{
				retval = 4817803;
			}
			if(find(bases.begin(),bases.end(),6)==bases.end())
			{
				retval = 346719;
			}
			if(find(bases.begin(),bases.end(),7)==bases.end())
			{
				retval = 28099;
			}
			if(find(bases.begin(),bases.end(),8)==bases.end())
			{
				retval = 711725;
			}
			if(find(bases.begin(),bases.end(),9)==bases.end())
			{
				retval = 2688153;
			}
			if(find(bases.begin(),bases.end(),10)==bases.end())
			{
				retval = 569669;
			}
		}

		while(retval <= 11814485)
		{
			bool winner = true;
			for(int i=0;i<bases.size() && winner ;i++)
			{
				winner = attempt(bases[i],retval,fail[bases[i]]);
			}
			if(winner)
			{
				break;
			}
			retval++;
		}

		cout << "Case #" << n << ": ";
		cout << retval;
		cout << endl;
	}
	return 0;
}
