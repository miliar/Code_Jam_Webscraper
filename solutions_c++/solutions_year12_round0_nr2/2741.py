
#include <iostream>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int N,S,p,y=0;

		cin>>N>>S>>p;
		//int *notes = new int(N);

		for(int j=0;j<N;j++)
			{int note; cin>>note;
			if(note>=3*p-2 || p==0) y++;
			else if ( note>=3*p-4 && S )  {if(p==1 && !note) break;
			 y++; S--;}
			}
		cout<<"Case #"<<i+1<<": "<<y<<endl;
		//delete [] notes;
	}
}
