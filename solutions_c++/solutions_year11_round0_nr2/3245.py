#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream in_file("B-large.in");
	ofstream out_file("B-large.out");

	int cases;
	in_file >> cases;
	
	for(int i = 0; i < cases; i++)
	{
		int combo_count;
		in_file >> combo_count;
		
		string combo_list[combo_count];
		
		for(int c = 0; c < combo_count; c++)
		{
			in_file >> combo_list[c];
		}
		
		int oppose_count;
		in_file >> oppose_count;
		
		string oppose_list[oppose_count];
		
		for(int c = 0; c < oppose_count; c++)
		{
			in_file >> oppose_list[c];
		}
		
		int ele_length;
		in_file >> ele_length;
		
		string ele_list;
		in_file >> ele_list;
		
		string new_list;
		
		int cur_length = 0;
		
		bool is_last_combo = false;
		
		for(int c = 0; c < ele_length; c++)
		{
			if(!is_last_combo)
			{
				bool is_combo = false;
				bool is_oppose = false;
				
				
				for(int c2 = 0; c2 < oppose_count; c2++)
				{
					if(oppose_list[c2][0] == ele_list[c])
					{
						for(int c3 = 0; c3 < cur_length; c3++)
						{
							if(new_list[c3] == oppose_list[c2][1])
							{
								is_oppose = true;
								cur_length = 0;
								new_list = "";
								break;
							}
						}
					}
					
					else if(oppose_list[c2][1] == ele_list[c])
					{
						for(int c3 = 0; c3 < cur_length; c3++)
						{
							if(new_list[c3] == oppose_list[c2][0])
							{
								is_oppose = true;
								cur_length = 0;
								new_list = "";
								break;
							}
						}
					}
				}
				
				if(c < ele_length - 1 && !is_oppose)
				{			
					for(int c2 = 0; c2 < combo_count; c2++)
					{
						if(combo_list[c2][0] == ele_list[c])
						{
							if(combo_list[c2][1] == ele_list[c + 1])
							{
								is_combo = true;
								is_last_combo = true;
								new_list.push_back(combo_list[c2][2]);
								cur_length++;
								break;
							}
						}
						else if(combo_list[c2][1] == ele_list[c])
						{
							if(combo_list[c2][0] == ele_list[c + 1])
							{
								is_combo = true;
								is_last_combo = true;
								new_list.push_back(combo_list[c2][2]);
								cur_length++;
								break;
							}
						}
					}
				}

				if(!is_combo && !is_oppose)
				{
					new_list.push_back(ele_list[c]);
					cur_length++;
				}
			}
			
			else
			{
				is_last_combo = false;
			}
		}
		
		out_file << "Case #" << i + 1 << ": [";

		for(int c = 0; c < cur_length; c++)
		{
			out_file << new_list[c];
			if(c < cur_length - 1)
				out_file << ", ";
		}
		out_file << "]" << endl;
	}
	
	return 0;
}

