#include<iostream>
#include<string>
#include<sstream>

using namespace std;

void main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T=0, N=0;
	int surprise;
	int best;

	
	cin >> T;

	
	for(int i=1;i<=T;i++)
	{
	
			cin>>N;
			int scores;
			int midnum;
			int remainder;
			int result=0;
			int surprisetest=0;

		
			cin>>surprise;
			cin>>best;

			//surprisetest=surprise;

			for(int n=0;n<N;n++)
			{
				cin>>scores;

				midnum=scores/(int)3;
				remainder=scores%3;

				if(remainder==0)
				{
					if(midnum>=best)
					{
						result++;
					}
					else
					{
						if((surprise>0)&&(midnum>0)&&((midnum+1)>=best))
						{
							result++;
							surprise--;
						}
					}
				}
				else if ( remainder==1)
				{
					if((midnum>=best)||((midnum+1)>=best))
					{
						result++;
					}
					else
					{
						if((surprise>0)&&((midnum+1)>=best))
						{
							result++;
							surprise--;
						}
					}
				}
			else if (remainder==2)
				{
					if(((midnum+1)>=best)||(midnum>=best))
					{
						result++;
					}
					else
					{
						if((surprise>0)&&((midnum+2)>=best))
						{
							result++;
							surprise--;
						}
					}
				}


			}

			//Debugging purpose 
			/*if(surprisetest==surprise)
			{
				cout<<"yaaayy   "<<surprise<<endl;
			}*/

			cout << "Case #" << i << ": " << result << endl;
	
	}


}