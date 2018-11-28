#include<iostream>
#include <string>
#include<fstream>
#include<ostream>
#include<vector>
using namespace std;
#define InputOutputToFile

int main(void)
{
#ifdef InputOutputToFile
	
	//cin redirection
	std::ifstream fin("cin.txt");
	std::streambuf *inbuf = std::cin.rdbuf(fin.rdbuf());

	//cout redirection
	std::streambuf* cout_sbuf = std::cout.rdbuf(); // save original sbuf 
	std::ofstream   fout("cout.txt"); 
	std::cout.rdbuf(fout.rdbuf()); // redirect 'cout' to a 'fout' 
	//std::cout.rdbuf(cout_sbuf); // restore the original stream buffer 
#endif

	int run = 0;
	cin>>run;
	int cs = 1;
	bool itrFlg = false;

	while(run--)
	{
		if(itrFlg)
			cout<<endl;
		itrFlg = true;

		int g = 0;
		cin>>g;
		int s = 0;
		cin>>s;
		int at = 0;
		cin>>at;
		vector<int> vc;
		vector<int>::iterator it_vc;
		int tmp=0;

		for(int i=0;i<g;i++)
		{
			cin>>tmp;
			vc.push_back(tmp);
		}

		int scr[3];

		int div = 0;
		int mod = 0;

		int count = 0;
		bool flag = true;

		for(it_vc = vc.begin();it_vc<vc.end();it_vc++)
		{
			flag = true;
			div = 0;
			mod = 0;
			tmp = *it_vc;
			div = tmp/3;
			mod = tmp%3;
			if(mod == 0)
			{
				scr[0]=scr[1]=scr[2]=div;
			}
			else if( mod == 1)
			{
				scr[0]=scr[1]=div;
				scr[2] = div+1;
			}
			else if( mod == 2)
			{
				scr[0]=div;
				scr[1]=scr[2]=div+1;
			}
			
			if(scr[2]>=at)
			{
				count++;
				flag = false;
			}
			
			if(s && flag)
			{
				if(scr[2]>0 && (scr[2] == (at-1)) && (scr[1] == (at-1)))
				{
					scr[2]++;
					scr[1]--;
					count++;
					s--;
					flag = false;
				}
			}
		}
		cout<<"Case #"<<cs<<": "<<count;
		cs++;
	}

	return 0;
}
