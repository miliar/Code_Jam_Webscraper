#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


main()
{
	int T,N,K,CASE=0;
	int i,j,k,p;
	char r;
	int x,y;

	vector <char> seq;
	vector <int> o;
	vector <int> b;

	int o_i, b_i, r_i, o_pos, b_pos;

//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);

//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);


	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%d",&N);

		seq.clear();
		o.clear();
		b.clear();

		for(i=0; i<N; i++)
		{
			scanf("%c",&r);
			scanf("%c %d",&r,&p);

			if(r == 'O')
				o.push_back(p);
			else if(r == 'B')
				b.push_back(p);

			seq.push_back(r);
		}


		o_i = 0;
		b_i = 0;
		r_i = 0;

		o_pos = 1;
		b_pos = 1;

		for(y=1; r_i < seq.size(); y++)
		{
			k = 0;

			if(o_i < o.size())
			{
				if(o_pos < o[o_i])
					o_pos++;
				else if(o_pos > o[o_i])
					o_pos--;
				else if(o_pos == o[o_i] && seq[r_i] == 'O')
				{
					o_i++;
					k = 1;
				}
			}

			if(b_i < b.size())
			{
				if(b_pos < b[b_i])
					b_pos++;
				else if(b_pos > b[b_i])
					b_pos--;
				else if(b_pos == b[b_i] && seq[r_i] == 'B')
				{
					b_i++;
					k = 1;
				}
			}

			if(k)
				r_i++;

		}

		y--;

		printf("Case #%d: %d\n",CASE,y);

	}




}