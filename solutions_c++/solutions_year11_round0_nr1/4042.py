#include<iostream>
#include<math.h>
#include<fstream.h>
using namespace std;








int canpushB(int B_pos, char color, int pos)
{
	if(color == 'B' && pos == B_pos)
		return 1;
	else
		return 0;
}

int canmoveB(int B_pos, char *color, int *cpos, int pos, int N)
{
	if(color[pos] == 'B' && B_pos!=cpos[pos])
	{
		if(B_pos<cpos[pos])
		{
			return 1;
		} else {
			return -1;
		}
	} else
	{
		for(int i=pos+1; i< N; i++)
		{
			if(color[i] == 'B')
			{
				if(B_pos!=cpos[i])
				{
					if(B_pos<cpos[i])
						return 1;
					else
						return -1;
				}
				break;
			}
		}
		return 0;
	}
	return 0;
}




int canpushO(int O_pos, char color, int pos)
{
	if(color == 'O' && pos == O_pos)
		return 1;
	else
		return 0;
}

int canmoveO(int O_pos, char *color, int *cpos, int pos, int N)
{
	if(color[pos] == 'O' && O_pos!=cpos[pos])
	{
		if(O_pos<cpos[pos])
		{
			return 1;
		} else {
			return -1;
		}
	} else
	{
		for(int i=pos+1; i< N; i++)
		{
			if(color[i] == 'O')
			{
				if(O_pos!=cpos[i])
				{
					if(O_pos<cpos[i])
						return 1;
					else
						return -1;
				}
				break;
			}
		}
		return 0;
	}
	return 0;
}






int main()
{
	int T,N,B_pos = 1, O_pos = 1,*cpos,pos=0,can =0,i,sec=1,change;

	char *color;

	ofstream out;
	ifstream in;
	in.open("in.txt");
	out.open("out.txt");
	in>>T;
	cout<<"#testcases"<<T;
	int counter = 1;
	for(counter=1; counter<=T; counter++)
	{
        cout<<"counter"<<counter<<endl;
		in>>N;
		cout<<"N: "<<N;
		
		color = new char[N];
		cpos = new int[N];
		cout<<endl;
		B_pos = 1; O_pos = 1;pos=0;can = 0;i=0;sec=1;change=0;
		for(i=0; i <N; i++)
		{
			in>>color[i];
			in>>cpos[i];
			cout<<color[i]<<cpos[i]<<" ";
		}
		cout<<endl;
		//cout<<"N: "<<N<<" color: "<<color<<" pos:"<<pos;

		
		while(1){  
            change=0;
			if(canpushB(B_pos, color[pos],cpos[pos])==0)
			{
				can = canmoveB(B_pos, color,cpos, pos, N);
					B_pos+=can;
			} else
			{
              change = 1;
            }
            
			if(canpushO(O_pos, color[pos],cpos[pos]) == 0)
			{
				can = canmoveO( O_pos, color, cpos,pos,N);
					O_pos+=can;
			}else
			{
                 change = 1;
            }
            if(change)
             pos++;
            if(pos == N)
              break; //end of this testcase
            sec++;
		}
		cout<<"\ntestcase:"<<T<<"  secs: "<<sec<<endl;
		out<<"Case #"<<counter<<": "<<sec<<"\n";
		cout<<endl;
		//T--;
		sec = 0;
		delete []color;
		delete []cpos;
	}
	getchar();
}

