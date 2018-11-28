#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cctype>
#include <fstream>

using namespace std;

int main()
{
	int l, d, n;
	string stmp;
	char fn[256];
	
	cout << "enter filename: " << endl;
	cin.getline(fn,256);
	
	ifstream fs(fn);
	ofstream ofs("out.txt");
	
	
	fs >> l >> d >> n;
	
	vector<string> words;
	
	for(int i = 0; i < d; i++)
	{
		fs >> stmp;
		words.push_back(stmp);
	}
	
	vector<string>::iterator it;
	
	for(int i = 0; i<n; i++)
	{
		int cnt = 0;
		fs >> stmp;
		
		//cout << stmp << endl;//
		
		for(it = words.begin(); it < words.end(); it++)
		{
			//cout << (*it) << endl;//
			
			int scnt = 0;
			
			bool no = false;
						
			for(int j=0; j<l; j++)
			{
				if(stmp[scnt] == '(')
				{
					bool yes = false;
					scnt++;
					while(stmp[scnt] != ')')
					{
						if(stmp[scnt] == (*it)[j])
							yes=true;
					
						scnt++;
					}
					scnt++;
					
					if(!yes)
						no = true;
				}
				else
				{					
					if(stmp[scnt] != (*it)[j])
						no = true;
						
					scnt++;
				}
								
			}
			
			if (no)
				continue;
			
			cnt++;
		}
		
		//cout << endl;//
		
		ofs << "Case #" << i + 1 << ": " << cnt << endl;
		cout << "Case #" << i + 1 << ": " << cnt << endl;//
	}
	
	fs.close();
	ofs.close();
	
	
}