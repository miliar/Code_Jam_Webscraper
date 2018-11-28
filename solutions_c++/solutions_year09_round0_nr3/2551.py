#include <iostream>
#include <cstdio>
#include <cmath>
#include <deque>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cctype>
#include <fstream>
#include <utility>

using namespace std;

deque<pair<char,int> > procd;
string wel = "welcome to code jam";

int sub(int loc, int cloc)
{
	//cout<<wel[cloc];//

	int cnt =0;
	for(int j=loc; j<procd.size(); j++)
	{
		
		if(cloc == 18 && procd[j].first == 'm')
			cnt += procd[j].second;
		else if(procd[j].first == wel[cloc])
			cnt += (procd[j].second * sub(j+1, cloc+1));
			
		cnt %= 10000;
	}	

	return (cnt%10000);

}

int main()
{
	char fn[256];
	
	cout << "enter filename: " << endl;
	cin.getline(fn,256);
	
	ifstream fs(fn);
	ofstream ofs("out.txt");
	
	int n;
	char stmp[501];	
	
	fs >> n;
	fs.getline(stmp, 501);//to consume endline char on 1st line
	
	for(int i=0; i<n; i++)
	{		
		procd.clear();
		
		fs.getline(stmp, 501);
		
		//cout<<stmp<<endl;//
		
		char last = '.';
		int cnt = 0;
		
		for(int j=0; stmp[j]!='\0'; j++)
		{
			char c = stmp[j];
			if(c == last)
				cnt++;
			else if(c=='w' || c=='e' || c=='l' || c=='c' || c=='o' || c=='m' || c==' ' || c=='t' || c=='d' || c=='j' || c=='a')
			{
				procd.push_back(make_pair(last,cnt));
				last=c;
				cnt=1;
			}
		}
		
		if(last != '.')
		{
			procd.push_back(make_pair(last,cnt));
			procd.pop_front();
		}
		
		// for(int j=0; j<procd.size(); j++)
		// {
			// cout << procd[j].first << ' ' << procd[j].second << ",";//
		// }
		
		//cout << endl;//
		
		cnt=0;
		
		for(int j=0; j<procd.size(); j++)
		{
			cout << 'w';//
			if(procd[j].first == 'w')
				cnt += (procd[j].second * sub(j+1, 1));	
			
			cnt %= 10000;
		}
		
		char ans[5];
		sprintf(ans, "%04d", cnt);
		//cout << endl;//
		ofs << "Case #" << i+1 << ": " << ans << endl;
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	
	fs.close();
	ofs.close();
	
	
}