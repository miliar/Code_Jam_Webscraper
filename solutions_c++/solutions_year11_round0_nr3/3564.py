#include <iostream>

using namespace std;

int main()
{

	freopen("C-large.in","r",stdin);	freopen("C-large.out","w",stdout);

	int T,N,c;
	//cin>>T;

	int Sum,Min,XorResult;
	int i = 1;

	scanf("%d",&T);

	while(T--){

		//cin>>N;
		scanf("%d",&N);

		Sum = 0;
		Min = INT_MAX;
		XorResult = 0;
		while(N--){
			//cin>>c;
			scanf("%d",&c);

			Sum += c;
			Min = min(c,Min);
			XorResult ^= c;
		}

		if(XorResult==0)
			cout<< "Case #" << i++ << ": " << (Sum-Min) << endl;
		else
			cout<< "Case #" << i++ << ": NO" << endl;
	}


	return 0;

}
