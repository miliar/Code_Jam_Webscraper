#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	ifstream fi("data.txt");
	ofstream fo("output.txt");
	int lines;
	fi >> lines;
	bool isNotTransponse(int a);
	int count(int j,int a,int b);
	int* da;
	da = new int[lines];
	int a;
	int b;
	for(int i=0; i<lines;i++)
	{
		da[i] = 0;
		fi >> a >> b;
		if((b>=10))
		{
			for(int j=a;j<b+1;j++)
			{
				 if(isNotTransponse(j))
				 {
					da[i] +=  count(j,a,b);
				 }
			}
		}
		//cout << "Case #" << i+1 <<": " << da[i] << endl;
		fo << "Case #" << i+1 <<": " << da[i] << endl;
	}
	fi.close();
	fo.close();
	return 0;
}
bool isNotTransponse(int j)
{
	int a0;
	int a1;
	int a2;

	a0 = j%10;
	a1 = (j%100-a0)/10;
	a2 = j/100;

	if((a0 == a1)&&(j<100))
		return false;
	else if((j>100) && (a0 == a1) &&(a1 == a2) && (a0 == a2))
		  return false;
	else
		return true;

}
int count(int j,int a,int b)
{
	int count=0;
	int a0;
	int a1;
	int a2;
	int a3;
	a0 = j%10;
	a1 = (j%100-a0)/10;
	a2 = j/100;
	a3 = j/1000;

	if(j<100)
	{
		
		int Nj;
		Nj = 10 * a0 + a1;
		if((Nj>= a)&& (Nj<=b)&&(Nj > j))
			{
				count++;
	//			cout << j << "-" << Nj << "  "; 
			}
	}
	else if(j<1000)
	{	
	
		int* Nj;
		Nj = new int[2];
		Nj[0] = 100 * a1 + 10 * a0 + a2;
		Nj[1] = 100 * a0 + 10 * a2 + a1;
		
		for(int i=0;i<2;i++)
		{
			for(int k=i+1;k<2;k++)
			{
				if(Nj[k] == Nj[i])
					Nj[k] =0;
			}
		}
		for(int i=0;i<2;i++)
		{
			if((Nj[i]>= a)&& (Nj[i]<=b)&&(Nj[i] > j))
			{
				count++;
		//		cout << j << "-" << Nj[i] << "  "; 
			}
		}
		delete[] Nj;
	}
	else if(j<10000)
	{
		a0 = j%10;
		a1 = (j%100-a0)/10;
	    a3 = j/1000;
		a2 = j/100-a3*10;
		int* mj;
		mj = new int[3];
		mj[0] = 1000 * a2 + 100 * a1 + 10 * a0 + a3;
	    mj[1] = 1000 * a1 + 100 * a0 + 10 * a3 + a2;
		mj[2] = 1000 * a0 + 100 * a3 + 10 * a2 + a1;
		
		for(int i=0;i<3;i++)
		{
			for(int k=i+1;k<3;k++)
			{
				if(mj[k] == mj[i])
					mj[k] =0;
			}
		}
		for(int i=0;i<3;i++)
		{
			if((mj[i]>= a)&& (mj[i]<=b)&&(mj[i] > j))
			{
				count++;
	//			cout << j << "-" << mj[i] << "  "; 
			}
		}
		delete[] mj;
	}
	else if(j<100000)
	{
		int a4;
		a0 = j%10;
		a1 = (j%100-a0)/10;
	    a3 = (j%10000-j%1000)/1000;
		a2 = (j%1000-j%100)/100;
		a4 = j/10000;

		int* mj;
		mj = new int[4];
		mj[0] = 10000 * a3 + 1000 * a2 + 100 * a1 + 10 * a0 + a4;
	    mj[1] = 10000 * a2 + 1000 * a1 + 100 * a0 + 10 * a4 + a3;
		mj[2] = 10000 * a1 + 1000 * a0 + 100 * a4 + 10 * a3 + a2;
		mj[3] = 10000 * a0 + 1000 * a4 + 100 * a3 + 10 * a2 + a1;
		
		for(int i=0;i<4;i++)
		{
			for(int k=i+1;k<4;k++)
			{
				if(mj[k] == mj[i])
					mj[k] =0;
			}
		}
		for(int i=0;i<4;i++)
		{
			if((mj[i]>= a)&& (mj[i]<=b)&&(mj[i] > j))
			{
				count++;
		//		cout << j << "-" << mj[i] << "  "; 
			}
		}
		delete[] mj;
	}
	else if(j<1000000)
	{
		int a4;
		int a5;
		a0 = j%10;
		a1 = (j%100-a0)/10;
	    a3 = (j%10000-j%1000)/1000;
		a2 = (j%1000-j%100)/100;
		a4 = (j%100000-j%10000)/10000;
		a5 = j/100000;

		int* mj;
		mj = new int[5];
		mj[0] = 100000 * a4 + 10000 * a3 + 1000 * a2 + 100 * a1 + 10 * a0 + a5;
	    mj[1] = 100000 * a3 + 10000 * a2 + 1000 * a1 + 100 * a0 + 10 * a5 + a4;
		mj[2] = 100000 * a2 + 10000 * a1 + 1000 * a0 + 100 * a5 + 10 * a4 + a3;
		mj[3] = 100000 * a1 + 10000 * a0 + 1000 * a5 + 100 * a4 + 10 * a3 + a2;
		mj[4] = 100000 * a0 + 10000 * a5 + 1000 * a4 + 100 * a3 + 10 * a2 + a1;
		
		for(int i=0;i<5;i++)
		{
			for(int k=i+1;k<5;k++)
			{
				if(mj[k] == mj[i])
					mj[k] =0;
			}
		}
		for(int i=0;i<5;i++)
		{
			if((mj[i]>= a)&& (mj[i]<=b)&&(mj[i] > j))
			{
				count++;
		//		cout << j << "-" << mj[i] << "  "; 
			}
		}
		delete[] mj;
	}
	else 
	{
		int a4;
		int a5;
		int a6;
		a0 = j%10;
		a1 = (j%100    -a0)       /10;
		a2 = (j%1000   -j%100)    /100;
	    a3 = (j%10000  -j%1000)   /1000;
		a4 = (j%100000 -j%10000)  /10000;
		a5 = (j%1000000-j%100000) /100000;
		a6 =  j/1000000;

		int* mj;
		mj = new int[6];
		mj[0] = 1000000 * a5 + 100000 * a4 + 10000 * a3 + 1000 * a2 + 100 * a1 + 10 * a0 + a6;
	    mj[1] = 1000000 * a4 + 100000 * a3 + 10000 * a2 + 1000 * a1 + 100 * a0 + 10 * a6 + a5;
		mj[2] = 1000000 * a3 + 100000 * a2 + 10000 * a1 + 1000 * a0 + 100 * a6 + 10 * a5 + a4;
		mj[3] = 1000000 * a2 + 100000 * a1 + 10000 * a0 + 1000 * a6 + 100 * a5 + 10 * a4 + a3;
		mj[4] = 1000000 * a1 + 100000 * a0 + 10000 * a6 + 1000 * a5 + 100 * a4 + 10 * a3 + a2;
		mj[5] = 1000000 * a0 + 100000 * a6 + 10000 * a5 + 1000 * a4 + 100 * a3 + 10 * a2 + a1;
		for(int i=0;i<6;i++)
		{
			for(int k=i+1;k<6;k++)
			{
				if(mj[k] == mj[i])
					mj[k] =0;
			}
		}
		for(int i=0;i<6;i++)
		{
			if((mj[i]>= a)&& (mj[i]<=b)&&(mj[i] > j))
			{
				count++;
			//	cout << j << "-" << mj[i] << "  "; 
			}
		}
		delete[] mj;
	}
	return count;
}