#include<iostream>
#include<fstream>
#include<queue>
#include<string>

using namespace std;

void main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int num_test;
	in >> num_test;

	for(int t=0; t<num_test; t++)
	{
		queue<int> orange, blue;
		char seqC[101]={};
		int  seqB[100]={};
		int action=0;
		int o=1, b=1; // orange와 blue의 위치
		int time=0;
		int num_button;
		in >> num_button;
		// input 받음
		for(int i=0; i<num_button; i++)
		{
			in >> seqC[i];
			in >> seqB[i];
		}

		//time check
		while(true)
		{
			char color = seqC[action];
			int button = seqB[action]; //버튼번호
			while( !orange.empty()) orange.pop();
			while( !blue.empty()) blue.pop();
			if( color == 'O') // orange case
			{
				int i=1;
				orange.push(button);
				// O가 나오면 계속 큐에 저장
				while(true)
				{
					if (action+i > num_button) break;
					char tmpC = seqC[action+i];
					int  tmpB = seqB[action+i];
					if(tmpC == 'O')
						orange.push(tmpB);
					else
					{
						blue.push(tmpB);
						break;
					}
					i++;
				}

			}
			else // blue case
			{
				int i=1;
				blue.push(button);
				//B가 나오면 계속 큐에 저장
				while(true)
				{
					if (action+i > num_button) break;
					char tmpC = seqC[action+i];
					int tmpB = seqB[action+i];
					if(tmpC == 'B')
						blue.push(tmpB);
					else
					{
						orange.push(tmpB);
						break;
					}
					i++;
				}
			}
			///// action /////
			if(color == 'O')
			{
				//orange action
				if( button == o)
				{
					//push
					action++;
				}
				else
				{
					//move
					if( button < o)			o--;
					else if (button > o)	o++;
				}
				//blue action
				int tmpB = blue.front();
				if( tmpB == b)
				{
					//stay
				}
				else
				{
					//move
					if( tmpB < b)		b--;
					else if( tmpB > b)	b++;
				}
			}
			else 
			{
				//blue action
				if( button == b)
				{
					//push
					action++;
				}
				else
				{
					//move
					if( button < b)			b--;
					else if (button > b)	b++;
				}
				//orange action
				int tmpB = orange.front();
				if( tmpB == o)
				{	
					//stay
				}
				else
				{
					//move
					if( tmpB < o)		o--;
					else if( tmpB > o)	o++;
				}
			}

			time++;
			if( action == num_button) break;
		}
		out << "Case #"<< t+1<< ": "<< time << endl;
	}

}