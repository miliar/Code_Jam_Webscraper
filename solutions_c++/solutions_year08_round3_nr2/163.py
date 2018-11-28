#include<iostream>

using namespace std;

string S;
int total;
bool chk(long long number)
{
	if(number%2==0 || number%3==0 || number%5==0 || number%7==0)
		return 1;
	return 0;
}
void get(int pos, long long number, int f, long long curr, bool op)
{
	if(pos==S.size())
	{
		if(f)
			number-=curr;
		else
			number+=curr;
		if(chk(number))
			total++;
		return;
	}
	//cout<<pos<<" "<<number<<" "<<f<<" "<<curr<<" "<<op<<endl;
	get(pos+1,number,f,curr*10+S[pos]-'0',1);
	if(!f && op)
	{
		get(pos,number+curr,0,0,!op);
		get(pos,number+curr,1,0,!op);
	}
	else if(f && op)
	{
		get(pos,number-curr,0,0,!op);
		get(pos,number-curr,1,0,!op);
	}
}
			
int main()
{
	int T;
	int count=1;
	cin>>T;
	while(T--)
	{
		cin>>S;
		int i;
		long long n;
		total=0;
		get(1,0,0,S[0]-'0',1);
		cout<<"Case #"<<count<<": "<<total<<endl;
		count++;
	}
	return 0;
}




