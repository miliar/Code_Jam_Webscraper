
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>

using namespace std;

vector<string> tionary;

void display_output(long long rv)
{
	long long op[] = {0,0,0,0};
	int j = 3;
	while(rv)
	{
		op[j--] = rv%10LL;
		rv/=10LL;
	}

	for(int  i = 0; i < 4; i++)
		cout<<op[i];
	cout << endl;
}
int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if(argc == 1)
		is.open("C:\\Users\\viv.NORTHAMERICA\\Downloads\\asmall.in");
	else
		is.open(argv[1]);


	// find total number of testcases
	string s;
	getline(is,s); 
	istringstream iss(s);
	iss >> tc;
	//printf("num tc == %d\n", tc);

	// for every testcase
	for(int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ",i);
		// find number of lines for this testcase
		getline(is,s); 
		long long rv = 0;
		for(int w = 0; w < s.size(); w++)
		{
			if('w' != s[w])
				continue;
		for(int e = w+1; e < s.size(); e++)
		{
			if('e' != s[e])
				continue;
		for(int l = e+1; l < s.size(); l++)
		{
			if('l' != s[l])
				continue;
		for(int c = l+1; c < s.size(); c++)
		{
			if('c' != s[c])
				continue;
		for(int o = c+1; o < s.size(); o++)
		{
			if('o' != s[o])
				continue;
		for(int m = o+1; m < s.size(); m++)
		{
			if('m' != s[m])
				continue;
		for(int ee = m+1; ee < s.size(); ee++)
		{
			if('e' != s[ee])
				continue;
		for(int z = ee+1; z < s.size(); z++)
		{
			if(' ' != s[z])
				continue;
		for(int t = z+1; t < s.size(); t++)
		{
			if('t' != s[t])
				continue;
		for(int oo = t+1; oo < s.size(); oo++)
		{
			if('o' != s[oo])
				continue;
		for(int zz = oo+1; zz < s.size(); zz++)
		{
			if(' ' != s[zz])
				continue;
		for(int cc = zz+1; cc < s.size(); cc++)
		{
			if('c' != s[cc])
				continue;
		for(int ooo = cc+1; ooo < s.size(); ooo++)
		{
			if('o' != s[ooo])
				continue;
		for(int d = ooo+1; d < s.size(); d++)
		{
			if('d' != s[d])
				continue;
		for(int ee = d+1; ee < s.size(); ee++)
		{
			if('e' != s[ee])
				continue;
		for(int zzz = ee+1; zzz < s.size(); zzz++)
		{
			if(' ' != s[zzz])
				continue;
		for(int j = zzz+1; j < s.size(); j++)
		{
			if('j' != s[j])
				continue;
		for(int a = j+1; a < s.size(); a++)
		{
			if('a' != s[a])
				continue;
		for(int mm = a+1; mm < s.size(); mm++)
		{
			if('m' != s[mm])
				continue;
			rv++;
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}

		//cout << process_testcase(s) << endl;
		//cout << rv << endl;
		display_output(rv);
	}
	is.close();
	return 0;
}
