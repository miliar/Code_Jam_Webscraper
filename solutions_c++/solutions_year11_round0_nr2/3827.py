
#include <iostream>
#include <vector>
#include <string>
using namespace std;


struct combine
{
    char e1;
	char e2;
	char result;
};


struct opposed
{
    char e1;
	char e2;
	bool c1;
	bool c2;
};


bool check_combine_and_modify(string &seq, char t, vector < combine > &combine_list, vector < opposed > &opposed_list)
{
    if (seq.size()<1)
		return 0;
	char o =  seq[seq.size()-1];

	for (int i=0; i<combine_list.size(); i++)
	{
		if(((combine_list[i].e1 == t) && (combine_list[i].e2 == o))
			||((combine_list[i].e2 == t) && (combine_list[i].e1 == o)))
		{
		    seq[seq.size()-1] = combine_list[i].result;
			return 1;
		}
	}
	return 0;
}

bool check_opposition(vector < opposed > opposed_list, string seq, char t)
{
    string temp;
	temp = seq+t;

	for (int i=0; i<opposed_list.size(); i++)
	{
        bool flag1=0, flag2=0;
		for (int j=0; j<temp.size(); j++)
		{
			if (temp[j] == opposed_list[i].e1)
			{
                flag1 = 1;
			}
		}
		if (flag1 == 0)
            return 0;

		for (int j=0; j<temp.size(); j++)
		{
			if (temp[j] == opposed_list[i].e2)
			{
                flag2 = 1;
			}
		}
		if ((flag1 == 1)&&(flag2 == 1))
		{
			return 1;
		}
	}
	return 0;
}

int main(void)
{
    int num_of_cases;
	cin>>num_of_cases;

	int tc_count = 1;
	while(tc_count <= num_of_cases)
	{

		int no_of_combine;
		cin>>no_of_combine;
		vector < combine > combine_list;
		for (int i=0; i<no_of_combine; i++)
		{
			combine temp;
			cin>>temp.e1>>temp.e2>>temp.result;
			combine_list.push_back(temp);
		}

		int no_of_opposed;
		cin>>no_of_opposed;
		vector < opposed > opposed_list;
		for (int i=0; i<no_of_opposed; i++)
		{
			opposed temp;
			cin>>temp.e1>>temp.e2;
			temp.c1 = 0;
			temp.c2 = 0;
			opposed_list.push_back(temp);
		}
       
		int seq_len;
		cin>>seq_len;

		string seq;

		while(seq_len--)
		{
			char t;
			cin>>t;
			if (check_combine_and_modify(seq, t, combine_list, opposed_list))
			{
				/* already combined and modified */
				/*  */
			    continue;
			}

			if (check_opposition(opposed_list, seq, t))
			{
				/* reset */
				seq = "";
				continue;
			}
			seq += t;
		}

		if (seq.size() == 0)
		{
			cout<<"Case #"<<tc_count<<": []\n";
		}
		else if (seq.size() == 1)
		{
			cout<<"Case #"<<tc_count<<": ["<<seq[0]<<"]\n";
		}
		else
		{
			cout<<"Case #"<<tc_count<<": "<<"[";
			for (int i=0; i<seq.size()-1; i++)
			{
				cout<<seq[i]<<", ";
			}
			cout<<seq[seq.size()-1]<<"]\n";
		}
		tc_count++;
	}
	return 0;
}