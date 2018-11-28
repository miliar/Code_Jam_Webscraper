#include<iostream>
#include<fstream>
using namespace std;

class BtnList
{
	int btn[100];
	int count;
	int size;
	
public:
	BtnList()
	{
		reset();
	}
	
	void reset()
	{
		count = 1;
		size = 0;
	}
	
	void put(int b)
	{
		size++;
		btn[size] = b;
	}
	
	int get()
	{
		if(count > size) return -1;
		return btn[count++];
	}
	
	bool isDone()
	{
		if(count > size) return true;
		return false;
	}
};

class Bot
{
	int pos;
	int step;
public:
	Bot()
	{
		reset();
	}
	
	void reset()
	{
		pos = 1;
		step = 0;
	}
	
	void press()
	{
		step++;
	}
	
	void go(int tar)
	{
		if(tar < 0) return;
		step += abs(tar - pos);
		pos = tar;
	}
	
	int abs(int n)
	{
		if(n < 0) n = -n;
		return n;
	}
	
	int steps()
	{
		return step;
	}
	
	static void comp(Bot& b1, Bot& b2, int i)
	{
		if(i == 0) 
		{
			if(b1.step > b2.step) b2.step = b1.step;
		}
		else
		{
			if(b2.step > b1.step) b1.step = b2.step;
		}
	}
	
	static void comp(Bot& b1, Bot& b2)
	{
		if(b1.step > b2.step) b2.step = b1.step;
		else b1.step = b2.step;
	}
	
	void show()
	{
		cout << "pos: " << pos << ", step: " << step << endl;
	}
};

void show(Bot& bot1, Bot& bot2)
{
	cout<<"o "; bot1.show();
	cout<<"b "; bot2.show();
	cout<<"@\n";
}

int main()
{
    ifstream fin("q1.in");
    ofstream fout("q1.out");
    int T, N; // T cases, N buttons
    int i, j, k; // counters
    BtnList btn[2];
    Bot bot[2];
    char cbuf1; // input buffer
    int ibuf1;
    int ord[100];
    
    fin >> T;

    for(i = 1; i <= T; i++)
    {
    	fin >> N;
    	
    	bot[0].reset();
    	bot[1].reset();
        
        for(j = 1; j <= N; j++)
        {
            fin >> cbuf1;
            fin >> ibuf1;
            
            ord[j] = cbuf1 == 'O' ? 0 : 1;
            btn[ord[j]].put(ibuf1);      
        }
        
        bot[0].go(btn[0].get());
        bot[1].go(btn[1].get());
        //show(bot[0],bot[1]);
        
        for(j = 1; j <= N; j++)
        {
        	bot[ord[j]].press();
        	//cout<<ord[j]<<"press()\n";
        	Bot::comp(bot[0], bot[1], ord[j]);
        	//show(bot[0], bot[1]);
        	bot[ord[j]].go(btn[ord[j]].get());
        	//show(bot[0], bot[1]);
        }
                
        Bot::comp(bot[0], bot[1]);
                
        fout << "Case #" << i << ": " << bot[0].steps() << '\n';
    }
}
