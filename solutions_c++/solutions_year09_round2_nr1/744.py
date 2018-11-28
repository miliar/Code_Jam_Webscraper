
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

string inp_file = "A-large.in";
string out_file = "A-large.out";

struct TreeNode
{
	TreeNode* left;
	TreeNode* right;
	double prob;
	string feat;
	TreeNode(double p = 0, string f = "")
		:prob(p), feat(f)
	{
		left = NULL;
		right = NULL;
	}

};
class Tree
{
	public:
		Tree(string tree_def)
		{
			root= new TreeNode;
			MakeNode(root,tree_def);

				
		}
	
		double compute_prob(string* features, int f_count)
		{
			return comp_prob(root,features,f_count);
		}
		
	
	private:
		TreeNode* root;
		bool has_it(string f, string* feats, int f_count)
		{
			for(int i= 1; i<=f_count; i++)
			{
				if(feats[i]== f)
					return true;
			}
			return false;

		
		}
		double comp_prob(TreeNode* r, string* features, int f_c)
		{
			if(r->left == NULL)
				return r->prob;
			else if(has_it(r->feat,features,f_c))
				return (r->prob*comp_prob(r->left,features,f_c));
			else
				return (r->prob*comp_prob(r->right,features,f_c));

		
		}
		void MakeNode(TreeNode* curr, string tree_def)
		{
		
			int tree_def_len = tree_def.length();
			int initial_par=-1, final_par=-1;
			bool cont = true;
			for(int i=0; i<tree_def_len && cont;  i++)
			{
				if(tree_def.at(i) == '(')
				{
					cont = false; initial_par = i;
				}

			}
			cont = true;
			for(int i2=tree_def_len-1; i2>=0 && cont;  i2--)
			{
				if(tree_def.at(i2) == ')')
				{
					cont = false; final_par = i2;
				}

			}
				
		
			string new_tree_def = tree_def.substr(initial_par+1,final_par-initial_par-1);
			
			int new_tree_len = new_tree_def.length();
			istringstream inp(new_tree_def);
			inp>>curr->prob;
			
			string temp1 , temp2;
			if(inp>>curr->feat)
			{
				bool ini_cont = true;
				int cntr = 1;
				int ini_coor, fin_coor;
				int i = 0;
					for(; i<new_tree_len && (cntr>=1);  i++)
					{
						if(new_tree_def.at(i) == '(')
						{
							if(ini_cont)
							{
								ini_cont = false; 
								ini_coor = i;
							}
							else
							{
								cntr++;
							}
						}
						else if(new_tree_def.at(i) == ')')
						{
							cntr--;
						}

					}
				fin_coor = i-1;
				temp1 = new_tree_def.substr(ini_coor,fin_coor-ini_coor+1);
				temp2 = new_tree_def.substr(fin_coor+1);
				curr->left = new TreeNode;
				curr->right = new TreeNode;
				MakeNode(curr->left,temp1);
				MakeNode(curr->right, temp2);
							
					
			}
			else
			{
				curr->left = NULL;
				curr->right = NULL;
			}
		
		}


	


};

int main()
{
	int N, L, A ,n2;
	ifstream input;
	input.open(inp_file.c_str());
	input>>N;
	ofstream output;
	output.open(out_file.c_str());
	string tree_def,str_temp ;
	for(int n1 = 1; n1<= N; n1++)
	{
		input>>L;
		tree_def = "";
		getline(input,str_temp);
		for(int l1= 1; l1<= L; l1++)
		{
			getline(input,str_temp);
			tree_def = tree_def + " " + str_temp;
		}
		Tree tr(tree_def);
	
		input>>A;
		output<<"Case #"<<n1<<":"<<endl;
		for(int a= 1; a<=A; a++)
		{
			input>>str_temp;
			input>>n2;
			string* fes = new string[n2+1];
			for(int n_2 = 1; n_2<=n2; n_2++)
			{
				input>>fes[n_2];
			}
			output<<setprecision(8)<<tr.compute_prob(fes,n2)<<endl;

			delete [] fes;
		}

	
	}





	return 0;
}