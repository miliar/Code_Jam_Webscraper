#include <stdlib.h>
#include <stdio.h>

#include <map>
#include <string>
#include <vector>

using namespace std;

void print_vec(const vector<string> &vec)
{
    printf("[");
    if (vec.size() > 0)
	printf("%s", vec[0].c_str());
    for (unsigned int i = 1; i < vec.size(); ++i)
	printf(", %s", vec[i].c_str());
    printf("]\n");
}

void test_case(int cur_case)
{
    map<string, string> com;
    map<string, bool> opp;
    vector<string> vec;

    int c, d, n;
    scanf("%d", &c);
    for (int i = 0; i < c; ++i)
    {
	char buf[4];
	scanf("%s", buf);
	string lhs = "";
	lhs += buf[0];
	lhs += buf[1];
	string rhs = "";
	rhs += buf[2];
	com[lhs] = rhs;
	lhs = "";
	lhs += buf[1];
	lhs += buf[0];
	com[lhs] = rhs;
    }

    scanf("%d", &d);
    for (int i = 0; i < d; ++i)
    {
	char buf[3];
	scanf("%s", buf);
	string lhs = "";
	lhs += buf[0];
	string rhs = "";
	rhs += buf[1];
	opp[lhs + rhs] = true;
	opp[rhs + lhs] = true;
    }

    scanf("%d", &n);
    char buf[n + 1];
    scanf("%s", buf);
    for (int i = 0; i < n; ++i)
    {
	string str = "";
	str += buf[i];
	vec.push_back(str);

	bool did_something = true;
	while (did_something)
	{
	    did_something = false;
	    if (vec.size() > 1)
	    {
		string vec2 = vec[vec.size() - 2];
		string vec1 = vec[vec.size() - 1];
		
		string com_str = vec2 + vec1;
		if (com.find(com_str) != com.end())
		{
		    vec.pop_back();
		    vec.pop_back();
		    vec.push_back(com[com_str]);
		    did_something = true;
		}
		else
		{
		    bool has_opp = false;
		    for (unsigned int j = 0; j < vec.size() - 1; ++j)
			if (opp.find(vec[j] + vec1) != opp.end())
			    has_opp = true;
		    if (has_opp)
		    {
			vec.clear();
			did_something = true;
		    }
		}
	    }
	}
    }
    
    printf("Case #%d: ", cur_case);
    print_vec(vec);
}

int main(int argc, char **argv)
{
    int t;
    scanf("%d", &t);
    int i;
    for (i = 0; i < t; ++i)
	test_case(i + 1);
    
    return 0;
}
