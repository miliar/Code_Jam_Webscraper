#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

class comb
{
	public:
		comb(bool b, int t)
		{
			bot = b;
			to_press = t;
		}
		
		comb(const comb &to_copy)
		{
			bot = to_copy.bot;
			to_press = to_copy.to_press;
		}
		
		int to_press;
		bool bot;
};

int main(int argc, char *argv[])
{
	FILE *fp = fopen(argv[1],"r");
	
	int tot_cases;
	
	vector<comb> v;
	v.reserve(100);
	
	fscanf(fp,"%d",&tot_cases);
	
	for(int outcnt = 1; outcnt <= tot_cases; outcnt++)
	{		int tot_moves;
		int curr_mov;
		char curr_name;
		
		fscanf(fp,"%d",&tot_moves);
		
		for(int cnt = 1; cnt <= tot_moves; cnt++)
		{		
			fgetc(fp);
			fscanf(fp,"%c%d",&curr_name,&curr_mov);
			if(curr_name == 'O')
				v.push_back(comb(0,curr_mov));
			else
				v.push_back(comb(1,curr_mov));
		}
		
		bool compa = true,compb = true;
		int apos = 1 ,bpos = 1;
		int total_count = 0;
		
		for(size_t acnt = -1, bcnt = -1; ; total_count++)
		{
			if(compa)
				while(++acnt < v.size())
					if(v[acnt].bot == 0)
						break;
						
			if(compb)
				while(++bcnt < v.size())
					if(v[bcnt].bot == 1)
						break;
						
			compa = compb = false;
						
			if(acnt == v.size() && bcnt == v.size())
				break;
						
			if( acnt < bcnt )
			{
				if(bcnt < v.size())
					if(bpos < v[bcnt].to_press)
						bpos++;
					else if (bpos > v[bcnt].to_press)
						bpos--;
				
				if(apos < v[acnt].to_press)
					apos++;
				else if (apos > v[acnt].to_press)
					apos--;
				else
					compa = true;
			}
			
			else
			{
				if(acnt < v.size())
					if(apos < v[acnt].to_press)
						apos++;
					else if (apos > v[acnt].to_press)
						apos--;
				
				if(bpos < v[bcnt].to_press)
					bpos++;
				else if (bpos > v[bcnt].to_press)
					bpos--;
				else
					compb = true;
			}
			
		}
		
		cout<<"Case #"<<outcnt<<": "<<total_count<<endl;
		
		v.clear();
	}
	
	fclose(fp);

	return 0;	
}
