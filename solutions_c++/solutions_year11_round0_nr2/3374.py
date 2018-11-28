#include <fstream>
#include <vector>
#include <map>
#include <utility>
#include <string>
#include <stack>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	ifstream input;
	input.open("B-large.in");

	ofstream output;
	output.open("output.txt");

	int T,C,N,D;
	string str;

	input>>T;
	for(int i=0;i<T;++i)
	{
		map < pair < char, char >, char > combine;
		map < char, vector < char > > opposed;
		stack < char > charStack;
		vector <char> charSet;

		input>>C;
		for(int j=0;j<C;++j)
		{	
			input>>str;
			combine[make_pair(str[0],str[1])]=str[2];
			combine[make_pair(str[1],str[0])]=str[2];
		}

		input>>D;
		for(int j=0;j<D;++j)
		{	
			input>>str;
			opposed[str[0]].push_back(str[1]);
			opposed[str[1]].push_back(str[0]);
		}

		input>>N;
		input>>str;

		for(int j=0;j<N;++j)
		{
			char current=str[j];
			if(charStack.empty())
			{
				charStack.push(current);
				charSet.push_back(current);
			}
			else
			{
				char top=charStack.top();
				if((combine.find(make_pair(current,top))!=combine.end()) || (combine.find(make_pair(top,current))!=combine.end()))
				{	
					charSet.pop_back();
					charStack.pop();					

					charStack.push(combine[make_pair(current,top)]);
					charSet.push_back(combine[make_pair(current,top)]);

				}
				else
				{
					
					if(opposed.find(current)!=opposed.end())
					{
						int k=0;
						for(;k<opposed[current].size();++k)
						{
							if(find(charSet.begin(),charSet.end(),opposed[current][k])!=charSet.end())
							{
								while(!charStack.empty())
									charStack.pop();

								charSet.clear();

								break;
							}
						}

						if(k==opposed[current].size())
						{
							charStack.push(current);
							charSet.push_back(current);
						}
					}
					else
					{
						charStack.push(current);
						charSet.push_back(current);
					}


				}
			}
		}


		output<<"Case #"<<i+1<<": [";
		stack <char> reverseStack;
		while(!charStack.empty())
		{
			reverseStack.push(charStack.top());
			charStack.pop();
		}
			
		while(!reverseStack.empty())
		{
			output<<reverseStack.top();
			reverseStack.pop();
			if(reverseStack.size()!=0)
				output<<", ";
		}

		output<<"]";
		
		if(i!=T-1)
			output<<endl;
	}

	input.close();
	output.close();

	return 0;
}