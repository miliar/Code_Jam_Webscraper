
	#include <iostream>
    #include <vector>
    #include <algorithm>
    #include <string>
    using namespace std;


    unsigned int process_t_string(string t_string, vector<string> dictionary)
	{
		unsigned int i;
		unsigned int count = 0;
	    vector <string> dabba_data;
		bool inside = 0;
		string temp;
		for (i = 0; i<t_string.size();i++)
		{
			if (t_string[i] =='(')
			{
				inside = 1;
				temp = "";
				continue;
			}
			if (t_string[i] == ')')
			{
				inside = 0;
				dabba_data.push_back(temp);
				continue;
            }
			if (inside)
			{
                temp = temp+t_string[i];
			}
			if (!inside)
			{
				string local = "";
				local = local + t_string[i];
			    dabba_data.push_back(local);
			}
		}
		size_t found;
        for (i=0; i<dictionary.size(); i++)
		{
			for (int j=0; j<dictionary[i].size(); j++)
			{
				found = dabba_data[j].find(dictionary[i][j]);
				{
					if (found==-1)
					{
					    count--;
						break;
					}

				}
			}
			count++;

		}
		return count;
	}


	unsigned int main()
	{
		unsigned int L, D, N; 
	    cin>>L;
		cin>>D;
		cin>>N;
		string temp;
        vector <string> dictionary;
		unsigned int temp_D = D;
		while(temp_D--)
		{
		    cin>>temp;
            dictionary.push_back(temp);
		}
		unsigned int temp_N = N;
		while (temp_N--)
		{
			string t_string;
		    cin>>t_string;
			cout<<"Case #"<<N-temp_N<<": "<<process_t_string(t_string, dictionary)<<"\n";
		}
        return 0;
	}
