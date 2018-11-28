#include <iostream>
#include <bitset>
using namespace std;
const int maxdev = 30;
void toggle(bitset<maxdev> &st,int n)
{
	int i;
	bool currstate;
	currstate=st.test(0);
	st.flip(0);
	for( i = 1;i < n ;i++)
	{
		if( currstate )
		{
			currstate = st.test(i);
			st.flip(i);
		}
		else
			break;
	}
	
}
int main()
{

	int T,N,K,i;
	bitset<maxdev> state;
	scanf("%d",&T);
	for (i=0 ;i < T ; i++)
	{
		scanf("%d%d",&N,&K);
		state.reset();
		int j =1;
		while (j <= K)
		{
			toggle(state,N);
			if( state.count() == N )
				break;
			j++;
		}
		if( (K >= j) && ((K +1) %(j+1) == 0) )
			cout<<"Case #"<<i+1<<":"<<" ON"<<endl;
		else
			cout<<"Case #"<<i+1<<":"<<" OFF"<<endl;

		
	}
	
}