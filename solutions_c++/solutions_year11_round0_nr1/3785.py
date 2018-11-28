#include <iostream>
#include <string>
#include<stdlib.h>
#include <fstream>
using namespace std;


int main()
{
int T;
//N no o	f test cases
cin>>T;
int *O, *B,*roboOrder;
ifstream ifile("robots_input_small.txt");
for(int main=0;main<T;main++)
{
        int N =0;
	ifile >> N;
        O = new int[N];
        B = new int[N];
	roboOrder = new int[N];
	

        int io= 0, ib= 0;
        for(int i=0;i<N;i++)
        {
        O[i] = -1;
        B[i] = -1;
        }
	int count = 0, iColor, k=0;
        while(count < N*2)
      	{
	char ch;
	ifile.get(ch);
		if(ch == ' ')
			continue;
		if(ch == 'O')
              	{
			roboOrder[k++] = 1;
			int temp;
			ifile >> temp;
   			O[io] = temp;
  //                      cout<<"\n Orange:"<<O[io];
                        io++;
                }
                else if(ch == 'B')
                {
			roboOrder[k++] = 2;
			int temp;
			ifile >> temp;
			B[ib] = temp;
    //                  cout<<"\n Blue:"<<B[ib];
                        ib++;
                }
		else if(ch == '\n')
		{
			break;
		}	
	count ++;
        }
//main algio


int sec =0, oPos=1, bPos=1,i=0,j=0,order=0,presscount =0;
bool bBreak= false;
while(1)
{
bool bMoved = false, bPressed = false;
//cout<<"\n roboorder "<< roboOrder[order];

{
	if(roboOrder[order]==1 && oPos == O[i] && !bPressed)
	{
//	cout<<"\n O Pressed "<<oPos;
	bPressed = true;
	presscount++;
	order++;
	i++;
	}
	else if((O[i] - oPos) != 0)
	{
//	cout<<"\n O moved";
	bMoved = true;
	if((O[i] - oPos) > 0)
		oPos ++;
	else
		oPos--;
	}
}
//if((B[j] - bPos) >=0)
{
	if(roboOrder[order]==2 && bPos == B[j] && !bPressed)
	{
//	cout<<"B pressed :"<<bPos;
	bPressed = true;
	presscount++;
	order++;
	j++;
	}
	else if((B[j]-bPos) != 0)
	{
//	cout<<"b moved";
	bMoved = true;
	if((B[j] - bPos) > 0)
		bPos ++;
	else
		bPos--;
	}
}
//cout<<"\n Sec "<<sec<<" OPos : "<<oPos<<" BPos : "<<bPos<<" order : "<<order<<" presscount : "<<presscount;

if(bMoved || bPressed)
sec++;

if(bBreak)
break;

///cout <<"\n -------------------------------------"<<presscount<<" N "<<N<<" main "<<main;
if(presscount == N)
break;
}

cout<<"\n Case #"<<main+1<<": "<<sec;
}

ifile.close();
}

