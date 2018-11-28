#include <cstdlib>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <functional>
#include <fstream>
#include <omp.h>
using namespace std;

struct tag_run
{
    int caseid;
    int a;
    int b;
    set<int> set_used;
    long long ans;
    int ccnt;
    tag_run()
    {
        caseid = 0;
        ans = 0;
        ccnt = -1;
    }
};

tag_run test_cases[1000];

long long count_cycle(int num, int a, int b, int ccnt, int scale, set<int> & set_used)
{
	long long ret = 0;
	set<int> ss;

	ss.insert(num);
	for(int i=0; i<=ccnt; i++)
	{
		num = num /10 + num%10*scale;
		if(num >=a && num <=b)
		{
			ss.insert(num);
			set_used.insert(num);
		}
	}
	
	if(ss.size()>1)
	{
		ret = ss.size()*(ss.size()-1)/2;
	}

	return ret;
}

void get_ans(tag_run & tc)
{
    int t = tc.a;
    while(t>0)
    {
        tc.ccnt++;
        t /= 10;
    }
    int scale = pow(10.0, tc.ccnt);

    for(int i=tc.a; i<=tc.b; i++)
    {
        if(tc.set_used.find(i) != tc.set_used.end())
            continue;

        tc.ans += count_cycle(i, tc.a, tc.b, tc.ccnt, scale, tc.set_used);
    }

}

int main()
{
	char chline[10000];
	ifstream inf("in.txt");
	ofstream outf("C-out.txt");

	inf.getline(chline,10000);
	istringstream iss(chline);

	int cnt;
	iss>>cnt;
    for(int zi=0; zi<cnt; zi++) {
        test_cases[zi].caseid = zi;
		inf.getline(chline,10000);
		istringstream iss_l(chline);
		iss_l>>test_cases[zi].a>>test_cases[zi].b;
    }
    inf.close();
    
    #pragma omp parallel for schedule(dynamic) num_threads(8)
	for(int zi=0; zi<cnt; zi++)
	{
        get_ans(test_cases[zi]);
	}
    
    for(int zi=0; zi<cnt; zi++)
    {
        outf<<"Case #"<<zi+1<<": "<<test_cases[zi].ans<<endl;
    }
	
	outf.close();
	return 0;
}
