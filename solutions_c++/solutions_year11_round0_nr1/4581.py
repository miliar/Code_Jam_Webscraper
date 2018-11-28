#include <cstdio>
#include <cstdlib>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iterator>
#include <math.h>


using namespace std;

//#define SMALL
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

int arr[2011];

inline int noneg(const int& shift,const int& t){
	return (shift-t>0)?(shift-t):0;
}
#define LARGE
int main()
{
	//freopen("b.txt","rt",stdin);
	//freopen("a.out","wt",stdout);
#ifdef SMALL
	freopen("A-small-attempt2.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

	int N;
	int n;
	int sum;
	vector<int> v;
	//int o;
	//int b;
	//int o_p;
	//int b_p;
	//int o_t;
	//int b_t;
	//int temp;
	int pos;//record last ele in vector
	int p;//input pos
	char r;
	char r_b = 'N';
	int last;//
	int s_s;
	int o_p;
	int b_p;

	cin>>N;
	rep(i,N)
	{
		cin>>n;
		o_p = b_p = 1;
		pos = 1;
		last = 0;
		sum = 0;
		r_b = 'N';
		rep(j,n)
		{
			cin>>r;
			
			if(r!=r_b)
			{
				pos = (r=='O')?b_p:o_p;//记录要计算的机器人r_b
				if(!v.empty())
				{
					//int t = *v.begin();
					vector<int>::iterator i = v.begin();
					s_s =0;
					s_s = noneg(abs(*i-pos),last)+1;
					pos = *i;
					i++;
					for(; i!= v.end();i++){
						s_s +=abs(*i-pos)+1;
						pos = *i;
					}
					sum += s_s;
					last = s_s;
					v.clear();
					if(r_b=='O')
						o_p = pos;
					else
						b_p = pos;
				}
				cin>>p;
				v.push_back(p);
				r_b = r;

			}else
			{
				cin>>p;
				v.push_back(p);
			}

		}
		if(!v.empty())
		{

			pos = (r_b=='B')?b_p:o_p;
			//int t = *v.begin();
			vector<int>::iterator i = v.begin();
			s_s =0;
			s_s = noneg(abs(*i-pos),last)+1;
			pos = *i;
			i++;
			for(; i!= v.end();i++){
				s_s +=abs(*i-pos)+1;
				pos = *i;
			}
			sum += s_s;
			last = s_s;
			v.clear();
		}

		printf("Case #%d: %d \n",i+1,sum);
		
	}
	

	

	return 0;
}




