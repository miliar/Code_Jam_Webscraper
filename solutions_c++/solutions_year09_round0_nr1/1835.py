


#include <iostream>
#include <fstream>
#include <string>
using namespace std;
class tree;

struct tree_node
{
	tree_node** nodes;
	tree_node()
	{
		nodes = new tree_node*[26];
		for(int i= 0; i<26; i++)
			nodes[i]= NULL;
	}
	~tree_node()
	{
		
		for(int i= 0; i<26; i++)
		if(	nodes[i] != NULL)
			delete nodes[i];

		delete [] nodes;
	}
};


class tree
{
	public:
	tree(int l)
	{
		L = l;
		root = new tree_node();

	}
	~tree()
	{
		delete root;
	}
	void add_word(string & s)
	{
		
		add_w(s,root,0);
	}
	int find_word(char** set_of_chr, int* car_of_set)
	{
		return find_w(root,0,set_of_chr,car_of_set);
	}
	private:
	tree_node* root;
	int L;
	void add_w(string & s, tree_node* r,int c)
	{
		if(c >= L)
			return;

		if(r->nodes[s.at(c) -'a'] != NULL)
			add_w(s,r->nodes[s.at(c) -'a'],c+1);
		else
		{
			r->nodes[s.at(c) -'a'] = new tree_node;
			add_w(s,r->nodes[s.at(c) -'a'],c+1);
		}
	}
	int find_w(tree_node* r,int c,  char** set_of_chr, int* car_of_set)
	{
		if(c >= L)
		{	 return 1;}
		int sum = 0;
		for(int i = 0; i<car_of_set[c]; i++)
		{
				if(r->nodes[set_of_chr[c][i]-'a'] != NULL)
					sum += find_w(r->nodes[set_of_chr[c][i]-'a'],c+1,set_of_chr,car_of_set);
		}
		return sum;
			
	}

};

bool update(int* nums,int* limits, int max, int cur)
{

	if(cur >= max)
		return false;
	else
	{
		if( nums[max-cur-1]  + 1 < limits[max-cur-1])
		{
			nums[max-cur-1]++; return true;
		}
		else
		{
			nums[max-cur-1] = 0;
			return update(nums,limits,max,cur+1);
		}
	}
}


int main()
{
	ifstream input;
	input.open("A-large.in");

	int num_of_chrs, num_of_words, num_of_exprs;
	input>>num_of_chrs>>num_of_words>>num_of_exprs;
	tree t(num_of_chrs);
	string temp;
	for(int w = 1; w<= num_of_words; w++)
	{
		input>>temp;
		t.add_word(temp);
	}
	ofstream output;
	output.open("out.txt");
	string s1,s2;
	int current_chr;
	char** chrs;

	chrs = new char*[num_of_chrs];
	int* count_chr = new int[num_of_chrs];
	int temp_initial;
	int* nums = new int[num_of_chrs];
	
	for(int e= 1; e<= num_of_exprs; e++)
	{
		current_chr = 0;
		input>>s1;
	
		for(int c= 0; c< num_of_chrs; c++)
		{
			if(s1.at(current_chr) == '(')
			{
				
				temp_initial = current_chr;
				while(s1.at(current_chr) != ')')
				{
				 current_chr++;
				}
				count_chr[c] = current_chr-temp_initial -1;
				chrs[c] = new char[current_chr-temp_initial -1];
				for(int j = 0; j< current_chr-temp_initial-1; j++)
				{
					 chrs[c][j] = s1.at(j+temp_initial+1);
				}
				

				
			}
			else
			{
				count_chr[c] = 1;
				chrs[c] = new char[1];
				chrs[c][0] = s1.at(current_chr);
				
			
			}
			current_chr++;
		
		}
	
	/*	for(int nn = 0; nn< num_of_chrs; nn++)
			nums[nn] = 0;

		nums[num_of_chrs-1]= -1;

		int final_count = 0;
		string test_s;
*/
	/*	while(update(nums,count_chr,num_of_chrs,0))
		{
			test_s ="";
			
			for(int ccc = 0; ccc<num_of_chrs; ccc++)
			{
				test_s += "a";
				test_s.at(ccc) = chrs[ccc][nums[ccc]];

			}
		//	cout<<test_s<<endl; int g; cin>>g;
			if(t.find_word(test_s))
				final_count++;

		}*/
		output<<"Case #"<<e<<": "<<t.find_word(chrs,count_chr)<<endl;
		for(int c4= 0; c4 <num_of_chrs; c4++)
		{
			delete [] chrs[c4];
		}	
	}

	output.close();
	input.close();
	delete [] chrs;
	delete [] nums;
	delete [] count_chr;






	return 0;
}