#include<iostream.h>
#include<fstream.h>
#include<math.h>

void main()
{
	int T,N,step[100];
	char bot[100];
	int O_move[100],B_move[100];
	int i;
	int O_loc;
	int B_loc;
	int k,l;
	int time,O,B;

	ifstream ifile;
	ifile.open("input.txt");
	ofstream ofile;
	ofile.open("outputbot.txt");
	ifile>>T;

	for(int count=1;count<=T;count++)
	{
		k=0;
		l=0;
		N=0;
		O_loc=1;
		B_loc=1;
		ifile>>N;

		for(i=0;i<N;i++)
		{
			ifile>>bot[i];
			ifile>>step[i];
		}

		for(i=0;i<N;i++)
		{
			if(bot[i]=='O')
			{
				O_move[k]=abs(step[i]-O_loc);
				O_loc=step[i];
				k++;
			}

			else if(bot[i]=='B')
			{
				B_move[l]=abs(step[i]-B_loc);
				B_loc=step[i];
				l++;
			}
		}


		time=0;
		i=0;
		k=0;
		l=0;
		O=0;
		B=0;

		while(i<N)
		{
			if(bot[i]=='O')
			{
				for(O=O;O<=O_move[k];O++)
				{
					time++;
					if(l!=sizeof(B_move) && B<B_move[l])
						B++;
				}

				i++;
				k++;
				O=0;
			}

			if(bot[i]=='B')
			{
				for(B=B;B<=B_move[l];B++)
				{
					time++;
					if(k!=sizeof(O_move) && O<O_move[k])
						O++;
				}

				i++;
				l++;
				B=0;
			}
		}

		ofile<<"Case #"<<count<<": "<<time<<"\n";
	}
	ofile.close();
	ifile.close();
}
