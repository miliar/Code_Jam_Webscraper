#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T,t=0;
	cin>>T;
	while(T--)
	{
		t++;
		char orig[30];
		cin>>orig;
		cout<<"Case #"<<t<<": ";
		int check=0;
		if(next_permutation(orig,orig+strlen(orig)))
		{
			check=1;
			cout<<orig<<endl;
		}
		prev_permutation(orig,orig+strlen(orig));
		while(check==0)
		{
			orig[strlen(orig)+1]='\0';
			for(int i=strlen(orig);i>=0;i--)
			{
				orig[i]^=orig[i-1]^=orig[i]^=orig[i-1];
			}
			orig[0]='0';
			if(next_permutation(orig,orig+strlen(orig)))
			{
				check=1;
				cout<<orig<<endl;
			}
		}
	}
	return 0;
}
