# include <iostream>
# include <fstream>
# include <vector>
# include <algorithm>

using namespace std;

int main()
{
	int cas=0,T;
	ifstream in("A-large.in");
	ofstream out("out");
//	ifstream in("A-small.in");

	in>>T;

	while(T--)
	{
		int n,k;
		
		in>>n>>k;
			
		if(n == 1)
		{
			if(k%2){
				out<<"Case #"<<++cas<<": "<<"ON"<<endl;
			}
			else{
				out<<"Case #"<<++cas<<": "<<"OFF"<<endl;
			}
			continue;
		}

		int d = 1;

		for(int i = 0;i<n;i++){
			d<<=1;
		}

		if((k+1)%d)
		{
			out<<"Case #"<<++cas<<": OFF"<<endl;		
		}
		else{
			out<<"Case #"<<++cas<<": ON"<<endl;
		}
	
	}

	return 0;
}

