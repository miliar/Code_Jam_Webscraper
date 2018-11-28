#include <fstream>
#include <vector>
#include <iostream>
#include <string>

int main()
{
	std::ifstream in("magicka.in");
	std::ofstream out("magicka.out");
	int T;
	in >> T;
	
	for(int i=1; i<=T; ++i)
	{
		out << "Case #" << i << ": [";
		bool badpairs[200][200]={0};
		char goodpairs[200][200]={0};
		int N;
		in >> N;
		for(int i=0; i<N; ++i)
		{
			std::string temp;
			in >> temp;
			goodpairs[temp[0]][temp[1]]=temp[2];
			goodpairs[temp[1]][temp[0]]=temp[2];
		}
		in >> N;
		for(int i=0; i<N; ++i)
		{
			std::string temp;
			in >> temp;
			badpairs[temp[0]][temp[1]]=true;
			badpairs[temp[1]][temp[0]]=true;
		}
		
		in >> N;
		std::string invoking;
		std::vector<char> result;
		in >> invoking;
		
		for(int i=0; i<N; ++i)
		{
			if(result.size()>0)
			{
				if(goodpairs[invoking[i]][result.back()] != 0)
				{
					char temp = goodpairs[invoking[i]][result.back()];
					result.pop_back();
					result.push_back(temp);
				}
				else
				{
					bool del=false;
					for(int n=0; n<result.size(); ++n)
					{
						if(badpairs[result[n]][invoking[i]])
						{
							del=true;
							break;
						}
					}
					if(del)
					{
						while(result.size()!=0)
						{
							result.pop_back();
						}
					}
					else
					{
						result.push_back(invoking[i]);
					}
				}
			}
			else
			{
				result.push_back(invoking[i]);
			}
		}
		
		if(result.size()>0)
		{
			for(int i=0; i<result.size()-1; ++i)
			{
				out << result[i] << ", ";
			}
			out << result.back() << "]" << std::endl;
		}
		else
		{
			out << "]" << std::endl;
		}
	}
	
}















