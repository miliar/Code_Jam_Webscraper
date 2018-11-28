#include<iostream>
using namespace std;
string game_state(string s[])
{
	string answer;
	int tag=1;
	int x_win_h[4];
	int x_win_v[4];
	int x_win_d[2]={1,1};
	int o_win_h[4];
	int o_win_v[4];
	int o_win_d[2]={1,1};
	int comp_tag_h[4];
	int comp_tag_v[4];
	int comp_tag_d[2]={1,1};
	int i,j;
	for(i=0;i<4;i++)
	{
		x_win_h[i]=1;
		x_win_v[i]=1;
		o_win_h[i]=1;
		o_win_v[i]=1;
		comp_tag_h[i]=1;
		comp_tag_v[i]=1;
	}	
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(s[i][j]=='X')
			{
				o_win_h[i]=0;
				o_win_v[j]=0;
				if(i==j)
				{
					o_win_d[0]=0;
				}
				if(i+j==3)
				{
					o_win_d[1]=0;
				}
			}
			else if(s[i][j]=='O')
			{
				x_win_h[i]=0;
				x_win_v[j]=0;
				if(i==j)
				{
					x_win_d[0]=0;
				}
				if(i+j==3)
				{
					x_win_d[1]=0;
				}
			}
			else if(s[i][j]=='.')
			{
				tag=0;
				comp_tag_h[i]=0;
				comp_tag_v[j]=0;
				if(i==j)
				{
					comp_tag_d[0]=0;
				}
				if(i+j==3)
				{
					comp_tag_d[1]=0;
				}
			}
		}
	}
	if(x_win_d[0]==1 && comp_tag_d[0]==1)
	{
		
		answer="X won";
		return answer;
	}

	if(x_win_d[1]==1 && comp_tag_d[1]==1)
	{
		answer="X won";
		return answer;
	}
	
	if(o_win_d[0]==1 && comp_tag_d[0]==1)
	{
		answer="O won";
		return answer;
	}

	if(o_win_d[1]==1 && comp_tag_d[1]==1)
	{
		answer="O won";
		return answer;
	}
		
	for(i=0;i<4;i++)
	{
		if(x_win_h[i]==1 && comp_tag_h[i]==1)
		{
			answer="X won";
			return answer;
		}
		else if(o_win_h[i]==1 && comp_tag_h[i]==1)
		{
			answer="O won";
			return answer;		
		}
		else if(x_win_v[i]==1 && comp_tag_v[i]==1)
		{
			answer="X won";
			return answer;
		}
		else if(o_win_v[i]==1 && comp_tag_v[i]==1)
		{
			answer="O won";
			return answer;
		}

	}
	if(tag==0)
	{
		answer="Game has not completed";
	}
	else if(tag==1)
	{
		answer="Draw";
	}
	return answer;
}
int main()
{
	int t,index,i,j;
	string s[4],answer;
	cin>>t;
	for(index=1;index<=t;index++)
	{
		for(i=0;i<=3;i++)
		{
			cin>>s[i];
		}
		answer=game_state(s);
		cout<<"Case #"<<index<<": "<<answer<<endl;		
	}
}
