#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <math.h>
#include <deque>

using namespace std;

#define MAXT 105
#define	MAXC 38
#define MAXD 30
#define MAXN 105

int T,C,D,N;

char elements[]="QWERASDF";

char baseToCombo[4];
char oppo[3];
char testStr[MAXN];
char result[2*MAXN];

char combo[8][8];
bool op[8][8];


int main()
{
	freopen("B-large.in","r", stdin);

	FILE *f = fopen("b-large.out","w");

	cin >> T;

	for(int i=0;i<T;i++)
	{			
		deque<char> q;
		cin >> C;
		for(int ss=0;ss<8;ss++) for(int sss=0;sss<8;sss++)
			combo[ss][sss] = '0';

		for(int cc=0;cc<C;cc++)
		{
			cin >> baseToCombo;
			char ch1=baseToCombo[0];
			char ch2=baseToCombo[1];
			char ch3=baseToCombo[2];
			int s1=0;
			while(elements[s1]!=ch1) s1++;
			int s2=0;
			while(elements[s2]!=ch2) s2++;
			combo[s1][s2] = combo[s2][s1] = ch3;
		}
		cin >> D;
		for(int ss=0;ss<8;ss++) for(int sss=0;sss<8;sss++)
			op[ss][sss]=false;

		for(int dd=0;dd<D;dd++)
		{
			cin >> oppo;
			char ch1=oppo[0];
			char ch2=oppo[1];
			int s1=0, s2=0;
			while(elements[s1]!=ch1) s1++;
			while(elements[s2]!=ch2) s2++;
			op[s1][s2]=op[s2][s1]=true;
		}

		cin >> N;
		cin >> testStr;

		// start
		q.push_back(testStr[0]);
		for(int j=1;j<N;j++)
		{
			char ch = testStr[j];
			// check combine
			int s=0;
			while(ch!=elements[s]) s++;
			if(!q.empty())
			{
				char ch2=q.back();
				int sp = 0;
				// check if the last element is basic element
				while(ch2 != elements[sp]) sp++;
				if(sp<8 && combo[s][sp]!='0')
				{
					q.pop_back();
					q.push_back(combo[s][sp]);
				}
				else
				{	// test all elements in q for opposed elements
					bool opposed = false;
					for(int m=0;m<(int)q.size();m++)
					{
						char ch3 = q[m];
						int l=0; while(ch3!=elements[l]) l++;
						if(l<8 && op[s][l])
						{
							q.clear();
							opposed = true; 
							break;
						}
					}
					if(!opposed)
						q.push_back(ch);
				}
			}
			else
				q.push_back(ch);
		}

		deque<char> r;

		if(q.empty())
		{
			printf("Case #%d: []\n",i+1);
			fprintf(f,"Case #%d: []\n",i+1);
			continue;
		}

		r.push_back('[');
		for(int k=0;k<(int)q.size();k++)
		{
			r.push_back(q[k]);
			r.push_back(',');
			r.push_back(' ');
		}
		r.pop_back(); r.pop_back();
		r.push_back(']');

		int k;
		for(k=0;k<(int)r.size();k++)
			result[k] = r[k];
		result[k]='\0';

		printf("Case #%d: %s\n", i+1, result);
		fprintf(f,"Case #%d: %s\n", i+1, result);
	}

	return 0;
}