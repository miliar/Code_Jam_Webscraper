#include <iostream>
#include <fstream>
using namespace std;

int smaller[2000005];
int biger[2000005];

int value[8]={10,100,1000,10000,100000,1000000,10000000,100000000};
int logs[10];
int index = 0;
int temp[8];
int A, B;


bool repeate(int number)
{
	for(int i=0; i<index; i++)
		if(logs[i]==number)
			return true;
	return false;
}

int At(int t, int loc)
{
	t%=value[loc];
	if(loc!=0)
		t /= value[loc-1];
	return t;
}
void getCount(int t, int bits)
{
	for(int i=0; i<bits; i++)
		temp[i] = At(t,bits-i-1);

	index = 0;
	for(int i=1; i<bits; i++)
	{
		if(temp[i] == 0)
			continue;

		int number = 0;
		for(int j=0; j<bits ; j++)
			number = number * 10 + temp[(i+j)%bits];
		if(number > t && number <= 2000000 && !repeate(number)){
			smaller[number] ++;
			biger[t] ++;
			logs[index++] = number;
		}
	}
}


int getSum13()
{
	int bitsA = 1, bitsB = 1;
	while(A>=value[bitsA-1])
		bitsA++;
	while(B>=value[bitsB-1])
		bitsB++;
	
	if(bitsB!=bitsA || bitsA ==1)
		return 0;

	int sum13=0;
	
	for(int t = value[bitsA-2]; t<A; t++)
	{
		for(int i=0; i<bitsA; i++)
			temp[i] = At(t,bitsA-i-1);

		index = 0;
		for(int i=1; i<bitsA; i++)
		{
			if(temp[i] == 0)
				continue;

			int number = 0;
			for(int j=0; j<bitsA ; j++)
				number = number * 10 + temp[(i+j)%bitsA];

			if(number > B && number <= 2000000 && !repeate(number)){
				sum13++;
				logs[index++] = number;
			}
		}
	}
	return sum13;
}

void init()
{
	memset(smaller, 0, sizeof(smaller));
	memset(biger, 0, sizeof(biger));

	for(int bits=2; bits <=6; bits++)
	{
		int s=1, t=9;
		for(int i=1; i<bits; i++)
		{
			s *=10;
			t = t*10+9;
		}
		for(int i=s; i<=t; i++)
			getCount(i, bits);
	}

	for(int i=1000000; i<=2000000;  i++)
		getCount(i, 7);
	for(int i=1; i<=2000000; i++)
		smaller[i] += smaller[i-1];
	for(int i=2000000-1; i>=0; i--)
		biger[i]+=biger[i+1];
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	init();
	int T;
	cin>>T;
	for(int ti=1; ti<=T; ti++)
	{
		cin>>A>>B;
		int sum13 = getSum13();
		int sumAll = biger[1];
		int SB = smaller[B];
		int BA = biger[A];
		cout<<"Case #"<<ti<<": "<<SB + BA + sum13 - sumAll<<endl;
	}
	return 0;
}