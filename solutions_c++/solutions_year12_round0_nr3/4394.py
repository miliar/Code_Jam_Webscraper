#include<iostream>
#include<sstream>
#include<string>
using namespace std;
string convert_to_string(int num)
{
	string temp;
	stringstream ss;
	ss<<num;
	ss>>temp;
	return temp;
}
int convert_to_int(string num)
{
	int temp;
	stringstream ss;
	ss<<num;
	ss>>temp;
	return temp;
}
int check_recycled_pair(int A,int B,int num)
{
	if(num < 10)
		return 0;
	int count=0;
	string str_num = convert_to_string(num);
	string temp;
	int size=str_num.size();
	int recycled_num;
	for(int i=1;i<size;++i)
	{
		temp = str_num.substr(i,size-i) + str_num.substr(0,i);
		recycled_num=convert_to_int(temp);
		if(recycled_num >= A && recycled_num <= B && recycled_num > num)
			++count;
	}
	return count;
}
int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int cases;
	cin>>cases;
	int A,B;
	for(int i=1;i<=cases;++i)
	{
		cin>>A>>B;
		int count =0;
		for(int n=A;n<=B;++n)
			count += check_recycled_pair(A,B,n);
	cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}