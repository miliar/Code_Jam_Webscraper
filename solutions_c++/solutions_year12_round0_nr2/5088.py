#include <iostream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int i=0; i < T; i++)
	{
		cout<<"Case #"<<i+1<<": ";
		int N = 0,S = 0,p = 0;
		cin>>N;
		cin>>S;
		cin>>p;
		int leg = 0;
		int sur = 0;
		for(int j = 0; j < N;j++)
		{
			int temp = 0;
			cin>>temp;
			if( (temp%3) == 0 ) {
				if( (temp/3) >= p ) {
					leg++;
				} else if( ((temp/3)+1) >= p && (temp/3) != 0 ) {
					sur++;
				}
			} else if( (temp%3) == 1 ) {
				if( (temp/3) >= p ) {
					leg++;
				} else if( ((temp/3)+1) >= p && (temp/3) != 0 ) {
					leg++;
					//sur++;
				}
			} else {
				if( (temp/3) >= p || ((temp/3)+1) >= p ) {
					leg++;
				} else if( ((temp/3)+2) >= p && (temp/3) != 0 ) {
					sur++;
				}
			}
		}
		if( sur > S ) {
			leg = leg + S;
		} else {
			leg = leg + sur;
		}
		cout<<leg<<endl;
		sur = 0;
		leg = 0;
	}
	return 0;
}
