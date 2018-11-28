#include<iostream>
#include<fstream>
#include<string>
using namespace std;

void non_surprising(int&n1, int&n2, int&n3 , int number);
void surprising(int&score1,int&score2,int&score3);
int main()
{
	//ifstream in("B-small-attempt0.in");
	ifstream in("B-large.in");
	ofstream out("fileL.txt");

	int p,s,n;
	int num_lines;
	int*arr;

	int score1;
	int score2;
	int score3;

	int output=0;
	in>>num_lines;
	for(int i=0; i<num_lines; i++)
	{
		in>>n;
		arr=new int[n];
		in>>s;
		in>>p;
		
		for(int i=0; i<n; i++)
		{
			in>>arr[i];
		}

		for(int i=0; i<n; i++)
		{
			non_surprising(score1,score2,score3,arr[i]);
			if(score1>=p)
				output++;
			else if(score2>=p)
				output++;
			else if(score3>=p)
				output++;
			else
				{
					if(s>0)
					{
						surprising(score1,score2,score3);
						

						if(score1>=p)
						{
							output++;
							s--;
						}
						else if(score2>=p)
						{
							output++;
							s--;
						}
						else if(score3>=p)
						{
							output++;
							s--;
						}
					}
				}
		}
		out<<"Case #"<<i+1<<": "<<output<<endl;
		output=0;
	}
	return 0;
}

void non_surprising(int&n1, int&n2, int&n3 , int number)
{
	int R=number/3;
	if(number-R*3 == 0)
	{
		n1=R;
		n2=R;
		n3=R;
	}
	else if(number-R*3 == 1)
	{
		n1 = R+1;
		n2 = R;
		n3 = R;
	}
	else if(number-R*3 == 2)
	{
		n1 = R+1;
		n2 = R+1;
		n3 = R;
	}
}

void surprising(int&score1,int&score2,int&score3)
{
	bool x = true;
	
	while(x==true)
	{
		if((score1+score2+score3==0)||(score1+score2+score3==1)||(score1+score2+score3==29)||(score1+score2+score3==30))
			x=false;
		else
		{
			int test1 = score1+1;
			int test2 = score2-1;
			
			if((test1-test2)<=2)
			{
				score1 = test1;
				score2 = test2;
				x=false;
			}
			else
			{
				score2 = score2+1;
				score3 = score3-1;
				x=false;
			}
		}
	}
}