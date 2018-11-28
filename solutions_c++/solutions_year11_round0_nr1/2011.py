#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>

using namespace std;
int abs(int x)
{
	if(x>0)
		return x;
	else
		return -1*x;
}
int main1()
{
	vector<int> O;
	vector<int> B;

	vector<char> step_bot;
	vector<int> step_cod;
	vector<int> complete;
		
	int target;
	
	int t;
	int direction;

	char bot[5];
	int pos;

	int foo;

	int n,n1;

	int check_b;
	int check_o;
	int b_pos,o_pos;
	int b_target,o_target;	
	int o_final_pos,b_final_pos;

	
	
	scanf("%d",&n1);
		
	for(n=0;n<n1;n++)
	{
		scanf("%s",bot);
		scanf("%d",&pos);

		step_bot.push_back(bot[0]);
		step_cod.push_back(pos);

		complete.push_back(0);

		if(bot[0]=='B')
			B.push_back(pos);
		
		if(bot[0]=='O')
			O.push_back(pos);

	}
	// input complete
	// processing start

	t=0;
	target=0;
	b_target=0;
	o_target=0;
	b_pos=1;
	o_pos=1;

	
	while(t+=1)
	{
		//cout<<"T : "<<t<<" " <<o_pos<<" "<<b_pos<<endl;

		if(target==step_bot.size())
			break;

		// check if target reached
			// yes
				// complete target
			// no
				// MOVE the bots
		
		// checking if target reached
		check_b=0;
		check_o=0;

		if(step_bot[target]=='B')
		{
			if(b_pos==step_cod[target])
			{
				complete[target]=1;// pressing the button
				target+=1;
				check_b=1;
				if(b_target!=B.size())
					b_target+=1;
			}
		}

		if(step_bot[target]=='O'&&check_b!=1)// if b is not pressed
		{
			if(o_pos==step_cod[target])
			{
				complete[target]=1;//pressing the button
				target+=1;
				check_o=1;
				if(o_target!=O.size())
					o_target+=1;
			}
		}
		
		if(check_b!=1&&B.size()!=0)
		{
			if(b_target==B.size())
				b_final_pos=b_pos;
			else
				b_final_pos=B[b_target];
			
			direction=0;

			if(b_final_pos!=b_pos)// to not advance it to keep waiting
				direction=(b_final_pos-b_pos)/abs(b_final_pos-b_pos);

			b_pos+=direction; // advance a step towards target and keep waiting if target reached			
		}
		
		if(check_o!=1&&O.size()!=0)
		{
			if(o_target==O.size())
				o_final_pos=o_pos;
			else
				o_final_pos=O[o_target];
			
			direction=0;

			if(o_final_pos!=o_pos)
				direction=(o_final_pos-o_pos)/abs(o_final_pos-o_pos);

			o_pos+=direction; // advance a step towards target and keep waiting if target reached			
		}

	}
	
	return t-1;
}
int main()
{
	int n;
	cin>>n;
	
	for(int k=1;k<=n;k++)
		cout<<"Case #"<<k<<": "<<main1()<<endl;

}
