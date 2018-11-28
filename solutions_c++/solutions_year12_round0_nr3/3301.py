#include<iostream>
#include<vector>
using namespace std;
int numberofdigits(int a)
{
	int count = 0;
	while(a != 0)
	{
		a = a/10;
		count++;
	}
	return count;
}
int rotate(int block, int a)
{
	int bsize=0, asize=0, r, rotate=1;
	while(block != 0)
	{
		block = block / 10;
		bsize++;
	}
	while(a != 0)
	{
		a = a/10;
		asize++;
	}
	r = asize - (bsize-1);
	while(r--)
		rotate *= 10;
	return rotate;
}
int main()
{
	int t;
	cin>>t;
	int tstatic = t;
	while(t--)
	{
		unsigned int a, b, astatic, block = 10, lastdigits, newnumber, count=0, torotate;
		cin>>a>>b;
		vector<int> holder;
		holder.resize(b-a+1);
		astatic  = a;
		for(int i=0;i<holder.size();i++)
			holder[i] = 1;
		while((a/block) != 0)
		{
			torotate = rotate(block,a);
			while(a<=b)
			{
				lastdigits = a % block;
				if(lastdigits == 0 || lastdigits < (block/10))
				{
					a++;
					continue;
				}
				newnumber = (lastdigits*torotate) + (a/block);
				if(newnumber <= b && newnumber > a )
				{
//					cout<<"Old number: "<<a<<" New number: "<<newnumber<<endl;
					count++;
				}
				a++;
			}
			block = block * 10;
			a = astatic;
		}
		if(numberofdigits(a) != 2 && numberofdigits(a) % 2 == 0)
			count = count - (numberofdigits(a)/2) + 1;
		cout<<"Case #"<<(tstatic - t)<<": "<<count<<endl;
	}
}	
