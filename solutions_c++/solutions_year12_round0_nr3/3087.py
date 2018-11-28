#include<iostream>
#include<cmath>
using namespace std;


int getLen(int num)
{
	int len = 0;
	while(num % 10 != num)
	{
		++len;
	}
	++len;
	return len;
}
int main()
{
	freopen("in.in" , "r" ,stdin);
	freopen("out.txt" , "w" ,stdout);




	int t, a, b;
	cin>>t;
	for(int i = 1; i <= t; ++i)
	{

		cin >> a >> b;
		int ans = 0;
		for(int s = a; s != b+1; ++s)
		{
			
			char s1[6];
			char s2[6];
			sprintf(s1 , "%d" , s);
			int len = strlen(s1);
			for(int i = 1 ; i < len ; ++i)
			{
				char c = s1[0];
				strcpy(s2,s1+1);
				s2[len-1] = c;
				s2[len] = 0;
				int num = atoi(s2);
				if(s2[0] == '0') {strcpy(s1,s2); continue;}
				if(s < num && num >= a && num <= b)
				{
			//		if(a == 1111)
			//		cout << s << " " << s2 << endl;
					++ans; 
				}
				strcpy(s1,s2);
			}
		}
		cout << "Case #"<< i <<": " <<ans << endl;
	}
	return 0;
}