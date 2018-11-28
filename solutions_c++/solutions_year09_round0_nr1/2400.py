//Alien Language

#include <iostream> 
#include <cmath> 
#include <vector> 
#include <string> 
#include <map> 
#include <iomanip>

using namespace std;

#define MAXT 20100

bool splitString(vector<string> &tokens, string str, string token)
{
	tokens.clear();
	size_t found;
	string s1;
	found=str.find(token);
	while((found!=string::npos))
	{
		s1 = str.substr(0,found);
		str = str.substr(found+1);
		tokens.push_back(s1);
		found=str.find(token);
	}
	if(!str.empty()) tokens.push_back(str);
}

int main()
{
	int L,D,N;
	cin>>L>>D>>N;
	string words[D], word;
	vector<string> vec;
	int n = 0;
	
	for(int i = 0; i < D; i++)
	{
		cin>>word;
		words[i] = word;
	}
	
	for(int j = 0; j < N; j++)
	{
		cin>>word;
		vec.clear();
		
		int s = 0;
		string w;
		
		while(s < word.size())
		{
			if(word[s] == '(')
			{
				s++;
				while(word[s] != ')') {w+=word[s];s++;}
				vec.push_back(w);
				w = "";	
			}
			else
			{
				w += word[s];
				vec.push_back(w);
				w = "";	
			}
			s++;
		}
		
		if(w.size() > 0) vec.push_back(w);
		
		//for(int j = 0; j < vec.size(); j++) cout<<vec[j]<<endl;
		
		bool succes = false;
		bool suma = false;
		
		for(int i = 0; i < D; i++)
		{
			suma = true;
			for(int k = 0; k < L; k++)
			{
				succes = false;

				for(int m = 0; m < vec[k].size(); m++)
				{
					if(words[i][k] == vec[k][m])
					{
						succes = true;
						continue;	
					}
				}
				
				if(succes == false)
				{
					suma = false;
					break;
				}
			}
			if(suma) n++;
		}
		cout<<"Case #"<<j+1<<": "<<n<<endl;
		n = 0;
	}
}
