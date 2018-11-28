#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

const char in_name[]="A-large.in";
const char out_name[]="123.out";

int main()
{
	ifstream in(in_name);
	ofstream out(out_name);

	queue<int> O,B;
	queue<char>  hod;
	int cur_o=1,cur_b=1;
	int i,j,but,t=0,test,k;
	char c;

	in>>test;
	for(i=0;i<test;i++)
	{	in>>k;
		t=0;
		cur_o=cur_b=1;
		for(j=0;j<k;j++)
		{	in>>c;
			in>>but;
			hod.push(c);
			if(c=='O')
				O.push(but);
			else
				B.push(but);

		}

		while(!hod.empty())
		{	if(hod.front()=='O')
			{	if(cur_o==O.front())
				{	hod.pop();
					O.pop();
					if(!B.empty())
					{if(B.front()-cur_b>0)
						cur_b++;
					else if(B.front()-cur_b<0)
						cur_b--;
					}
				}
				else
				{	if(!O.empty())
					{if(O.front()-cur_o>0)
						cur_o++;
					else if(O.front()-cur_o<0)
						cur_o--;
					}
					if(!B.empty())
					{if(B.front()-cur_b>0)
						cur_b++;
					else if(B.front()-cur_b<0)
						cur_b--;
					}
				}
			}
			else
			{	if(cur_b==B.front())
				{	hod.pop();
					B.pop();
					if(!O.empty())
					{if(O.front()-cur_o>0)
						cur_o++;
					else if(O.front()-cur_o<0)
						cur_o--;
					}
				}
				else
				{	if(!O.empty())
					{if(O.front()-cur_o>0)
						cur_o++;
					else if(O.front()-cur_o<0)
						cur_o--;
					}
					if(!B.empty())
					{if(B.front()-cur_b>0)
						cur_b++;
					else if(B.front()-cur_b<0)
						cur_b--;
					}
				}
			}
			t++;
		}

		out<<"Case #"<<i+1<<": "<<t<<endl;
	}

	in.close();
	out.close();
	return 0;
}