#include <iostream>
#include <fstream>
#include <math.h>
#include <cstdlib>
#include <set>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

int len;


bool recycled (char m[10],char n[10])
{
	bool retv;
	//int len=strlen(m);
	for (int offset=0;offset<len;offset++)
	{
		retv=true;
		for (int i=0;i<len;i++)
			if (m[i]!=n[(i+offset)%len]) {retv=false;break;};
		if (retv) return true;
	}
	return false;
};

void num_print(vector<char> &str, unsigned long n)
{
	int i=0;
	while (n)
	{
		str[i]=n%10;
		n/=10;
		i++;
	};
};

bool same_num(unsigned long k)
{
	int l=len;
	int d=k%10;
	while (l--)
	{
		if ((k%10)!=d) return false;
		k/=10;
	};

	return true;
};

unsigned long calc_num(vector<char> &str,int len)
{
	unsigned long ret=0;
	int f=1;int i=9;
	while (len--)
	{
		ret=ret+f*str[i];
		i--;f*=10;
	};
	return ret;
};

int num_pairs(int k)
{
	switch (k)
	{
	case(1): return 0;
	case(2): return 1;
	case(3): return 3;
	case(4): return 6;
	case(5): return 10;
	case(6): return 15;
	case(7): return 21;
	default: return 0;
	};
};

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	set<int> s,lo_s;s.clear();
	unsigned long **rec=new unsigned long*[1000000];
	rec[0]=new unsigned long[1000000*7];
	for (int i=1;i<1000000;i++)
		rec[i]=rec[i-1]+7;
	int num_rec=0;
	for (int i=0;i<1000000;i++)
		for (int j=0;j<7;j++)
			rec[i][j]=0;
	vector<char> num_s(10);

	ifstream fo("numlist2.bin",ifstream::binary);
	fo.read((char *)rec[0],sizeof(unsigned long)*7*1000000);

	////gen all recycled numbers
	//ofstream fo("numlist2.bin",ofstream::binary);
	//for (int i=12;i<2000000;i++)
	//{
	//	vector<char> num_s(10);
	//	len=ceil(log10((float)i));
	//	//num_print(num_s,i);
	//	//sort(num_s.begin(),num_s.end());
	//	unsigned long k=i;//=calc_num(num_s,len);
	//	if (s.count(k)||same_num(k)) continue;
	//	//gen all 
	//	s.insert(k);
	//	lo_s.clear();lo_s.insert(k);
	//	rec[num_rec][0]=k;
	//	//cout<<k<<' ';
	//	int factor=1;
	//	int j=len-1;unsigned long num_row=1;
	//	while (j--) factor*=10;
	//	j=len-1;
	//	while (j--)
	//	{
	//		int g=k%10;
	//		k/=10;
	//		k=k+g*factor;
	//		if ((ceil(log10((float)k))<len) || lo_s.count(k)) continue;
	//		rec[num_rec][num_row++]=k;
	//		//cout <<k<<' ';
	//		s.insert(k);lo_s.insert(k);
	//	};
	//	//cout << num_row << ' ';
	//	//for (int l=0;l<num_row;l++)
	//		//fo.write((char*)rec[0],sizeof(unsigned long)*7*1000000);
	//	//cout<<endl;
	//	num_rec++;
	//};
	//fo.write((char*)rec[0],sizeof(unsigned long)*7*1000000);return 0;

	int tc; 
	std::cin >> tc;
	for (int t=0;t<tc;t++)
	{
		int c=0;s.clear();
		unsigned long min,max;
		std::cin >> min >> max;
		//len=ceil(log10((float)max));
		unsigned long i=0;
		assert(i==0);
		assert(rec[0]);
		for (i=0;((i<1000000)&&(rec[i][0]<max));i++)
		{
			int lo_c=0;
			for (int j=0;j<7;j++)
				if ((rec[i][j]>=min) && (rec[i][j]<=max)) 
				{
					lo_c++;
					//cout<<rec[i][j]<<' ';
				};
			
			if (lo_c>1) 
			{
				//cout<<num_pairs(lo_c)<<endl;
				c+=num_pairs(lo_c);
			};
		}
		printf("Case #%d: %d\n",t+1,c);
	};
	return 0;
};

//int main()
//{
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("output.txt","w",stdout);
//	int tc; cin >> tc;
//	for (int t=0;t<tc;t++)
//	{
//		int c=0;
//		unsigned long min,max;
//		cin >> min >> max;
//		len=ceil(log10((float)max));
//		for (unsigned long i=min;i<=max;i++)
//			for (unsigned long j=i+1;j<=max;j++)
//		{
//			char num1[10],num2[10];
//			num_print(num1,i);
//			num_print(num2,j);
//			if (recycled(num1,num2)) {c++;
//			//cout << i<< ' '<<j<<endl;
//			};
//		};
//		printf("Case #%d: %d\n",t+1,c);
//	};
//	return 0;
//};

//bool recycled (unsigned long m,unsigned long n)
//{
//	if (m<10) return false;
//	int len=max<unsigned long>(ceil(log10((float)m)),ceil(log10((float)n)));
//	
//	int factor=1;
//	int i=len-1;
//	while (i--) factor*=10;
//	i=len;
//	while (i--)
//	{
//		int k=n%10;
//		n/=10;
//		n=n+k*factor;
//		if (n==m) return true;
//	};
//	return false;
//};
