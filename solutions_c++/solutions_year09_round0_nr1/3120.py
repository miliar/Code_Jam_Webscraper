#include<iostream>
#include<string.h>
#include<list>
#include<set>

using namespace std;

int helper_func(int a[],int n,int l[]);

int main()
{
	int L,D,N;
	cin>>L>>D>>N;
	string dict_word[D];
	string test_case[N];
	set<string> pos_letter[L];
	set<string> dic_wrd;
	set<string> tc_pos_letter[L];
	list<string> result_list;
	
	string temp;
	set<string>::iterator iter1,iter2;
	list<string>::iterator it1;
	
	int i,j,k;
	//input for the words in the dictionary
	for(i=0;i<D;i++)
	{
		cin>>dict_word[i];
		dic_wrd.insert(dict_word[i]);
				
		for(j=0;j<L;j++)
		{
			pos_letter[j].insert(dict_word[i].substr(j,1));
		}
		
	}
	
	//input for test cases
	for(i=0;i<N;i++)
	{
		cin>>test_case[i];
	}
	
	//tokenize the inputs
	for(k=0;k<N;k++)
	{
		temp=test_case[k];
		int ind1,ind2,ind3;
		ind1=0;
		ind2=0;
		ind3=temp.length();
		bool truth=false;
		int count=0;
		
		while(ind2<ind3)
		{
			string ch=temp.substr(ind2,1);
			if(ch=="(")
			{
				truth=true;
			}
			if(ch==")")
			{
				truth=false;
				ind1++;
			}
			else
			{	
				if(1)
				{
					tc_pos_letter[ind1].insert(ch);
				}
				if(truth==false)
				ind1++;
			}
			ind2++;
		}
		//tokenized the input string
		bool yes=true;
		for(int h=0;h<D;h++)
		{
			for(int g=0;g<L;g++)
			{
				if(tc_pos_letter[g].count(dict_word[h].substr(g,1))>0)
				{
					yes=true;
				}
				else
				{
					yes=false;
					break;
				}
			}
			if(yes==true)
			count++;
		}
				
		cout<<"Case #"<<k+1<<": "<<count<<endl;
		
		//end of the work pending
		for(i=0;i<L;i++)
		{
			tc_pos_letter[i].clear();
		}
			
	}
	

return 0;
}


