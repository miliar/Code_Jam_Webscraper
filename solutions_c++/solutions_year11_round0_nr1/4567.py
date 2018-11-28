#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


void main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	
	int N=0,T=0;

	cin >> T;

	for(int n = 1 ; n <= T ; n++)
	{
	cin>>N;
	char *color;
	int button;
	int *buttonO;
	int *buttonB;
	bool orange =false;
	color=new char[N];
	buttonO=new int[N];
	buttonB=new int[N];
	int B=0,O=0;
	int CurrentO=1,CurrentB=1,time=0;



		for(int t = 0 ; t < N ; t++)
		{
			cin>>color[t];
			
			if(color[t]=='O')
			{
				cin>>buttonO[O];
				O++;
			}
			else
			{
				cin>>buttonB[B];
				B++;
			}


		}
		
		int tO=0;
		int tB=0;
		int t=0;
		while((tO<O) || (tB<B))
		{
			//what started first ?
			
				if(color[t]=='O')
				{
					orange=true;
				}
				else
				{
					orange=false;
				}


			//for orange

				if(tO!=O)
				{
				if(buttonO[tO]==CurrentO)
				{
					if(orange==true)
					{
						time++;
						//cout<<"Push button"<<CurrentO<<endl;
						//cout<<"Time: "<<time<<endl;
						tO++;
						t++;
					}
					
				}


			else if(buttonO[tO]>CurrentO)
			{
					if(orange==true)
					{
						time++;
					}
					CurrentO++;
					//cout<<"move to button"<<CurrentO<<endl;
					//cout<<"Time: "<<time<<endl;

			}
			else if(CurrentO>buttonO[tO])
			{

					if(orange==true)
					{
						time++;
					}
					CurrentO--;
					//cout<<"move to button"<<CurrentO<<endl;
					//cout<<"Time: "<<time<<endl;
			}

				}
			//for Blue

				if(tB!=B)
				{
			if(buttonB[tB]==CurrentB)
				{
					if(orange==false)
					{
						time++;
						
						//cout<<"Push buttonB " <<CurrentB<<endl;
						//cout<<"Time: "<<time<<endl;
						tB++;
						t++;
					}
					
				}


			else if(buttonB[tB]>CurrentB)
			{
					if(orange==false)
					{
						time++;
					}
					CurrentB++;
					//cout<<"move to buttonB "<<CurrentB<<endl;
					//cout<<"Time: "<<time<<endl;

			}
			else if(CurrentB>buttonB[tB])
			{
					if(orange==false)
					{
						time++;
					}
					CurrentB--;
					//cout<<"move to buttonB "<<CurrentB<<endl;
					//cout<<"Time: "<<time<<endl;
			}
				}



		}
					cout << "Case #" << n << ": " << time << endl;
	}
}