// For Code Jam 2009
// By BAIZHIJIE (baizhj@gmail.com)

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iterator>

using namespace std;

class WelcomeToCodeJam
{
	public:
		void GetTestCases(string inputFile)
		{
			ifstream ifs(inputFile.c_str());
			if(ifs)
			{
				bool loop = !ifs.eof();
				char c;
				int i = 0;
				ifs >> N;
				p = "welcome to code jam";
				string t;
				bool firstline = true;
				while(loop)
				{
					c = ifs.get();
					loop = !ifs.eof();
					if(loop)
					{
						if(('\n'==c)&&(!firstline))
						{
							test.push_back(t);
							t.clear();
							i ++;
						}
						else if(p.find(c)!=string::npos)
						{
							t.push_back(c);	
						}
						else
						{
							// cout << c;
							// t.push_back(c);
							// do nothing.
						}
					}
					firstline = false;
				}
				ifs.close();
			}
		}

		vector<string> RunTestCases()
		{
			vector<string> r;
			for(int j=0; j<test.size(); j++)
			{
				string s = RunTestCase(j);
				r.push_back(s);
			}
			return r;
		}
		
		void ShowTestCases()
		{
			for(vector<string>::iterator iter=test.begin(); iter!=test.end(); iter++)
			{
				cout << *iter << endl;
			}
		}
	private:
		string RunTestCase(int n)
		{
			vector<int> r = rtc(n, 0, 0);
			char c[5] = "\0";
			for(int j=0; j<4; j++)
			{
				c[j] = r[3-j] + '0';
			}
			string s(c);
			return s;
		}
		vector<int> rtc(int n, int d, int j)
		{
			vector<int> r(4, 0);
			
			if(d >= p.length())
			{
				r[0] = 1;
				return r;
			}

			int i = test[n].find(p[d], j);
			while(i!=string::npos)
			{
				vector<int> t = rtc(n, d+1, i+1);

				int addition = 0;
				for(int k=0; k<4; k++)
				{
					r[k] += t[k] + addition;
					addition = r[k] / 10;
					r[k] %= 10;
				}
				// cerr << r[3] << r[2] << r[1] << r[0] << endl;
				i = test[n].find(p[d], i+1);
			}

			return r;
		}
		int N;
		vector<string> test;
		string p;
};

int main(int argc, char * argv[])
{
	if(argc!=3)
	{
		cout << "Usage: " << argv[0] << "<input_file>" << "<output_file>" << endl;
	}
	else
	{
		string file(argv[1]);
		WelcomeToCodeJam wtcj;
		wtcj.GetTestCases(file);
		// wtcj.ShowTestCases();
		vector<string> r = wtcj.RunTestCases();
		ofstream ofs(argv[2]);
		for(int j=0; j<r.size(); j++)
		{
			ofs << "Case #" << j+1 << ": " << r[j] << endl;
		}
	}
	return 0;
}
