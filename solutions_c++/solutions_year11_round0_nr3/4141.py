#include <stdio.h>
#include <fstream.h>

int	Partition(long *Array,int low,int high)
{
	int pivotkey = Array[low];
	Array[0] = Array[low];

	while(low<high)
	{
		while(low<high && Array[high]>=pivotkey)
			--high;
		Array[low] = Array[high];

		while(low<high && Array[low]<=pivotkey)
			++low;
		Array[high] = Array[low];
	}

	Array[low] = Array[0];

	return low;
}

void	QSort(long *Array,int low,int high)
{
	if(low<high)
	{
		int pivotloc = Partition(Array,low,high);
		QSort(Array,low,pivotloc-1);
		QSort(Array,pivotloc+1,high);
	}
}

long Run(long *a,int length)
{
	long n = 0;
	long tempn;
	long tempv = 0;
	long value = 0;
	int temp;
	for(int i=1;i<=length;i++)
	{
		n = n^a[i];
	}
	if(n != 0)
		return -1;

	while(length > 1)
	{
		tempn = n^a[length];
		tempv = tempv^a[length];
		temp = tempn^tempv;
		if(temp == 0)
		{
			value += a[length];
			n = tempn;
			
		}//if
		else
		{
			tempv = tempv^a[length];
		}

		length--;
	}
	tempn = n^a[1];
	if(tempn != 0)
	{
		tempv = tempv^a[length];
		temp = tempn^tempv;
		if(temp == 0)
		{
			value += a[length];
			n = tempn;
			
		}//if
		else
		{
			tempv = tempv^a[length];
		}
	}

	return value;
}


void main()
{
	ifstream in;
	ofstream out;

	in.open("D:\\input.in",ios::out,0);
	out.open("D:\\out.out",ios::out,0);

	int total;
	in>>total;
	
	long a[1001] = {0};

	int index = 1;
	int indext = 1;
	int i;
	long num;
	while(total > 0)
	{
		total--;
		index = 1;
		for(i=0;i<1001;i++)
			a[i] = 0;
		
		in>>i;
		while(i-- > 0)
			in>>a[index++];
		QSort(a,1,index-1);

		num = Run(a,index-1);
		if(num == -1)
		{
			out<<"Case #"<<indext<<": "<<"NO"<<"\n";
		}
		else
		{
			out<<"Case #"<<indext<<": "<<num<<"\n";
		}
		indext++;
	}
}