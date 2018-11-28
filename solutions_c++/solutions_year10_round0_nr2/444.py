#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <assert.h>
using namespace std;

struct vecInteger
{
	bool isNegative;
	vector<int> vec;
	vecInteger()
	{
		isNegative = false;
		vec.clear();
		vec.push_back(0);
	}
	void removeHeadingZero()
	{
		while (vec.back() == 0 && vec.size() > 1) vec.pop_back();
	}
	string toString()
	{
		removeHeadingZero();
		string ret;
		if (isNegative) ret+="-";
		for (int q=vec.size()-1;q>=0;--q) ret+=vec[q]+'0';
		return ret;
	}
	bool isZero()
	{
		removeHeadingZero();
		return (vec.size()==1 && vec[0]==0);
	}
	void operator-=(const vecInteger& obj)
	{
		assert(obj.isNegative == false);
		while (vec.size()<obj.vec.size()) vec.push_back(0);
		for (int q=0;q<obj.vec.size();++q)
		{
			int i = q;
			vec[i] -= obj.vec[i];
			while (i+1 < vec.size() && vec[i]<0) { vec[i]+=10; vec[i+1]--; i++; }
		}
		removeHeadingZero();
		if (vec.back()<0) 
		{
			isNegative = true;
			vec.back() *= -1;
		}
		//return *this;		
	}
	vecInteger operator-(const vecInteger& obj) const
	{
		vecInteger ret;
		ret = *this;
		ret-= obj;
		return ret;
	}
	vecInteger(char* tmp)
	{
		isNegative = false;
		vec.clear();
		for (int q=0;*(tmp+q);++q) vec.push_back(tmp[q]-'0');
		reverse(vec.begin(),vec.end());
	}
	void powerMinus(const vecInteger& obj)
	{
		int offset = 0;
		offset = vec.size() - obj.vec.size() - 1;
		if (offset<0) offset = 0;
		assert(obj.isNegative == false);
		for (int q=0;q<obj.vec.size();++q)
		{
			int i = q + offset;
			vec[i] -= obj.vec[i - offset];
			while (i+1 < vec.size() && vec[i]<0) { vec[i]+=10; vec[i+1]--; i++; }
		}
		removeHeadingZero();
		if (vec.back()<0) 
		{
			isNegative = true;
			vec.back() *= -1;
		}
		assert(isNegative == false);
	}
	bool operator<(const vecInteger& obj) const
	{
		if (vec.size() != obj.vec.size()) return vec.size() < obj.vec.size();
		for (int q=vec.size()-1;q>=0;--q)
			if (vec[q]!=obj.vec[q]) 
				return vec[q]<obj.vec[q];
		return false;
	}
};

vecInteger gcd(vecInteger a,vecInteger b)
{
	while (a.isZero() == false && b.isZero() == false)
	{
		if (a<b)
		{
			b.powerMinus(a);
			//b-=a;
		}
		else 
		{
			//a-=b;
			a.powerMinus(b);
		}
	}
	return a.isZero() ? b : a;
}
int gcd(int a,int b)
{
	while (a&&b)
	{
		a%=b;
		if (a) b%=a;
	}
	return a|b;
}

int main()
{
//#define USEINTEGER
	freopen("B-large.in","r",stdin);
	int T;
	scanf("%d",&T);
#ifdef USEINTEGER
	freopen("b-small-attempt2.real","w",stdout);
	for (int kase=1;kase<=T;++kase)
	{
		int N;
		int nums[1000];
		scanf("%d",&N);
		for (int q=0;q<N;++q) scanf("%d",nums+q);
		int T=abs(nums[0]-nums[1]);
		for (int q=0;q<N;++q) for (int w=q+1;w<N;++w)
			T=gcd(T,abs(nums[q]-nums[w]));
		nums[0] %= T;
		if (nums[0]) nums[0] = T - nums[0];
		printf("Case #%d: %d\n",kase,nums[0]);
	}
#else
	freopen("b-large.out","w",stdout);
	for (int kase=1;kase<=T;++kase)
	{
		fprintf(stderr,"%d\n",kase);
		int N;
		scanf("%d",&N);
		vecInteger nums[1000];
		for (int q=0;q<N;++q) 
		{
			char tmp[55];
			scanf("%s",tmp);
			nums[q] = vecInteger(tmp);
		}
		vecInteger T = (nums[0]<nums[1]) ? nums[1] - nums[0] : nums[0] - nums[1];
		if (T.isNegative) T.isNegative = false;
		for (int q=0;q<N;++q) for (int w=q+1;w<N;++w)
		{
			vecInteger delta = (nums[q]<nums[w]) ? nums[w] -nums[q]:nums[q] - nums[w];
			if (delta.isNegative) delta.isNegative = false;
			T=gcd(T,delta);
		}
		while (true)
		{
			if (nums[0]<T) break;
			//nums[0]-=T;
			nums[0].powerMinus(T);
		}
		if (nums[0].isZero() == false) nums[0] = T - nums[0];
		cout << "Case #" << kase << ": " << nums[0].toString() << endl;
	}
#endif
	return 0;
}