#include <iostream>
#include <fstream>
#include <queue>
#include <vector>

using namespace std;
struct tr
{
	int start;
	int end;
	int side;//0a 1b
	
	

	};
	
	
  class   greater1   
  {   
          public:  bool   operator()(tr   &t1,tr   &t2)   
            {   
                      return   t1.start>t2.start;   
            }   
  };
  
tr t;
priority_queue  <int,   vector <int> ,   greater<int>  > qa[2];
priority_queue <tr, vector<tr> ,greater1> qt;
int main()
{
		ifstream fin ("B-large.in.txt");
		ofstream fout ("B-large.out.txt");
		int cases,n;
		int ta,tb;
		int delay;
		
		fin>>n;
		int i,j;
		
		for(cases = 1 ;cases<=n;cases ++)
		{
			int ans[2] = {0,0};
			while(!qa[0].empty())
			qa[0].pop();
			while(!qa[1].empty())
			qa[1].pop();
			
			fin>>delay>>ta>>tb;
			
			char c;
			int h,m;
			for(i=0;i<ta;i++)
			{
				fin>>h>>c>>m;
				//	cout<<h<<" "<<m<<endl;
				t.start = h * 60 + m;
				fin>>h>>c>>m;
				t.end = h* 60 + m;
				t.side = 0;		
				
				qt.push(t);
						
			}
			
			for(i=0;i<tb;i++)
			{
				fin>>h>>c>>m;
				
				t.start = h * 60 + m;
				fin>>h>>c>>m;
				t.end = h* 60 + m;
				t.side = 1;			
				qt.push(t);	
			}
			
			//for(i=0;i<ta+tb;i++)
			//cout<<t.start<<" "<<t.end<<" "<<t.side<<endl;
			while(!qt.empty())
			{
				cout<<qt.size()<<endl;
				tr tr1 = qt.top();
				qt.pop();
				cout<<tr1.start<<" "<<tr1.side<<endl;
				if(qa[tr1.side].empty() || qa[tr1.side].top() > tr1.start)
				{
					//cout<<qa[tr1.side].top()<<endl;
					qa[1 - tr1.side].push( tr1.end + delay );
					ans[tr1.side]++;
				}
				else if(qa[tr1.side].top() <= tr1.start)
				{
					qa[tr1.side].pop();
					qa[1 - tr1.side].push( tr1.end + delay );
				}
				else
					{
						cout<<"error"<<tr1.start<<" "<<tr1.end<<" "<<tr1.side<<endl;
						}
			}
			fout<<"Case #"<<cases<<": "<<ans[0]<<" "<<ans[1]<<endl;
		}
}
