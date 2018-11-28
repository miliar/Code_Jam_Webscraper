#include <iostream>
#include <string>
#include <dispatch/dispatch.h>
using namespace std;
typedef unsigned int uint;

struct trnode
{
	trnode* c[26];
	trnode() {for(uint i=0; i<26; ++i) c[i] = NULL;}
};


uint test(const string &p, uint pos, const trnode *cur)
{
	if (pos >= p.length()) return 1u;
	uint c = 0;
	if (p[pos] == '(')
	{
		uint k = pos;
		while (p[++k] != ')');
		while (++pos < k)
		{
			trnode *t;
			if ((t = cur->c[p[pos]-'a']))
			{
				c += test(p, k+1, t);
			}
		}
	}
	else 
	{
		trnode *t;
		if ((t = cur->c[p[pos]-'a']))
		{
			c += test(p, pos+1, t);
		}
	}
	return c;

}



int main() {
	
	uint L, D, N;
	cin >> L >> D >> N;
	
	trnode root;
	for (uint i=0; i<D; ++i)
	{
		string w;
		cin >> w;
		trnode *c = &root, *t;
		for (uint j=0; j<w.length(); ++j)
		{
			
			if (!(t = c->c[w[j] - 'a']))
				t = c->c[w[j]-'a'] = new trnode();
			
			c = t;
		}
	}
	
	uint res[N];
	dispatch_queue_t queue = dispatch_get_global_queue(0,0);
	dispatch_group_t group = dispatch_group_create();
	
	for (uint i=0; i<N; ++i)
	{
		string p;
		cin >> p;
		res[i] = 0u;
		dispatch_group_async(group, queue, ^{
			res[i] = test(p,0,&root);
		});
	}
	
	dispatch_group_wait(group,DISPATCH_TIME_FOREVER);
	for (uint i=0; i<N; ++i)
	{
		cout << "Case #" << (i+1) << ": " << res[i] << endl;
	}

	
	return 0;
}